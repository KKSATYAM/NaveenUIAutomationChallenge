# Node.js--> H1 heading

[open governance model](./GOVERNANCE.md)---> hyperlink for .md file located in the current directory

**This project has a [Code of Conduct][].**----> to bold out the content

## Table of contents---> H2 heading

* [Support](#support) -----> table index with #support tagges

[semantic versioning](https://semver.org).---> hyperlink for particular https link with text as semantic versioning

### Download------> H3 heading

#### Current and LTS releases------> H4 heading

<https://nodejs.org/download/release/>---> way to add hyperlink with same text

`SHASUMS256.txt` ---> way to highlight the text

```bash
curl -O https://nodejs.org/dist/vx.y.z/SHASUMS256.txt----> way to add the bash command
```

<details>

<summary>Emeriti</summary>

* [yosuke-furukawa](https://github.com/yosuke-furukawa) -
  **Yosuke Furukawa** <<`yosuke.furukawa@gmail.com`>>

</details>

## Release types

* **Current**: Under active development. Code for the Current release is in the
  branch for its major version number (for example,
  [v19.x](https://github.com/nodejs/node/tree/v19.x)). Node.js releases a new
  major version every 6 months, allowing for breaking changes. This happens in
  April and October every year. Releases appearing each October have a support
  life of 8 months. Releases appearing each April convert to LTS (see below)
  each October.
* **LTS**: Releases that receive Long Term Support, with a focus on stability
  and security. Every even-numbered major version will become an LTS release.
  LTS releases receive 12 months of _Active LTS_ support and a further 18 months
  of _Maintenance_. LTS release lines have alphabetically-ordered code names,
  beginning with v4 Argon. There are no breaking changes or feature additions,
  except in some special circumstances.
* **Nightly**: Code from the Current branch built every 24-hours when there are
  changes. Use with caution.




  

Current and LTS releases follow [semantic versioning](https://semver.org). A
member of the Release Team [signs](#release-keys) each Current and LTS release.
For more information, see the



</a>
  <a title="Localised" href="https://crowdin.com/project/nodejs-web">
    <img src="https://badges.crowdin.net/nodejs-web/localized.svg" />
 </a>
[Release README](https://github.com/nodejs/Release#readme).

## Support

Looking for help? Check out the
[instructions for getting support](.github/SUPPORT.md).
