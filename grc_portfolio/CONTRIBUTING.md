# Contributing to GRC Portfolio Hub

First off, thank you for considering contributing to the GRC Portfolio Hub! This project exists because of the efforts of people like you.

## Code of Conduct

By participating in this project, you agree to abide by the [GitHub Community Guidelines](https://docs.github.com/en/site-policy/github-terms/github-community-guidelines). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the behavior, and find related reports.

* **Use the GitHub issue tracker** - Create issues in the repository's issue tracker to report bugs.
* **Describe the bug** - Provide a clear and descriptive title and details about the bug.
* **Include reproduction steps** - Tell us how to reproduce the issue.
* **Specify your environment** - Include which AWS region, tool versions, etc.
* **Include screenshots** - If applicable, add screenshots to help explain your problem.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

* **Use the GitHub issue tracker** - Create issues in the repository's issue tracker for enhancement suggestions.
* **Describe the enhancement** - Provide a clear and descriptive title and explanation of the proposed feature.
* **Provide specific examples** - Include copy/pasteable snippets and examples of how the feature would be used.
* **Describe the current behavior and explain the behavior you expected**
* **Explain why this enhancement would be useful** to most GRC Portfolio Hub users.

### Your First Code Contribution

Unsure where to begin contributing? Look for these labels in the issue tracker:

* `good first issue` - issues which are ideal for beginners.
* `help wanted` - issues that need assistance.
* `documentation` - improvements to documentation.

### Pull Requests

* Fill in the required pull request template.
* Follow the [styleguides](#styleguides).
* After you submit your pull request, verify that all status checks are passing.
* Request review from one of the project maintainers.

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature").
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
* Limit the first line to 72 characters or less.
* Reference issues and pull requests liberally after the first line.

### Markdown Styleguide

* Use [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).
* Structure documents with clear headings and subheadings.
* Use code blocks for all code examples.
* Include alt text for all images.
* Link to relevant resources where appropriate.

### Code Styleguide

#### CloudFormation
* Follow the [AWS CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html).
* Use descriptive logical IDs for resources.
* Use clear, descriptive parameter names.
* Include descriptions for all parameters.
* Use parameter constraints where appropriate.
* Provide default values where it makes sense.
* Include comments to explain complex logic.

#### AWS CDK
* Follow the [AWS CDK Best Practices](https://docs.aws.amazon.com/cdk/latest/guide/best-practices.html).
* Use constructs consistently.
* Use clear, descriptive names for constructs and properties.
* Create reusable constructs for common patterns.
* Include comments to explain complex logic.

#### Python
* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
* Use docstrings for all functions, classes, and modules.
* Include type hints where appropriate.
* Write unit tests for all functions.
* Handle errors gracefully.

#### Bash
* Follow the [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html).
* Use shellcheck to validate your scripts.
* Include usage examples in comments.
* Handle errors and edge cases.

### Documentation Styleguide

* Start each lab with clear objectives.
* Include prerequisite information.
* Provide step-by-step instructions.
* Use screenshots and diagrams where helpful.
* Include expected outcomes.
* Provide troubleshooting guidance.
* End with cleanup instructions.

## Lab Contribution Guidelines

When contributing a new lab, please ensure it includes:

1. **README.md** with:
   * Lab title and description
   * Learning objectives
   * Prerequisites
   * Estimated time to complete
   * Cost estimate

2. **Architecture diagram** showing the solution components

3. **Step-by-step guide** with detailed instructions

4. **Code** including:
   * CloudFormation templates
   * AWS CDK constructs (if applicable)
   * Any necessary scripts
   * Cleanup scripts

5. **Validation checklist** to verify correct implementation

6. **Challenges** of varying difficulty levels

## Portfolio Template Contribution Guidelines

When contributing a new portfolio template, please ensure it includes:

1. **Clear structure** with sections for:
   * Introduction
   * Technical skills
   * Projects
   * Certifications
   * Education
   * Contact information

2. **Formatting guidance** for users

3. **Examples** of how to showcase projects

4. **Instructions** on customization

## Review Process

All contributions will go through the following review process:

1. Initial review
2. Technical validation of any code
3. Documentation review
4. Final approval and merge

I aim to review all pull requests within 7 days, but please be patient as I manage this repository in my spare time.

## Recognition

All contributors will be recognized in the project README. Significant contributions may be highlighted in project announcements.

## Questions?

If you have any questions about contributing, please open an issue with your question or contact one of the project maintainers.

Thank you for your interest in improving the GRC Portfolio Hub! 