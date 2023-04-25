<!-- 
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/frankmaina/kollector">
    <img src="https://github.com/frankmaina/kollector/blob/master/static/logo/main.png?raw=true" alt="Kollector" width="300" height="300">
  </a>


<h3 align="center">Kollector</h3>

  <p align="center">
    Kollector is a web api platform that enables business/users to build dynamic forms and subsequently submit data based on the defined form schema.
    <br />
  </p>
</div>

> **Warning**
> The project is currently in its early stages of development and may not be suitable for use in Production environments.


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
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The platform provides users with the capability to define a comprehensive form schema by specifying a particular set of fields and corresponding rules. This schema can be leveraged to validate the submitted form data to ensure that it adheres to the specified rules.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![FastAPI][FastAPI.com]][Fastapi-url]
* [![Python][Python.org]][Python-url]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The quickest way to get started (right now) is to set up a python environment locally and couple the installation with a local or remote MongoDB installation, or alternatively, use a running Docker container with MongoDB.

### Installation

1. ```sh
   virtualenv venv
   ```
2. Switch to environment
   ```sh
   source venv/bin/activate 
   ```
3. Install PIP packages
   ```sh
   pip install -r requirements.txt
   ```
4. Start the local server
   ```sh
   ./start_server.sh 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] Form Data CRUD
- [ ] House Keeping, (tests, propper logging, timestamps)
- [ ] Add support for User management using Zitadel
- [ ] Support for Docker Compose
- [ ] Mobile Client
    - [ ] Web Client
- [ ] Streaming Events

See the [open issues](https://github.com/frankmaina/kollector/issues) for a full list of known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Img Shields](https://shields.io)
* [ReadMe Template](https://github.com/othneildrew/Best-README-Template)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/frankmaina/kollector.svg?style=for-the-badge
[contributors-url]: https://github.com/frankmaina/kollector/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/frankmaina/kollector.svg?style=for-the-badge
[forks-url]: https://github.com/frankmaina/kollector/network/members
[stars-shield]: https://img.shields.io/github/stars/frankmaina/kollector.svg?style=for-the-badge
[stars-url]: https://github.com/frankmaina/kollector/stargazers
[issues-shield]: https://img.shields.io/github/issues/frankmaina/kollector.svg?style=for-the-badge
[issues-url]: https://github.com/frankmaina/kollector/issues
[license-shield]: https://img.shields.io/github/license/frankmaina/kollector.svg?style=for-the-badge
[license-url]: https://github.com/frankmaina/kollector/blob/master/LICENSE.txt
[Python.org]: https://img.shields.io/badge/-Python-blue?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[FastAPI.com]: https://img.shields.io/badge/-FastAPI-black?style=for-the-badge&logo=fastapi&logoColor=white
[Fastapi-url]: https://fastapi.tiangolo.com/