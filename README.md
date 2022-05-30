<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">


<h3 align="center">Solution Ioet Coding Exercise</h3>

  <p align="center">
    This is my proposed solution built with Python for the Ioet Coding Exercise.
    <br />
    <a href="https://github.com/asperduti/ioet-coding-exercise"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/asperduti/ioet-coding-exercise">View Demo</a>
    ·
    <a href="https://github.com/asperduti/ioet-coding-exercise/issues">Report Bug</a>
    ·
    <a href="https://github.com/asperduti/ioet-coding-exercise/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
        <li>
      <a href="#coding-exercise">Coding Exercise</a>
      <ul>
        <li><a href="#description">Description</a></li>
        <li><a href="#solution">Solution</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python 3.10](https://www.python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

  - Python 3.10

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/asperduti/ioet-coding-exercise.git
   ```
3. Install Python packages, just for dev(testing, formatting, etc.)
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->



##  Coding Exercise

### Description

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Time/Day      | Monday - Friday | Saturday and Sunday |
| ------------- | --------------- | ------------------- |
| 00:01 - 09:00 | 25 USD          | 30 USD              |
| 09:01 - 18:00 | 15 USD          | 20 USD              |
| 18:01 - 00:00 | 20 USD          | 25 USD              |


The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

 - MO: Monday
 - TU: Tuesday
 - WE: Wednesday
 - TH: Thursday
 - FR: Friday
 - SA: Saturday
 - SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

*Case 1:*

> INPUT
> 
> RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
>
> OUTPUT:
>
> The amount to pay RENE is: 215 USD

*Case 2:*

> INPUT
>
> ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
>
> OUTPUT:
> 
> The amount to pay ASTRID is: 85 USD



### Solution

Due to the simplicity of the initial problem, I can use a few functions in a Python script to solve the problem. But thinking that the business description can change in the future, the system can grow up, and the idea of the challenge is to show the development skills to solve a real problem, I'm going to take an approach a bit more sophisticated, making the solution scalable, easy to maintain and extend.

With that in mind, I'll follow the OOD methodology to solve the problem. I split the problem into minor parts, thinking about these parts as the entities that I can identify from the business description (User/Employee, hours worked, data) and some other entities not explicitly mentioned in the business description, but they will give the possibility to extend the solution, like (Parser, DataLoader, Output).

I decided to use the TDD process to build the solution, always using good principles in the development process.

## Roadmap

See the [open issues](https://github.com/asperduti/ioet-coding-exercise/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/asperduti/ioet-coding-exercise](https://github.com/asperduti/ioet-coding-exercise)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/asperduti/ioet-coding-exercise.svg?style=for-the-badge
[contributors-url]: https://github.com/asperduti/ioet-coding-exercise/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/asperduti/ioet-coding-exercise.svg?style=for-the-badge
[forks-url]: https://github.com/asperduti/ioet-coding-exercise/network/members
[stars-shield]: https://img.shields.io/github/stars/asperduti/ioet-coding-exercise.svg?style=for-the-badge
[stars-url]: https://github.com/asperduti/ioet-coding-exercise/stargazers
[issues-shield]: https://img.shields.io/github/issues/asperduti/ioet-coding-exercise.svg?style=for-the-badge
[issues-url]: https://github.com/asperduti/ioet-coding-exercise/issues
[license-shield]: https://img.shields.io/github/license/asperduti/ioet-coding-exercise.svg?style=for-the-badge
[license-url]: https://github.com/asperduti/ioet-coding-exercise/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/arielsperduti
[product-screenshot]: images/screenshot.png
