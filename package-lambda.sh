#!/bin/bash
set -e
echo "Packaging Lambda Function..."
rm -rf build
mkdir -p build
pip install -r requirements.txt -t build/ --upgrade
cp lambda_function.py build/
cd build
zip -r ../lambda-source.zip . -q
cd ..
echo "✅ Package created: lambda-source.zip"
