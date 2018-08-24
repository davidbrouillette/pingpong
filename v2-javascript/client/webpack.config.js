const path = require('path');
module.exports = {
  entry: './src/index.js',
  output: {
    path: path.join(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
        test: /\.js|jsx$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query: {
          presets: [ 'env', 'react']
        }
      },
      {
          test: /\.css$/,
          use: [
              {
                  loader: 'style-loader',
                  options: {
                      hmr: true
                  }
              },
              {
                  loader: 'css-loader',
                  options: {
                      importLoaders: 1,
                      minimize: false,
                      sourceMap: true
                  }
              }
            ]
      }
    ]
  }
};