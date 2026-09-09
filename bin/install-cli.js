#!/usr/bin/env node

/**
 * Avari Pet v2 Installer for ChatGPT / Codex Desktop
 * Usage:
 *   npx avari-pet
 *   npx github:OstKost/avari-pet
 *   node bin/install-cli.js [--target <custom_path>]
 */

const fs = require('fs');
const path = require('path');
const os = require('os');
const https = require('https');

const PET_ID = 'avari';
const REPO_RAW_BASE = 'https://raw.githubusercontent.com/OstKost/avari-pet/main/dist';

function parseArgs() {
  const args = process.argv.slice(2);
  let targetDir = null;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--target' || args[i] === '-t') {
      targetDir = args[i + 1];
      i++;
    }
  }
  return { targetDir };
}

function getCodexPetDir(customTarget) {
  if (customTarget) {
    return path.resolve(customTarget);
  }
  const codexHome = process.env.CODEX_HOME || path.join(os.homedir(), '.codex');
  return path.join(codexHome, 'pets', PET_ID);
}

function downloadFile(url, destPath) {
  return new Promise((resolve, reject) => {
    const fileStream = fs.createWriteStream(destPath);
    https.get(url, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        return downloadFile(res.headers.location, destPath).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        return reject(new Error(`Failed to download ${url}: HTTP ${res.statusCode}`));
      }
      res.pipe(fileStream);
      fileStream.on('finish', () => {
        fileStream.close();
        resolve();
      });
    }).on('error', (err) => {
      fs.unlink(destPath, () => {});
      reject(err);
    });
  });
}

async function install() {
  console.log('\n🔮 \x1b[36m\x1b[1mAvari Pet v2 Installer\x1b[0m');
  console.log('   White elf companion for ChatGPT / Codex Desktop\n');

  const { targetDir: customTarget } = parseArgs();
  const destDir = getCodexPetDir(customTarget);

  console.log(`📁 Target directory: \x1b[33m${destDir}\x1b[0m`);

  try {
    fs.mkdirSync(destDir, { recursive: true });
  } catch (err) {
    console.error(`\x1b[31m❌ Error creating directory ${destDir}:\x1b[0m`, err.message);
    process.exit(1);
  }

  const localDistDir = path.join(__dirname, '..', 'dist');
  const filesToInstall = ['pet.json', 'spritesheet.webp'];

  for (const file of filesToInstall) {
    const localSrc = path.join(localDistDir, file);
    const destFile = path.join(destDir, file);

    if (fs.existsSync(localSrc)) {
      // Local copy from npm package / repo
      fs.copyFileSync(localSrc, destFile);
      const sizeMb = (fs.statSync(destFile).size / (1024 * 1024)).toFixed(2);
      console.log(`   \x1b[32m✔\x1b[0m Installed ${file} (${sizeMb} MB)`);
    } else {
      // Fallback: download from GitHub
      const url = `${REPO_RAW_BASE}/${file}`;
      process.stdout.write(`   ⏳ Downloading ${file}... `);
      try {
        await downloadFile(url, destFile);
        const sizeMb = (fs.statSync(destFile).size / (1024 * 1024)).toFixed(2);
        console.log(`\x1b[32m✔\x1b[0m (${sizeMb} MB)`);
      } catch (err) {
        console.error(`\x1b[31mFailed\x1b[0m\n❌ Error: ${err.message}`);
        process.exit(1);
      }
    }
  }

  console.log('\n\x1b[32m\x1b[1m✨ Avari successfully installed!\x1b[0m\n');
  console.log('👉 \x1b[1mNext steps:\x1b[0m');
  console.log('   1. Restart or reload \x1b[36mChatGPT Desktop / Codex\x1b[0m.');
  console.log('   2. Select \x1b[35mAvari\x1b[0m in your pet selector.');
  console.log('   3. Enjoy coding with your magical white elf companion! 🪄✨\n');
}

install().catch((err) => {
  console.error('\x1b[31m❌ Installation failed:\x1b[0m', err);
  process.exit(1);
});
