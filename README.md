<!-- style>
  .license {
    color: blue;
    text-decoration: bold;
  }
  .license:hover{
    color: purple;
    text-decoration: underline;
    background-color: cyan;
    border-radius: 10px;
    padding: 2px;
  }
  .navbar {
    color: white;
    text-decoration: none;
    background-color: gray;
    border-radius: 5px;
    padding: 5px;
  }
  .navapps {
    color: white;
    background-color: #5D9B9B;
    padding: 5px;
    border-radius: 5px;
  }
  .navapps:hover {
    color: white;
    background-color:rgba(28, 113, 11, 0.86);
    padding: 5px;
    border-radius: 5px;
    text-decoration: none;
  }
  .navapps-active {
    color: white;
    background-color:rgb(9, 144, 255);
    border-radius: 5px;
    padding: 5px;
  }

  .navapps-active:hover {
    background-color: rgba(28, 113, 11, 0.86);
    border-radius: 5px
    border-style: solid;
    color: white;
    padding: 5px;
    text-decoration: none;
  }
</style> -->
<h1>Hello!</h1>
<div class="navbar" style="border: black">
<a class="navapps-active" href="https://github.com/Majix-Co/map-server/tree/main">Main Branch</a>
<a class="navapps" href="https://github.com/Majix-Co/map-server/tree/Linux-Installer-Tester">Linux-Test-Branch</a>
<!-- <a class ="navapps" href="https://github.com/Majix-Co/map-server/tree/Openbeta">OpenBeta</a> -->
<a class="navapps" href="https://github.com/Majix-Co/map-server/tree/Installmain">InstallMain</a>
</div>
<h2> Welcome to the Majix Application Portal Server (MAPS)</h2>
<h3> Welcome to the Linux Install Branch!</h3>
<h4>Here are some of the branch's</h4>
<hr>
<ul>
  <li>&#11088; Main Branch | Does not have a purpose
  <li>Installmain | Majix Installer Branch</li>
  <li>Openbeta | Beta's for main applications</li>
  <li>Linux-Installer-Tester | Used for Majix Co. Testing. Is used to check for bugs with the linux installer</li>
</ul>
<hr>
<h4> &#11088; == You are currently here</h4>
<hr>
<h3> How do I install?</h4>
<h4> Automated Install (Internet Required) (Is easier to use)</h4>

```
curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/install.py -o install.py | python3 install.py
```

<h4> Requirments!</h4>
<ul>
  <li> Curl (For building installer or online install only)</li>
  <li> Python3 | For debian linux Users: sudo apt-get python3 | Windows users: winget install python</li>
  <li> Cyryptography libary | pip install cryptography</li>
</ul>
<h4> Offline Install (Usally older version of install) only works on linux currently</h4>
<hr>
<h2><b>[DISCLAMER]</b> The offline install branch is in the process being removed. The Offline meBuilder will allow you to make offline installs. Until this is released do not expect offline support.</h2>
<br>
<h2>Sorry for the inconvience, But the builder will be easier to use, And easier to maintain, Meaning it will ALWAYS be up to date from the online install. (When builder is made within current version time-schedule)</h2>
<ol>
  <li> Make a new directory to put files in</li>
  <li> Make sure you installed python </li>
  <li>Paste the link in your web-browser on another computer or phone</li>
  <a href="https://github.com/Majix-Co/map-server/archive/refs/heads/offlineinstaller.zip">https://github.com/Majix-Co/map-server/archive/refs/heads/offlineinstaller.zip</a>
  <li> Add all files within in the directory you created</li>
  <li> unzip with unzip command and the file name example (unzip majixinstall.zip)</li>
  <li> Run "install.py" within that folder with "python3 install.py"</li>
  <li> Wait for it to install then delete the directory you created</li>
</ol>
<hr>
<h4> What is this branch used for?</h4>
<ul>
  <li> This branch is used for nothing</li>
  <li> Mostly this branch never changes</li>
  <li> So for consumers this branch is not used for much </li>
</ul>
<hr>
<h5> © Majix Co. 2025 | For most refrences MAP will refer to NWEA Map testing service. All refrences in this document or on any Majix Co. branded sites MAP or MAPS refers to Majix Application Portal Server or Majix Application Portal. These are not valid copyrights in US law HOWEVER any data or scripts provided under this name are protected by LAW under "GNU GENERAL PUBLIC LICENSE." For more info about this license <a class="license" href="https://www.gnu.org/licenses/gpl-3.0.en.html">click here</a></h5>
</body>
</html>
