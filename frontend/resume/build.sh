#!/bin/bash

# check if dist directory exists, if yes remove it
if [ -d "dist" ]; then
  rm -rf dist
  npm run build
  else
    npm run build
fi

# move dist files to static directory
rm -rf ../../app/static/*
cp -r dist/* ../../app/static/