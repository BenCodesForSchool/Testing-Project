const cucumber = require('cypress-cucumber-preprocessor').default;
const webpack = require('@cypress/webpack-preprocessor');

module.exports = (on, config) => {
  on('file:preprocessor', cucumber());
  on('file:preprocessor', webpack({
    webpackOptions: require('../webpack.config'),
    watchOptions: {}
  }));
};
