# Qurro QIIME 2 "Moving Pictures" Tutorial

## Introduction

### What is Qurro?
Qurro visualizes the output from a tool like
[songbird](https://github.com/biocore/songbird) or
[DEICODE](https://github.com/biocore/DEICODE). It displays a plot of
__feature rankings__ (either the differentials produced by a tool like
songbird, or the loadings in a compositional biplot produced by a tool
like DEICODE) alongside a plot showing the __log ratios__ of
selected features' abundances within samples.

### Why is this useful?

Regardless of if we're looking at feature differentials or feature loadings,
what we care about when analyzing them are the log ratios between feature
abundances (or between groups of features' abundances), particularly as
compared to sample metadata categories. Both
[songbird's paper (Morton and Marotz et al. 2019)](https://www.nature.com/articles/s41467-019-10656-5) and
[DEICODE's paper (Martino et al. 2019)](https://msystems.asm.org/content/4/1/e00016-19) mention
analyzing the log ratios between features' abundances; Qurro provides an easy
way to do this.

Log ratio analyses are needed because data obtained from a microbiome study is
inherently compositional: we only have access to the relative abundances of
features in each sample, instead of their absolute abundances.
To quote [Gloor et al. 2017](https://www.frontiersin.org/articles/10.3389/fmicb.2017.02224):

> The starting point for any compositional analyses [_sic_] is a ratio transformation of the data. Ratio transformations capture the relationships between the features in the dataset and these ratios are the same whether the data are counts or proportions. Taking the logarithm of these ratios, thus log-ratios, makes the data symmetric and linearly related, and places the data in a log-ratio coordinate space (Pawlowsky-Glahn et al., 2015). Thus, we can obtain information about the log-ratio abundances of features relative to other features in the dataset, and this information is directly relatable to the environment.

### What is this tutorial going to cover?

In this tutorial, we'll visualize feature loadings produced by DEICODE for the
"Moving Pictures" dataset.
This tutorial picks up right where the
[DEICODE tutorial](https://library.qiime2.org/plugins/deicode/19/) leaves off
(and that tutorial, in turn, picks up where the [QIIME 2 Moving Pictures
tutorial](https://docs.qiime2.org/2019.4/tutorials/moving-pictures/) leaves
off).

## Installing Qurro

First off, activate your QIIME 2 environment. If you don't already have QIIME
2 installed, there are instructions for installing it
[here](https://docs.qiime2.org/2019.4/install/).

You can install Qurro using [pip](https://pip.pypa.io/en/stable/):

```
pip install numpy
pip install qurro
```

A python version of at least 3.5 is required to use Qurro.

Once you've installed Qurro, let's get QIIME 2 to recognize it. Run the
following command in a terminal:

```
qiime dev refresh-cache
```

To verify that Qurro was installed, you can run the following command:

```
qiime qurro --help
```

If this command succeeds, you should see information about Qurro's QIIME 2
plugin.

## Input files (what we'll need to run Qurro)

If you've completed the DEICODE tutorial already, you can follow along here
(using the output files you produced from DEICODE).
If you haven't completed the DEICODE tutorial already, you can download the
necessary files for this tutorial here:

- `table.qza` [view](https://view.qiime2.org/?src=https%3A%2F%2Fdocs.qiime2.org%2F2019.4%2Fdata%2Ftutorials%2Fmoving-pictures%2Ftable.qza) | [download](https://docs.qiime2.org/2019.4/data/tutorials/moving-pictures/table.qza)
- `sample-metadata.tsv` [download](https://data.qiime2.org/2019.4/tutorials/moving-pictures/sample_metadata.tsv)
- `taxonomy.qza` [view](https://view.qiime2.org/?src=https%3A%2F%2Fdocs.qiime2.org%2F2019.4%2Fdata%2Ftutorials%2Fmoving-pictures%2Ftaxonomy.qza) | [download](https://docs.qiime2.org/2019.4/data/tutorials/moving-pictures/taxonomy.qza)
- `ordination.qza` [view](https://view.qiime2.org/?src=http%3A%2F%2Fbiocore.github.io%2Fqurro%2Ftutorials%2Fmoving-pictures%2Fdata%2Fordination.qza) | [download](http://biocore.github.io/qurro/tutorials/moving-pictures/data/ordination.qza)
- `biplot.qzv` [view](https://view.qiime2.org/?src=http%3A%2F%2Fbiocore.github.io%2Fqurro%2Ftutorials%2Fmoving-pictures%2Fdata%2Fbiplot.qzv) | [download](http://biocore.github.io/qurro/tutorials/moving-pictures/data/biplot.qzv)

## Running Qurro

Since we'll be working with DEICODE output (i.e. a compositional biplot), we'll
need to use the `qiime qurro unsupervised-rank-plot` command. (The
`supervised-rank-plot` command is for working with differentials.)

```
qiime qurro unsupervised-rank-plot \
    --i-table table.qza \
    --i-ranks ordination.qza \
    --m-sample-metadata-file sample-metadata.tsv \
    --m-feature-metadata-file taxonomy.qza \
    --o-visualization qurro-plot.qzv
```

##### Output Artifacts

- `qurro-plot.qzv` [view](https://view.qiime2.org/?src=http%3A%2F%2Fbiocore.github.io%2Fqurro%2Ftutorials%2Fmoving-pictures%2Fdata%2Fqurro-plot.qzv) | [download](http://biocore.github.io/qurro/tutorials/moving-pictures/data/qurro-plot.qzv)

You just generated your first Qurro plot! `qurro-plot.qzv` is a `.qzv` file --
that is, a QIIME 2 visualization. You can view it either by running `qiime tools
view qurro-plot.qzv` or by uploading the file to
[view.qiime2.org](https://view.qiime2.org/). (You can also just click on the
"view" link right above to see a precomputed version of this visualization.)

## Interacting with a Qurro visualization

Let's view `qurro-plot.qzv`, as described above.

<img src="https://raw.githubusercontent.com/biocore/qurro/master/docs/tutorials/moving-pictures/screenshots/qurro1.png" alt="Qurro interface screenshot #1. No features are selected." />

So right away we see two things: on the left a plot of rankings (in this case,
loadings) for each feature, and on the right a plot of selected features' log
ratios in samples. In this tutorial these plots will be referred to as the
_rank plot_ and _sample plot_, respectively.

Since no features are currently selected to be part of a log ratio, these plots
look pretty empty. So let's select some features!

### Selecting features to construct log ratios

Recall that we'd like to analyze the log ratios between features' abundances.
In Qurro, "selecting features" lets us define a __log ratio__ between multiple
features' abundances in each sample.

There are a few ways of doing this in Qurro:

- One way is just by clicking on the rank plot twice. The first click sets
  the numerator feature for a log ratio, and the second click sets the
  denominator feature for the log ratio.
- You can also select features based on a text-search through their feature
  IDs or metadata. For example, it's possible to construct the log ratio of all
  features with taxonomy annotations containing the text `o__Fusobacteriales` over all
  features with taxonomy annotations containing the text `o__Pseudomonadales`.
    - This is equivalent to the log ratio of all ranked features in the order
      [_Fusobacteriales_](https://en.wikipedia.org/wiki/Fusobacteria) over all
      ranked features in the order
      [_Pseudomonadales_](observe://en.wikipedia.org/wiki/Pseudomonadales)).
    - In this case -- where an arbitrary of features can be in the numerator
      and denominator of the log ratio -- the log ratio is computed for a given
      sample by summing the feature abundances of the numerator features,
      summing the feature abundances of the denominator features, and then
      taking the log ratio of these sums (`log(top sum) - log(bottom sum)`,
      which is equivalent to `log(top sum / bottom sum)`).

Let's try the second of these options out. In the bottom-right corner of the
screen -- under the `Numerator` section -- change the feature metadata selector
(it's the dropdown that comes right after some text that says
"Filter to features where") to say `Taxon` instead of `Feature ID`. Now copy
the text `o__Fusobacteriales` into the text box in this section.

Repeat this process for the `Denominator` section, but now copy the text
`o__Pseudomonadales` instead. Press the "Regenerate plots" button. You should
see something like this:

<img src="https://raw.githubusercontent.com/biocore/qurro/master/docs/tutorials/moving-pictures/screenshots/qurro2.png" alt="Qurro interface screenshot #2. The log ratio of o__Fusobacteriales to o__Pseudomonadales is selected." />

Congrats! You just constructed a log ratio in Qurro. Both the rank plot and
the sample plot should be updated now:

- The rank plot should now have some bars colored red and some bars colored
  blue. The red bars indicate the numerator features that were just selected
  (i.e. all features with taxonomy annotations containing the text
  `o__Fusobacteriales`), and the blue bar indicates the denominator features
  that were just selected (i.e. all features with taxonomy annotations
   containing the text `o__Pseudomonadales`).

- The sample plot should now look like a scatterplot containing at least a few
  points. The y-axis value of each of these points is set to the log ratio of
  the selected features' abundances; the x-axis values and colors are set to
  whatever metadata categories you'd like to use.

#### A caveat with basic text searching

This is great, but there's one thing to watch out for. Since Qurro only checks
that a given feature's taxonomy annotation _contains the text_ `o__Fusobacteriales`,
there's the potential for it to find other features that happen to contain the
text `o__Fusobacteriales` in their taxonomy annotations but aren't actually in the order
`o__Fusobacteriales`.

Say a new order is discovered and named _Fusobacteriales2_. (This will almost
certainly never happen, but you never know.) Since we only care about a
feature's taxonomy annotation *containing* the text `o__Fusobacteriales`, features that
were classified as being in `o__Fusobacteriales2` would also get included in
our searches!

In practice, we can account for this by changing the __search type__ (currently
set to `contains the exact text`) options in Qurro. The
`contains the exact separated text fragment(s)` setting will split up each
feature's ID or metadata field at every occurrence of whitespace, commas, or
semicolons, and then only search against perfect matches of each of those
"fragments". This would protect us against our hypothetical
`o__Fusobacteriales2` scenario.

(In practice this sort of problem is observable when, for example, the features
being investigated include Viruses in addition to Bacteria: there are plenty of
_Staphylococcus_ species and plenty of _Staphylococcus_ phages, and a basic
text search for just `Staphylococcus` will give you both.)

### Changing up the sample plot

The sample plot's "x-axis" and "color" fields are initially set to an
arbitrary sample metadata field (in this case, `BarcodeSequence`). This isn't
super useful, so we can change it to a more interesting metadata field.

Let's try setting the x-axis to the `Body Site` field and the color to the
`ReportedAntibioticUsage` field. You can do this using the controls underneath
the sample plot, on the middle-right side of the Qurro interface.

<img src="https://raw.githubusercontent.com/biocore/qurro/master/docs/tutorials/moving-pictures/screenshots/qurro3.png" alt="Qurro interface screenshot #3. The same log ratio as before is selected, and the x-axis of the sample plot is set to BodySite (with 'left palm' and 'right palm' as values) and the color of each point is set to ReportedAntibioticUsage (mostly 'No', with one 'Yes' value)." />

This is more interesting. Of course, there aren't a lot of samples in the plot,
and this was a pretty arbitrary log ratio we just selected. So it's hard to
draw any meaningful conclusions from this.

Actually, let's examine that first problem in more depth: _where are all of the
missing samples in the sample plot_?

### Missing samples

Notice the text underneath the sample plot controls? If you've been following
along with the tutorial so far, it should say that only
`15 / 34 samples (44.12%)` are shown in the sample plot. What gives?

As the text underneath this explains, it's because the other samples have
invalid log ratios. These other samples either didn't have any
`o__Fusobacteriales` bacteria observed, didn't have any `o__Pseudomonadales`
bacteria observed, or didn't have either of these bacteria.

Zeroes in either the top or bottom of a log ratio mess things up. The logarithm
of 0 / x (i.e the logarithm of 0) is undefined, as is the logarithm of x / 0
(since you straight-up can't divide by 0).

## Combining Qurro and Emperor

If you followed the DEICODE tutorial, you might remember seeing a biplot.
(`biplot.qzv`). Here, we'll use this biplot as a way to select features in Qurro.

### Selecting features directly from a biplot

First, open up the biplot in a new browser tab or window. As with the Qurro plot,
you can do this using `qiime tools view` or by uploading `biplot.qzv` to
[view.qiime2.org](https://view.qiime2.org/).

<img src="https://raw.githubusercontent.com/biocore/qurro/master/docs/tutorials/moving-pictures/screenshots/biplot.png" alt="Screenshot of the biplot generated in the DEICODE tutorial, visualized in Emperor." />

Try double-clicking on an arrow in this biplot. You should see a message pop up
in the bottom left of your screen that says `(copied to clipboard)`, followed
by a long sequence of characters. This indicates that you just copied the
__Feature ID__ of this feature to your clipboard.

Move back to the tab or window where you have the Qurro plot open.
You can paste (using something like ctrl-V or &#8984;-V) the feature ID you just copied
directly into the numerator or denominator search box, in the bottom right corner of Qurro's interface. You can do this twice
(once for the numerator and once for the denominator) to create log ratios of
features directly from the biplot.

Now press the `Regenerate plots` button to apply this log ratio to the rank and
sample plots.

#### Hey, wait a second! There are only eight arrows in the biplot, but there are over five hundred features in the feature ranks plot. What gives?

This is just a result of how the biplot visualization was created in the DEICODE
tutorial. In the `qiime emperor biplot` command, the `--p-number-of-features`
parameter was set to 8, so only 8 arrows (i.e. features) are shown in the
Emperor visualization of the biplot. Feel free to try rerunning this command
with a different number of features to show more features in the biplot.

## Epilogue: How do I actually, like, select features in Qurro?

That's a good question! You have a few strategies in choosing what to inspect
in a Qurro visualization. There isn't a clear "best practice," at least as of
writing.

One strategy (as mentioned in the
[songbird FAQ](https://github.com/biocore/songbird#faqs), regarding
differentials) is to "...investigate the top/bottom microbes [features] with
the highest/lowest ranks."

You can also try picking out features that appear to be strongly associated
with clustering of your samples in a compositional biplot, as we did with
Emperor above.

Other work has been done on this; see, for example,
[Rivera-Pinto et al. 2018](https://msystems.asm.org/content/3/4/e00053-18.abstract).

## Acknowledgements

This tutorial was based on the [DEICODE](https://library.qiime2.org/plugins/deicode/19/) and [QIIME 2](https://docs.qiime2.org/2019.4/tutorials/moving-pictures/) moving pictures tutorials.