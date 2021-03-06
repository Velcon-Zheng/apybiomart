#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os

from click.testing import CliRunner
import pytest  # noqa

from apybiomart import cli


def test_cli_filters_default():
    """Test the available attributes returned by apybiomart filters for the
    default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["filters"])
    assert result.exit_code == 0
    assert "Filter ID" in result.output
    assert "link_so_mini_closure" in result.output
    assert "hsapiens_gene_ensembl" in result.output


def test_cli_filters_saved():
    """Test the saved attributes returned by apybiomart filters for the
    default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["filters", "--save"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("apybiomart_filters.csv")
    finally:
        os.remove("apybiomart_filters.csv")


def test_cli_filters_output():
    """Test the saved attributes returned by apybiomart filters with a given
    filename for the default dataset (hsapiens_gene_ensembl)."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["filters", "--save",
                                      "--output", "tested.csv"])
    try:
        assert result.exit_code == 0
        assert os.path.isfile("tested.csv")
    finally:
        os.remove("tested.csv")


def test_cli_filters_ontology():
    """Test the available attributes returned by apybiomart filters for the
    closure_ECO dataset."""
    runner = CliRunner()
    result = runner.invoke(cli.main,
                           ["filters",
                            "--dataset", "closure_ECO"])
    assert result.exit_code == 0
    assert "Filter ID" in result.output
    assert "accession_305" in result.output
    assert "closure_ECO" in result.output
