{ pkgs ? import <nixpkgs> {} }:
let
  python-packages = ps: with ps; [
      jupyter
      ipython
      pip
  ];
  my-python = pkgs.python310.withPackages python-packages;
in my-python.env
