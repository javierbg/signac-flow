# <img src="https://raw.githubusercontent.com/glotzerlab/signac-flow/main/doc/images/palette-header.png" width="75" height="58"> signac-flow - manage workflows with signac

[![Affiliated with NumFOCUS](https://img.shields.io/badge/NumFOCUS-affiliated%20project-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org/sponsored-projects/affiliated-projects)
[![PyPI](https://img.shields.io/pypi/v/signac-flow.svg)](https://pypi.org/project/signac-flow/)
[![conda-forge](https://img.shields.io/conda/vn/conda-forge/signac-flow.svg?style=flat)](https://anaconda.org/conda-forge/signac-flow)
[![RTD](https://img.shields.io/readthedocs/signac.svg?style=flat)](https://docs.signac.io)
[![License](https://img.shields.io/github/license/glotzerlab/signac-flow.svg)](https://github.com/glotzerlab/signac-flow/blob/main/LICENSE.txt)
[![PyPI-downloads](https://img.shields.io/pypi/dm/signac-flow.svg?style=flat)](https://pypistats.org/packages/signac-flow)
[![Slack](https://img.shields.io/badge/Slack-chat%20support-brightgreen.svg?style=flat&logo=slack)](https://signac.io/slack-invite/)
[![Twitter](https://img.shields.io/twitter/follow/signacdata?style=social)](https://twitter.com/signacdata)
[![GitHub Stars](https://img.shields.io/github/stars/glotzerlab/signac-flow?style=social)](https://github.com/glotzerlab/signac-flow/)

The [**signac** framework](https://signac.io) helps users manage and scale file-based workflows, facilitating data reuse, sharing, and reproducibility.

The **signac-flow** tool provides the basic components to set up simple to complex workflows for projects managed by the [**signac** framework](https://signac.io).
That includes the definition of data pipelines, execution of data space operations and the submission of operations to high-performance super computers.

## Resources

- [Framework documentation](https://docs.signac.io/):
  Examples, tutorials, topic guides, and package Python APIs.
- [Package documentation](https://docs.signac.io/projects/flow/):
  API reference for the **signac-flow** package.
- [Slack Chat Support](https://signac.io/slack-invite/):
  Get help and ask questions on the **signac** Slack workspace.
- [**signac** website](https://signac.io/):
  Framework overview and news.


## Installation

The recommended installation method for **signac-flow** is through **conda** or **pip**.
The software is tested for Python versions 3.6+ and is built for all major platforms.

To install **signac-flow** *via* the [conda-forge](https://conda-forge.github.io/) channel, execute:

```bash
conda install -c conda-forge signac-flow
```

To install **signac-flow** *via* **pip**, execute:

```bash
pip install signac-flow
```

**Detailed information about alternative installation methods can be found in the [documentation](https://docs.signac.io/en/latest/installation.html).**


## Testing

You can test this package by executing

    $ python -m pytest tests/

within the repository root directory.


## Acknowledgment

When using **signac** as part of your work towards a publication, we would really appreciate that you acknowledge **signac** appropriately.
We have prepared examples on how to do that [here](http://docs.signac.io/en/latest/acknowledge.html).
**Thank you very much!**

The signac framework is a [NumFOCUS Affiliated Project](https://numfocus.org/sponsored-projects/affiliated-projects).
