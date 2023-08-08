ZotFileCleaner
==============
An utility to find pdf files that are locally stored in Zotero database instead of ZotFile custom locations.

## 0. Prerequisite
This utility relies on the `ZotFile` and `Better Bibtex` plugins. If you use them too, you may face the same problem as me. 

Environment: `Python3` and [`bibtexparser`](https://github.com/sciunto-org/python-bibtexparser)

```sh
pip install --no-cache-dir --force-reinstall git+https://github.com/sciunto-org/python-bibtexparser@main
pip install send2trash
```

##  1. Preparation in Zotero
- [ ] Remember the `Custom Location` setting in the `ZotFile Preferences`:  
![1](https://github.com/TimoLin/Zotero-ZotFileCleaner/assets/7792396/e2e4956d-9e4a-4d1e-bd3a-03d964b31e12)

- [ ] In Zotero, click (1)`File`->(2)`Export Library`->(3)`Select Better BibTex`->(3)Check `Keep updated` option->(4)Save the bib file to any folder your like.  
![2](https://github.com/TimoLin/Zotero-ZotFileCleaner/assets/7792396/c5053768-56af-4904-8f93-f7864beb2c0e)

## 2. Run the script
```sh
$ python3 ~/github/Zotero/src/zotfileCleaner.py -h
usage: zotfileCleaner.py [-h] -f FILE -c CUSTOMLOCATION [-e] [-d]

ZotFileCleaner: An utility to find pdf files that are locally stored in Zotero
database instead of ZotFile custom locations.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Zotero automatic exported better bibtex lib file.
  -c CUSTOMLOCATION, --customlocation CUSTOMLOCATION
                        Custom location defined in ZotFile preferences.
  -e, --empty           Print items without any attachment files.
  -d, --delete          Clean up the zombie files under ZotFile folder .
```
### Examples
1. Find the items that are locally stored in Zotero database instead of ZotFile custom locations
    ```
    # Replace with your own path
    python3 ~/github/Zotero/src/zotfileCleaner.py -f "YOUR/PATH/mylib.bib" -c "YOUR/ZOTFILE/CUSTOM/PATH"
    ```
    ```console
    # Output
    Citation keys of the files in Zotero database: 2
      labahnLeanBlowoutSimulations
      wangLargeeddySimulationsFlow2020
    ---------------------------------------------
    ZotFile zombie files: 7
    Done!
    ```
2. Find the items without any attachment files
    ```sh
    # Replace with your own path
    python3 ~/github/Zotero/src/zotfileCleaner.py -f "YOUR/PATH/mylib.bib" -c "YOUR/ZOTFILE/CUSTOM/PATH" -e
    ```
    ```console
    # Output
    Citation keys of the files in Zotero database: 2
      labahnLeanBlowoutSimulations
      wangLargeeddySimulationsFlow2020
    ---------------------------------------------
    Citation keys of items without attachment files: 123
      ahnHeatReleaseRate2022
      aignerSwirlCounterswirlEffects1988
      aignerSwirlCounterswirlEffects1988a
      andreiniLocalSourceBased2013
      ansysinc.ANSYSFluentTheory
      ...
      zhouyuTongZhouSheLiuRanShaoShiFeiYuHunTuanLiuRanShaoLiuChangTeXingDaWoMoNiYanJiu2017
    ---------------------------------------------
    ZotFile zombie files: 7
    Done!
    ```
3. Delete the ZotFile zombie files
    ```sh
    # Replace with your own path
    python3 ~/github/Zotero/src/zotfileCleaner.py -f "YOUR/PATH/mylib.bib" -c "YOUR/ZOTFILE/CUSTOM/PATH" -d
    ```
    ```console
    #Output
    Citation keys of the files in Zotero database: 2
      labahnLeanBlowoutSimulations
      wangLargeeddySimulationsFlow2020
    ---------------------------------------------
    ZotFile zombie files: 7
    ---------------------------------------------
    Moving Zombie Files to Trash...
      /Dropbox/Zotero/_/李林_et_al_一种双预膜气动雾化低污染燃烧室头部结构.pdf
      /Dropbox/Zotero/2018/夏朝阳_et_al_2018_基于FGM的湍流射流扩散火焰超大涡模_拟.pdf
      /Dropbox/Zotero/2015/Zips_et_al_2015_Numerical_simulation_of_a_single-element_GOx-GCH_4_rocket.pdf
      /Dropbox/Zotero/Science China Technological Sciences2015/Zhang_et_al_2015_Large_eddy_simulation_of_unconfined_turbulent_swirling_flow.pdf
      /Dropbox/Zotero/Combustion and Flame2020/Zadsirjan_et_al_2020_Large_eddy_simulation_of_turbulent_diffusion_jet_flames.pdf
      /Dropbox/Zotero/Chinese Journal of Aeronautics2015/Zhiyin_2015_Large-eddy_simulation.pdf
      /Dropbox/Zotero/Combustion and Flame2021/Zhong_et_al_2021_Local_flame_and_flow_properties_of_propagating_premixed.pdf
    Done!
    ```

## 3. Find the items with problems and do your modification
- [ ] Click `Edit`->`Advanced Search`->`Paste the Citation keys to the input field`-> Click `Search` -> `Save Search`:  
![3](https://github.com/TimoLin/Zotero-ZotFileCleaner/assets/7792396/bf5e683d-8a52-4bc7-b590-393b2ae2912b) 
![4](https://github.com/TimoLin/Zotero-ZotFileCleaner/assets/7792396/abec1dcd-aa27-438b-a893-e67b80cb3a6c)

- [ ] The sub collection named `Untitled` will be shown under `My library`. Do you modifications and then the `Untitled` collection can be deleted.  
![5](https://github.com/TimoLin/Zotero-ZotFileCleaner/assets/7792396/6fec2a0e-cbd5-459a-9724-e7257665212a)

