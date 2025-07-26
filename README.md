### Automation Lab, Sungkyunkwan University

#### GitHub Stats

![](https://img.shields.io/github/downloads/SKKU-AutoLab-VSW/ETSS-08-Data/total.svg?style=for-the-badge)



# Traffic Surveillance Dataset

1. Traffic Surveillance Data Generation capable of producing various environment record on road by using Carla.

  ![gif](attachments/traffic_surveillance_intersection.gif)


2. Real-world traffic surveillance systems



## I. Using CARLA

<details open>

  <summary>Building CARLA, Instruction, and samples</summary>

  ### 1. Building CARLA

  Use `git clone` or download the project from [CARLA Github][carlagithublink].

  Then follow the instruction at [How to build on Linux][buildlinuxlink] or [How to build on Windows][buildwindowslink].

  The Linux build needs for an UE patch to solve some visualization issues regarding Vulkan. Those already working with a Linux build should insta


  ### 2. Instructionll the patch and make the UE build again using the following commands.

  ```sh
  # Download and install the UE patch  
  cd ~/UnrealEngine_4.24
  wget https://carla-releases.s3.eu-west-3.amazonaws.com/Linux/UE_Patch/430667-13636743-patch.txt ~/430667-13636743-patch.txt
  patch --strip=4 < ~/430667-13636743-patch.txt

  # Build UE
  ./Setup.sh && ./GenerateProjectFiles.sh && make
  ```

  [carlagithublink]: https://github.com/carla-simulator/carla
  [buildlinuxlink]: https://carla.readthedocs.io/en/latest/build_linux/
  [buildwindowslink]: https://carla.readthedocs.io/en/latest/build_windows/
  

  Please refer to [INSTRUCTION.md](DataGeneration-CARLA/Instruction.md) for how to use.


  ### 3. Sample

  Please go to this repository for [Realistic-Traffic-Surveillance Generated Sample](https://github.com/SKKU-AutoLab-VSW/Realistic-Traffic-Surveillance_GeneratedSample)

</details open>


## II. Real-world System

We are conducting research to develop a real-world traffic surveillance system.

Read the [Introduction][RealWorldSystem/README.md] for more details.


## III. Citation 

If you find our work helpful for your research, please consider citing the following BibTeX entry.

```bibtex
@misc{AutoLab-Dataset-CARLA,
  author = {Automation Laboratory},
  license = {Apache-2.0},
  title = {Traffic Surveillance Dataset},
  howpublished = {\url{https://github.com/SKKUAutoLab/ETSS-08-Data}},
  year = {2025},
  note = {Data Generation using Carla}
}
```


## IV. License

Both the code and the weights pretrained on the COCO dataset are released under the [Apache 2.0 license](/LICENSE).