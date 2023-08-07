ZotFileCleaner
==============
An utility to find pdf files that are locally stored in Zotero database instead of ZotFile custom locations.

## 0. Prerequisite
This utility relies on the `ZotFile` and `Better Bibtex` plugins. If you use them too, you may face the same problem as me. 

Environment: `Python3` and [`bibtexparser`](https://github.com/sciunto-org/python-bibtexparser)

```sh
pip install --no-cache-dir --force-reinstall git+https://github.com/sciunto-org/python-bibtexparser@main
```

##  1. Preparation in Zotero
- [] Remember the `Custom Location` setting in the `ZotFile Preferences`:

- [] In Zotero, click (1)`File`->(2)`Export Library`->(3)`Select Better BibTex`->(3)Check `Keep updated` option->(4)Save the bib file to any folder your like.

## 2. Run the script

```sh
$ python3 ~/github/Zotero/src/zotfileCleaner.py -h
usage: zotfileCleaner.py [-h] -f FILE -c CUSTOMLOCATION [-e]

ZotFileCleaner: An utility to find pdf files that are locally stored in Zotero
database instead of ZotFile custom locations.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Zotero automatic exported better bibtex lib file.
  -c CUSTOMLOCATION, --customlocation CUSTOMLOCATION
                        Custom location defined in ZotFile preferences.
  -e, --empty           Print items without any attachment files
```
For example:  
```
$ python3 ~/github/Zotero/src/zotfileCleaner.py -f "~/Documents/Zotero/mylib.bib" -c "/Dropbox/Zotero" -e

Citation keys of the files in Zotero database:
  ahnHeatReleaseRate2022
  aignerSwirlCounterswirlEffects1988
  aignerSwirlCounterswirlEffects1988a
  alessandroStudyTurbulentSpray2019
  andreiniLocalSourceBased2013
  ansysinc.ANSYSFluentTheory
  araiBreakupLengthSpray1985
  barlowEffectsTurbulenceSpecies1998
  bhatiaUnderstandingLiquidJet2022
----------------------------------------------
Citation keys of items without attachment files:
  brzustowskiCombustionTheory1987
  caowenyuCaiYongflameletMoXingFenXiXuanLiuBeiRanShaoShiJinPinYouXiHuoDian2014
  carvalhoLiquidFilmDisintegration2002
  chiEfficientPremixedTurbulent2022
  chuDirectNumericalSimulation2016
  chungBLASTNeTCallCommunityinvolved2022
  ciolkoszKIAIProjectFinal1999
```

## 3. Find the items with problems and do your modification
Click `Edit`->`Advanced Search`->`Paste the Citation keys to the input field`-> Click `Search` -> `Save Search`:  

The sub collection named `Untitled` will be shown under `My library`. Do you modifications and then the `Untitled` collection can be deleted.

