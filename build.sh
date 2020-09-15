#!/usr/bin/env bash
# . ~/.bash_profile

OS=$(uname -s)
echo $OS

if [ "$OS" = "Darwin" ]; then
  DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
else
  full_path=$(realpath $0)
  DIR=$(dirname $full_path)
fi

echo $DIR

cd $DIR && rm -rf build *.egg-info dist && pip3 uninstall messagehub -y && python3 setup.py bdist_wheel && pip3 install dist/messagehub-0.1.2-py3-none-any.whl

pip3 list | grep messagehub
echo "=====messagehub install ok====="


