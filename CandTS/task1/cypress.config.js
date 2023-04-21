const cucumber = require('cypress-cucumber-preprocessor').default;
const browserify = require('@cypress/browserify-preprocessor');
const resolve = require('resolve');

module.exports = {
  fileServerFolder: ".",
  fixturesFolder: false,
  plugins: [
    browserify({
      typescript: resolve.sync('typescript', { basedir: __dirname }),
      transformOptions: {
        extensions: ['.js', '.ts']
      }
    }),
    cucumber(),
  ],
  e2e: {
    specPattern: "cypress/integration/**/*.spec.ts",
    supportFile: "cypress/support/index.ts",
    cucumber: {
      require: ['./cypress/integration/**/*.ts'],
      tags: '@all',
      format: 'json:cypress/cucumber-json/cucumber.json',
    },
    setupNodeEvents: (on, config) => {
      on('before:browser:launch', (browser = {}, launchOptions) => {
        if (browser.name === 'chrome') {
          launchOptions.extensions.push('cypress/extensions/uBlock0_1.47.4.firefox.signed.crx');
        }
        return launchOptions;
      });
    }
  },
  component: {
    spec: 'cypress/integration/**/*.spec.ts',
    supportFile: "cypress/support/index.ts",
    baseUrl: 'http://localhost:3000',
    setupNodeEvents: (on, config) => {
      // implement node event listeners here
    },
  }
};
