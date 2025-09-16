import streamlit as st
import ollama
import chromadb

# docs
RAW_DOCS = """
Significance Both plant biodiversity and soil fertility are in decline.
We find that restoration of plant biodiversity on a nutrient-poor, unfertilized soil led to greater increases in soil fertility than occurred when these same plant species grew in monocultures.
The plant species in this biodiversity experiment fell along a trade-off surface in their nutrient content traits, precluding any one species, or any one type of species, from markedly increasing soil fertility.
Our results have implications for degraded agroecosystems, suggesting that increasing plant functional biodiversity may help restore their soil fertility.
Creative applications of our findings to pastures, cover crops, and intercropping systems may provide greenhouse gas benefits from soil carbon storage and reduce the amounts of fertilizers needed for optimal yields.
Abstract Fertile soils have been an essential resource for humanity for 10,000 y, but the ecological mechanisms involved in the creation and restoration of fertile soils, and especially the role of plant diversity, are poorly understood.
Here we use results of a long-term, unfertilized plant biodiversity experiment to determine whether biodiversity, especially plant functional biodiversity, impacted the regeneration of fertility on a degraded sandy soil.
After 23 y, plots containing 16 perennial grassland plant species had, relative to monocultures of these same species, ∼30 to 90% greater increases in soil nitrogen, potassium, calcium, magnesium, cation exchange capacity, and carbon and had ∼150 to 370% greater amounts of N, K, Ca, and Mg in plant biomass.
Our results suggest that biodiversity, likely in combination with the increased plant productivity caused by higher biodiversity, led to greater soil fertility.
Moreover, plots with high plant functional diversity, those containing grasses, legumes, and forbs, accumulated significantly greater N, K, Ca, and Mg in the total nutrient pool (plant biomass and soil) than did plots containing just one of these three functional groups.
Plant species in these functional groups had trade-offs between their tissue N content, tissue K content, and root mass, suggesting why species from all three functional groups were essential for regenerating soil fertility.
Our findings suggest that efforts to regenerate soil C stores and soil fertility may be aided by creative uses of plant diversity.
Sign up for PNAS alerts.
Get alerts for new articles, or get an alert when an article is cited.
For a soil to be fertile, it must supply sufficient amounts of the multiple nutrients that may limit plant growth, such as nitrogen (N), phosphorus (P), potassium (K), calcium (Ca), and magnesium (Mg), and have sufficient organic matter to retain water and nutrients (1, 2).
Low levels of one or more of these factors would reduce plant productivity.
In natural ecosystems, plants contribute to the creation of fertile soils through the fixation of carbon (C) and N, through root chemical liberation of unavailable forms of soil minerals and their movement from deep to surface soils, and through the uptake and retention of nutrients (3–12).
However, if plant species differ in their capacity to liberate, capture, or retain particular limiting soil nutrients (5), then any one species growing alone might lead to the creation of a soil relatively deficient in those nutrients that it has difficulty obtaining.
If plants species have trade-offs between their abilities to acquire different nutrients, with each species being better at acquiring some nutrients but poorer for others (13), then a diversity of plant species may be essential for the long-term accrual of the multiple elements that are required for a soil to be fertile.
Here we use a long-term grassland biodiversity field experiment to explore the potential role that different perennial grassland plant species, plant traits, and plant biodiversity may play in generating and restoring soil fertility.
While greater plant biodiversity is associated with greater primary productivity and soil C accumulation (14–17), increased soil C alone does not make a soil more fertile.
Greater fertility also requires increases in all potentially limiting nutrients such as N, P, K, Ca, and Mg, as well as optimal soil pH and adequate soil cation exchange capacity (CEC) (1, 2).
Here we test the hypothesis “that the sustainability of soil nutrient cycles and thus of soil fertility depends on biodiversity” (18).
Because greater plant species richness has been associated with greater uptake of available soil nutrients and greater plant biomass production (18), higher plant biodiversity might increase soil fertility if the increased nutrients in plant biomass are returned to the soil as plant tissue decomposes (3, 4, 6, 7, 12, 19–21) and if greater plant diversity leads to lower leaching losses of these nutrients (22).
This increase in soil fertility could then increase biomass production, creating a positive feedback as even more nutrients were added to the soil from greater biomass inputs (7, 19, 23).
In particular, as roots, leaves, and other plant parts are shed, soil bacteria, fungi, and invertebrates modify and stabilize these organic matter inputs and release nutrients as they decompose plant tissue (9, 10, 21, 24–29).
Nutrients released by decomposition can increase plant growth and thus the amount of plant biomass that subsequently gets returned to the soil (7).
On a nutrient-poor soil, greater plant diversity may lead to greater accumulation of soil nutrients and organic matter and therefore may cause plant productivity to increase more through time than in low-diversity ecosystems (21, 30, 31).
Our experiment, planted in the spring of 1994, manipulated the composition and diversity of perennial grassland plant species growing on a sandy, degraded soil.
In August 1993, the upper 6 cm to 8 cm of topsoil was removed from an abandoned agricultural field to eliminate a weedy soil seed bank.
The field was then plowed and disked multiple times, and had bare soil from August 1993 until planted in spring 1994.
The one hundred fifty-four 9 × 9 m plots established for this experiment were seeded to have 1, 2, 4, 8, or 16 perennial grassland species randomly chosen from a pool of 18 species.
Here, “plant diversity” refers to the number of species planted in a plot.
We additionally calculated plant “functional group diversity” based on a functional grouping commonly applied to grasslands, classifying plant species as grasses, legumes, or forbs (32).
Plots were never fertilized, were annually burned in early spring before green-up, and were fenced to exclude large vertebrate herbivores.
The glacial outwash sandplain soils of our site in east-central Minnesota are agronomically classified as “very low” in organic matter, N, and K, but “very high” in P (SI Appendix, Table S1).
Using archived soil samples collected from each plot before planting in 1994 and samples collected after 23 y of growth in 2017, we measured soil total N and C, exchangeable K, Ca, and Mg, soil CEC, soil pH, and extractable Bray P in the upper 0 cm to 20 cm of the soil profile.
In August 2017, both aboveground and belowground (root; 0- to 30-cm depth) plant biomass were measured, as were N, P, K, Ca, and Mg in both aboveground and root biomass.
We additionally measured aboveground plant tissue chemistry for each individual plant species.
Results Higher levels of plant diversity led to increases in numerous factors that contribute to soil fertility.
Comparison of pretreatment 1994 soils to 2017 soils shows that plots with higher plant diversity had significantly greater increases in soil N, K, Ca, Mg, and C, in CEC and in soil pH (Fig.
1 and SI Appendix, Figs.
S1 and S2 and Table S2).
Soil P levels, which were very high before planting, remained very high in 2017, with no detectable effect of plant diversity (Fig.
1H and SI Appendix, Table S2).
Although no plots were ever fertilized, by 2017, the soils of the 16-species treatment had 29% more total soil N (0- to 20-cm depth) than the monoculture mean of these same species, 95% more soil K, 30% more soil Ca, 29% more soil Mg, 35% more total soil C, 34% greater CEC, and a less acidic soil (0.2 pH increase from monocultures) (Fig.
Although soil bulk density declined with plant diversity from a mean ± SE of 1.46 g⋅cm−3 ± 0.015 in the monocultures to 1.37 g⋅cm−3 ± 0.018 in 16 species plots (F1,85 = 23, R2 = 0.21, P < 0.001), expressing soil elemental levels on a concentration basis and on an area density basis were qualitatively similar (SI Appendix, Figs.
S3–S5 and Table S3).
Soil chemistry vs.
plant diversity.
Mean ±1 SE of soil chemistry (0- to 20-cm depth) before planting in 1994 in green (diamond) and in 2017 in orange (circle) of (A) total carbon, (B) total nitrogen, (C) exchangeable potassium, (D) exchangeable calcium, (E) exchangeable magnesium, (F) CEC, (G) soil pH, and (H) extractable Bray phosphorus versus number of planted species (1, 2, 4, 8, or 16; log scale).
Lines are linear regressions ± 1 SE (n = 154 plots).
The quantity (grams per square meter) for C, N, P, K, Ca, and Mg were calculated using soil bulk density.
Sample sizes for each diversity level (1 to 16 species) are 1 species = 32 plots; 2 = 28; 4 = 29; 8 = 30; and 16 = 35.
The greater accumulation of N, K, Ca, and Mg in surface soils (0- to 20-cm depth) at higher plant diversity was accompanied by even greater percent increases relative to monocultures in the pool size of these nutrients in both aboveground and belowground plant biomass in 2017 (Fig.
Linear regressions show that tissue pools of N, K, Ca, and Mg in aboveground and in belowground biomass were, relative to average levels across all monocultures, positively dependent on the log of plant diversity (all P < 0.001; Fig.
2 and SI Appendix, Figs.
S6 and S7 and Table S4).
Nutrient contents relative to monoculture levels.
The 2017 relative shoot (blue; circle) and root (red; diamond) nutrient content of biomass for each diversity treatment is expressed as the percent of the 2017 mean nutrient content of all monocultures combined (mean ± 1 SE).
Percent change relative to the mean of all monocultures for (A) nitrogen, (B) potassium, (C) calcium, and (D) magnesium contained in aboveground shoot biomass and belowground (0 cm to 30 cm) root biomass.
Lines are linear regressions ± 1 SE (n = 154 plots).
Shoots are dried aboveground biomass, and roots are dried belowground biomass (0 cm to 30 cm).
Biomass was multiplied by the concentration of each element.
Why, though, might the production of greater plant biomass and the accumulation of soil nutrients depend on plant diversity?
Diversity is thought to impact ecosystem processes because of functional differences between species (32).
Because the herbaceous perennial species of tallgrass prairie are often functionally classified as grasses (Poaceae), legumes (Fabaceae), and forbs (not including legumes; Asteraceae, Lamiaceae, and Apocynaceae), we tested whether the rate of ecosystem accumulation of particular nutrients was related to the presence of these plant functional groups.
To do this, we classified each plot by its presence of grass (G), legume (L), or forb (F) species.
This gave seven functional group compositions: G, L, F, G+F, L+F, G+L, and G+L+F.
Ecosystem pools of accumulated N, K, Ca, and Mg (Fig.
3) were calculated as the change in each plot of each element in the soil from 1994 to 2017 (as grams per square meter of each element in the 0- to 20-cm soil depth increment) plus the total amount of each element accumulated in shoots and roots by 2017 (as grams per square meter), since all plant biomass had been removed the year before planting.
Change in ecosystem total nutrient pools (black points) for each functional group composition for (A) nitrogen, (B) potassium, (C) calcium, and (D) magnesium.
Each black point shows the mean of the total ecosystem pool ± 1 SE.
Pools were defined as the change from 1994 to 2017 in soil levels of a nutrient (0- to 20-cm-depth increment) plus amounts of that nutrient in aboveground biomass and in roots (0 cm to 30 cm) in 2017; sum expressed as grams of nutrient per square meter.
Bars show the value for each nutrient in aboveground biomass (gray), in belowground biomass (yellow), and in soil (blue).
Bars with negative values, shown below the zero line, indicate a reduction from 1994 to 2017 for an element.
Functional group compositions: G = grasses only, n = 22; F = nonlegume forb only, n = 10; L = legumes only, n = 11; FL = at least one forb and one legume, n = 5; GL = at least one grass and one legume, n = 23; GF = at least one grass and one forb, n = 14; GFL = at least one grass, one legume, and one forb, n = 69.
Letters indicate whether means for a particular nutrient differ (P < 0.05) following a Tukey correction.
The presence of all three functional groups, the G+F+L plots, was associated with the largest increases in ecosystem pools of N, K, Ca, and Mg compared to when just a single functional group was present (Fig.
In particular, plots containing all three functional groups (G+L+F) had significantly greater accumulation in soils plus plant biomass of each of the four nutrients, N, K, Ca, and Mg, than did the plots with just a single functional group (the F, G, or L plots; Fig.
3 and SI Appendix, Table S5).
This was not the case for any combination of just two functional groups (Fig.
Neither the G+F nor the F+L plots accumulated significantly greater ecosystem pools of N, K, Ca, or Mg than did the G, F, or L plots (Fig.
Results were intermediate for the G+L plots, which were not significantly different from F or L in Mg accumulation or from L in Ca accumulation, but had greater N accumulation than plots planted with a single functional group or with G+F.
Finally, although G+F+L and G+L did not differ in ecosystem pools of N, Ca, or Mg, G+F+L had significantly greater K pools than all other functional compositions except F+L, suggesting that the presence of forbs was an important cause of the observed large increases in K at high plant biodiversity.
In total, plots planted with a single functional group accumulated significantly lower ecosystem pools of most nutrients than did G+F+L plots, and those planted with two functional groups only significantly exceeded single functional groups in one-fourth of the pairwise comparisons (Fig.
Separate analyses for each of the plant, root, and soil nutrient pools demonstrates that, when compared to plots planted with a single functional group, G+F+L produced more aboveground and belowground biomass and accumulated more C, N, K, Ca, and Mg in 87% of the comparisons (39 out of 45 comparisons) (SI Appendix, Fig.
On an even finer scale, for amounts of each of the four nutrients in aboveground biomass, G+F+L was significantly greater than G+L, but was never significantly greater than F+L (SI Appendix, Fig.
For root nutrients, G+F+L was significantly higher in root K than both F+L and G+L.
The only functional group with root K levels as high as those of G+F+L was F, the forb-only plots.
For root Mg, F+L did not differ from G+F+L, but G+F+L had significantly more Mg than G+L.
For root Ca, the opposite occurred: G+F+L did not differ from G+L but had significantly more Ca than F+L.
In total, these results suggest that forbs, and the joint presence of forbs and legumes, are important contributors of K and Mg to ecosystem pools and that legumes and the joint presence of legumes and grasses are more important contributors of N and Ca. Since not all of these nutrients may be limiting to the production of plant biomass, we determined which soil variables were more strongly correlated with observed diversity-dependent changes in productivity while accounting for the effect of plant diversity.
We used linear multiple regressions and multimodel inference, finding that total plant biomass depended positively on the loge of the number of species (156 ± 25.6 g⋅m−2 biomass per 1 loge(number of plant species), P < 0.001), soil exchangeable K (51.3 ± 8.8 g⋅m−2 biomass per g⋅m−2 of K, P < 0.001), total soil N (2.88 ± 0.67 g⋅m−2 biomass per g⋅m−2 of N, P < 0.001), and total soil C (0.23 ± 0.05 g⋅m−2 biomass per g⋅m−2 of C, P < 0.001) (SI Appendix, Table S6).
This analysis suggests that total soil C, total soil N, and exchangeable soil K are the soil variables most strongly associated with the amount of plant biomass produced in this field experiment, which is consistent with our soil analyses that indicated agronomically low soil levels of N, K, and organic matter at the start of our experiment (SI Appendix, Table S1).
Finally, we determined how the plant species in the three functional groups might differ in traits relevant to the accumulation of soil K, N, and C.
For K and N, we used average measured aboveground tissue concentrations of K and N for each species in monoculture and 16-species plots.
For soil C accumulation, we used average monoculture root mass for each species because prior results of this experiment showed that greater root biomass (as gram per square meter) was the variable most strongly associated with greater increases in soil C (14, 17).
These three measured traits of the species (root mass, tissue %N, tissue %K) defined a regression plane (Fig.
4 and SI Appendix) (F2,12 = 6.3, R2 = 0.51, P = 0.014).
The species within each functional group tended to be similar to each other, as evident by their tendency to cluster (Fig.
On this trade-off surface, perennial C4 grasses were low in both tissue %N and %K but had the highest root biomass.
Forbs and legumes, which had less root biomass than C4 grasses, were further differentiated: Legumes had higher %N but markedly lower %K.
Forbs, in contrast, had higher %K but lower %N (Fig.
Forbs and legumes had similar %Ca and %Mg levels, and their levels were greater than for grasses (SI Appendix, Fig.
Empirical trade-off surface among plant traits for the 15 herbaceous perennial plant species that persisted in the experiment.
A regression plane (F2,12 = 6.3, R2 = 0.51, P = 0.014) is fitted to species-specific measured values of percent aboveground tissue potassium (K) (x axis), percent aboveground tissue nitrogen (N) (y axis), and mean monoculture root biomass (grams per square meter; 0- to 30-cm depth; z axis).
Each point represents the three measured traits of each of 15 species (SI Appendix, Table S7) classified as grasses (C4 grasses in dark green and C3 grasses in light green), forbs (purple), and legumes (orange).
The %N and %K represent the mean across each species' monocultures and the biomass of each species in five 16-species plots.
Root biomass represents the mean root mass (0- to 30-cm depth) of each species' monocultures.
Removing the two C3 grasses (lighter green; below the plane), which are subdominant species in this ecosystem and grew poorly in monoculture, increased the fit of the plane to F2,10 = 15, R2 = 0.75, P = 0.001 (not shown).
The point for Andropogon gerardii (C4 grass) was slightly jittered in the x and y axis to avoid overplotting with Sorghastrum nutans (C4 grass).
Discussion Early in this experiment, greater plant diversity was associated with greater capture of soil nitrate (18) and with 16 species plots being ∼100% more productive than the average of these species in monocultures.
After 23 y, we find that greater plant diversity was associated with higher levels of soil C, N, K, Ca, and Mg and with 16 species plots being ∼200% more productive than monocultures.
The progressively greater primary productivity observed through time at higher diversity in this and other long-term biodiversity experiments (refs.
30 and 31, but see ref.
33) and the greater accumulation of multiple nutrients and C in soil and in plant biomass (Figs.
1 and 2) suggest the existence of a positive feedback effect (7, 23) of plant diversity on soil fertility that increased primary productivity through time.
We hypothesize that high plant diversity, and especially the joint presence of grass, legume, and forb species, leads to greater liberation and capture of limiting soil nutrients (18).
This, in turn, allows greater production of plant biomass.
We suggest that the nutrient and C contents of the greater biomass (roots and shoots) produced by diverse mixtures of grass, legume, and forb species is then recycled when it senesces, helping create a more fertile soil.
This more fertile soil would then further increase plant biomass production and biomass nutrient pools, in a positive feedback loop that would persist until an equilibrium is reached (7, 19, 20).
We note, however, that the annual early spring burning in our experiment likely volatilizes some of the C and N that had been in litter from senesced aboveground biomass, but also likely deposits biologically available forms of other elements in ash (e.g., Ca, Mg, and K).
Because root mass in our prairie-like high-diversity plots is about 4 times the aboveground biomass, senesced biomass from root turnover may add C, N, and other nutrients to soil (6–8, 10, 11, 19, 34).
The three-way trade-off shown in Fig.
4 suggests why plant functional diversity may have been essential for increasing soil fertility in our experiment, which was unfertilized.
It suggests that no single species and no functional group could, by itself, span the full space of the root biomass–N–K trade-off surface and thus cause soil C, N, and K, which seem to limit productivity, to all increase.
Increases in all three of these were associated with greater productivity in our experiment, and thus with the hypothesized feedback effect of greater productivity and its nutrient contents on soil fertility.
In contrast, increased N, P, and K fertilization is often required to increase the productivity of an agricultural monoculture crop, and such fertilization can also lead to increased soil C (35).
Our monocultures, however, were never as productive as our high-diversity plots (17).
At our site, soil P was at agronomically very high levels both prior to planting and 23 y later.
While root biomass, N, and K differed among functional groups, and while soil C, soil N, and soil K increased with diversity, we found that soil P was not significantly dependent on plant diversity or functional groups, and tissue P levels did not differ among functional groups when growing on this P-rich soil (Fig.
1H and SI Appendix, Figs.
The trait differences (Fig.
4) between grasses, legumes, and forbs suggest a mechanistic link from plant traits to the effect of functional diversity on primary productivity and the accumulation of soil nutrients.
The trade-off surface shows that each functional group should contribute to the soil more of one of root biomass, N, or K, but less of the other two.
Because legumes were high in %N and %Ca while forbs were high in %K, %Ca, and %Mg, the presence of each of these functional groups should have particularly enriched soil for those elements that were in higher relative concentration in its biomass (Fig.
3 and SI Appendix, Figs.
The high root biomass of C4 grasses may have decreased nutrient losses via leaching and helped increase soil organic C (14, 17, 18, 22).
Moreover, no functional group growing alone increased soil C and nutrients as much as occurred when all three groups were present (Fig.
3 and SI Appendix, Fig.
The increases in surface soil exchangeable K, Ca, and Mg may have come from root uptake of these elements in deeper soils that was concentrated at the surface as aboveground tissues and shallow roots died and decomposed or as elements were deposited as ash from litter during early spring burns (6).
Ca, for example, tends to move unidirectionally from roots to shoots, with limited resorption when tissues senesce (34, 36).
If greater root uptake and recycling of nutrients from ash or root turnover is the mechanism for the accumulation of soil fertility in high-diversity plots, then one would expect a coupling of the accumulation of plant and soil pools (37).
For example, soil K was highly dependent on plant diversity (R2 = 0.47), and K was the nutrient with the largest % increase (370%) in its aboveground plant pool when comparing 16-species plots to the mean of all monocultures (Fig.
For K, Ca, and Mg, 16 species plots had ∼150 to 370% greater aboveground pools and ∼90 to 150% greater root pools than monocultures, indicating that higher plant diversity led to greater ecosystem capture and retention in biomass of these cations (Fig.
Moreover, in these sandy soils, increases in soil organic C were correlated with increases in CEC (1994: R2 = 0.20, P < 0.001; 2017: R2 = 0.52, P < 0.001; SI Appendix, Fig.
S11), which should increase K, Ca, and Mg retention in these soils.
Our long-term experiment revealed surprisingly large diversity-dependent increases in soil fertility.
This magnitude, however, might depend on our initial soil characteristics.
The soils of our site, which formed on a glacially deposited sand plain, are classified taxonomically as entisols, which have limited horizon development (38).
At the beginning of this experiment, some of the topsoil and its organic matter were removed, and soils were plowed and disked, which tended to homogenize the remaining topsoil with deeper soil layers.
The low initial levels of soil C and N and high levels of P in our starting soils are characteristic of geologically young soils undergoing progressive development (39).
Thus, if degraded and abandoned agricultural soils at our site accumulate C and nutrients in a logistic manner (40), the rates of increase in soil C, N, K, Ca, and Mg that we observed at high plant diversity may be greater than if our soil had initially been higher in these elements.
Our results, and their likely mechanistic basis, may provide insights into methods to restore soil C and increase limiting soil macronutrients in agroecosystems and managed forests.
For instance, incorporating greater plant functional diversity via appropriate choice of the plant species used in crop rotations, intercropping, or cover crops may lead to long-term increases in soil fertility and subsequent reductions in the amount of fertilizer needed (41–44).
Because our results suggest it is not simply the number of plant species that matters, but rather the appropriate suite of complementary plant traits, it would be interesting to determine whether as few as perhaps three such plant species might offer notable soil benefits relative to monocultures.
In our study, the increased inputs of senesced plant biomass that occurred at higher diversity had to be transformed and mineralized by the soil microbial and invertebrate communities, suggesting that soil microbial biodiversity may also help explain the results in Fig.
1 (45, 46), which is an intriguing possibility (9, 16, 25, 27, 28).
Greater accumulation of plant or soil pathogens in monocultures, or increases in soil mutualists, or decreases in soil pathogens at high plant diversity are other possible ways that microbial biodiversity might impact ecosystem functioning through time (25, 47).
In total, our results show that plant diversity, including plant functional diversity, can play a significant role in the generation of soil fertility, likely via positive feedback effects of diversity-dependent increases in nutrient capture and productivity on soil fertility.
Our results raise the interesting possibility that the high plant diversity of most natural ecosystems may have been an important factor leading to the creation of fertile soils around the world.
Efforts to increase soil C stores and fertility of degraded soils may be aided by creative uses of plant diversity.
Methods Experimental Design.
The experimental field had been abandoned from agriculture for more than 15 y when, in August of 1993, the herbicide glyphosate was applied and surface vegetation, once dead and dried, was burned.
The top 6 cm to 8 cm of soil was scraped off to reduce the presence of weedy annual plant seeds in the soil seed bank.
This also reduced soil carbon and soil nutrient levels.
The site was then plowed twice and harrowed multiple times that year, and again in May 1994 before planting.
The 168 plots, initially 13 m by 13 m but subsequently reduced to the central 9 m by 9 m portion, were planted with 1, 2, 4, 8, or 16 perennial plant species randomly chosen from a species pool of 18.
The species pool consisted of common perennial grassland species of regional tallgrass prairie and two oaks common in nearby oak savannas.
Herbaceous species were functionally categorized as C4 grasses, C3 grasses, legumes, and nonleguminous forbs, with four species in each functional group.
Because of poor establishment, 14 plots were dropped from the experiment, leaving 154 plots.
In particular, the two oak species failed to survive because of annual burning.
Two of the four C3 grasses, Agropyron smithii and Elymus canadensis, initially germinated but failed to survive long term.
The final experimental design thus consisted of 154 plots seeded with 1, 2, 4, 8, or 16 randomly selected perennial grassland species, and with 32, 28, 29, 30, and 35 replicates of each diversity level, respectively.
Monocultures were not, by design, replicated; rather, the monoculture treatment was based on random draws of single species from the species pool.
Most species were randomly assigned to two monocultures.
However, Poa pratensis and Panicum virgatum have one monoculture; Liatris aspera, Lespedeza capitata, Dalea purpureum, and Schizachyrium scoparium have three monocultures; and Sorghastrum nutans has four.
In addition, one forb species, Solidago rigida, failed to germinate during the first year and was planted with another forb, Monarda fistulosa, in spring 1995.
In the third year, S.
rigida germinated and eventually became well established and dominated its monocultures.
Plots were annually burned early each spring before green-up but received no fertilizer.
Each plot was annually weeded by hand to remove nonplanted species.
The experiment was fenced to exclude white-tailed deer.
Additional details can be found on the Long-Term Ecological Research (LTER) program website for the Cedar Creek Ecosystem Science Reserve under experiment name “e120: Biodiversity II: Effects of Plant Biodiversity on Population and Ecosystem Processes” (https://www.cedarcreek.umn.edu/research/experiments/e120).
Calculation of Plant Functional Groups.
For each plot in the experiment, we determined if it had been planted with grasses (“G,” Poaceae), legumes (“L,” Fabaceae) or forbs (“F,” Asteraceae, Lamiaceae, and Apocynaceae).
We then categorized each plot by the functional groups planted in it.
This grouping gave seven functional group compositions: G, L, F, G+F, L+F, G+L, and G+L+F.
Sample sizes were as follows: G = grasses only, n = 22 plots; F = forb only, n = 10; L = legumes only, n = 11; FL = at least one forb and one legume, n = 5; GL = at least one grass and one legume, n = 23; GF = at least one grass and one forb, n = 14; GFL = at least one grass, one legume, and one forb, n = 69.
Field Collection of Soil Samples.
Nine soil cores per plot were collected in an evenly spaced 3 × 3 sampling grid pattern in September of 2017 to a depth of 60 cm in 20-cm increments using a 1.9-cm-diameter soil corer.
The nine cores from a plot were then combined, dried at 60 °C, sieved to a 2-mm fraction, and then well mixed.
Soil samples were similarly taken and processed in 1994 prior to planting.
Those samples remained in glass archived vials until analysis.
The 2017 soil samples were similarly archived.
Plant Biomass Sampling.
In August, near the time of peak aboveground biomass, two parallel 0.10-m by 6-m strips were clipped at the soil surface in each plot each year to sample plant biomass.
Strips were located in the middle half of each plot, separated by about 1 m to 2 m, and located so as to not clip an area that had previously been clipped within the past decade.
One strip per plot was sorted to species; the other was unsorted.
Root biomass was subsequently sampled in the clipped area, with a 5.1-cm-diameter soil probe used to collect three cores per strip (six per plot) to a depth of 30 cm.
Roots were washed over a mesh screen to remove soil.
Roots and aboveground biomass were dried in a dehumidified drying room at 60 °C until achieving constant mass.
Aboveground biomass was sampled annually starting in 1996.
Belowground biomass has been sampled in years 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2010, 2015, and 2017.
Laboratory Analysis of Soil Samples.
The University of Minnesota Research Analytical Laboratory analyzed soil samples that we collected from depth increments of 0 cm to 20 cm, 20 cm to 40 cm, and 40 cm to 60 cm in 2017 and 0 cm to 20 cm in 1994 for exchangeable cations (calcium, magnesium, potassium, sodium) using a pH 7 ammonium acetate extraction and for aluminum using a 1 M KCl extraction followed by analysis using an Inductively Coupled Argon Plasma Optical Emission Spectrometer (iCap 7600 Duo ICP-OES Analyzer, Thermo Fisher Scientific) (48).
Effective CEC was measured by the summation method of exchangeable Ca, Mg, K, Na, and Al (48).
Extractable P was measured using a standard Bray-1 extract (49) (0.025 M HCl and 0.03 M NH4F) and analyzed colorimetrically on a Brinkmann PC 900 probe colorimeter (Thermo Fisher Scientific).
A commercial laboratory, Waypoint Analytical, analyzed soil samples at depths 0 cm to 20 cm, 20 cm to 40 cm, and 40 cm to 60 cm in 2017 and 0 cm to 20 cm, 20 cm to 40 cm, and 40 cm to 60 cm in 1994 for soil pH in a 1:1 soil:deionized water slurry.
Soil total carbon and nitrogen were analyzed in soil samples from depth increments of 0 cm to 20 cm, 20 cm to 40 cm, and 40 cm to 60 cm in 1994, 2015, and 2017.
The average of 2015 and 2017 values was used to reduce sampling noise.
Ground soil was analyzed using dry combustion gas chromatography on an Elemental Analyzer (Costech ECS 4010 CHNSO Analyzer).
Because of the lack of carbonate minerals in these soils (38), total C represents total organic C.
In order to evaluate the agronomic status of our starting soil (SI Appendix, Table S1), Waypoint Analytical measured total soil organic matter using loss on ignition for 1994 soil.
Laboratory Analysis of Plant Samples.
The dried aboveground and belowground biomasses sampled in August of 2017 were analyzed for their chemical composition.
The homogenate unsorted clipped strip of dried biomass for each of 154 plots was ground completely and then subsampled.
Additionally, for all monoculture plots and five 16-species plots, the total sorted quantity, including leaves, stems, and inflorescences if present, of each of the 15 plant species was additionally ground to provide estimates of their individual traits.
Because the legume, Lupinus perennis, has a spring growth and seed shedding pattern that required a separate spring biomass sampling to determine its tissue nutrient contents, samples of L.
perennis from June in 2019 were also analyzed and used instead of the 2017 sample.
Plant samples were ground using a Model 4 Wiley Mill (Thomas Scientific) and analyzed at a commercial laboratory, Waypoint Analytical, for tissue chemistry using method 3050B of the Environmental Protection Agency Manual SW-846.
Specifically, each plant sample was digested in concentrated nitric acid followed by heating for 15 min at 95 °C.
Then 30% hydrogen peroxide was added until effervescence was no longer observed, followed by 5 mL of concentrated HCl and continued heating for 30 min.
Five to ten milliliters of water was finally added to the sample following filtration using Whatman #2 and analyses using Inductively Coupled Plasma Optical Emission Spectrometry (Perkin-Elmer Optima 8300).
Estimation of Ecosystem Nutrient Pools.
The concentration of each measured soil variable was adjusted to an area density quantity (grams per square meter) with soil bulk density.
Bulk density was measured in 2018 to a depth of 60 cm in 20-cm increments using an AMS Inc.
split soil core sampler with a removal jack (part numbers 400.99, 403.41, 403.73, 211.05, and 211.06) in a subset of plots (87) with a sample size of 26, 16, 15, 15, and 15 at 1, 2, 4, 8, and 16 number of species, respectively, randomly chosen while including two replicates for each species in monoculture where available.
For unmeasured plots, we estimated bulk density using a linear regression of the dependency of bulk density (0 cm to 20 cm) on % soil C (0 cm to 20 cm) measured in 2017.
Bulk density was not measured in 1994.
We estimated bulk density (0 cm to 20 cm) values in each plot in 1994 using the measured % soil C values in 1994 (0 cm to 20 cm) and the regression fit with % soil C in 2017 (0 cm to 20 cm).
The predicted mean bulk density of 1.45 g⋅cm−3 (0 cm to 20 cm) in 1994 approximates measured soil bulk density at the site's soil survey of the Nymore series of 1.4 g⋅cm−3 (0 cm to 23 cm) (ref.
Estimated bulk density in 1994 at 0 cm to 20 cm had treatment means ± 1 SE of 1.45 g⋅cm−3 ± 0.01, 1.44 g⋅cm−3 ± 0.00, 1.45 g⋅cm−3 ± 0.01, 1.44 g⋅cm−3 ± 0.01, and 1.44 g⋅cm−3 ± 0.01 at 1, 2, 4, 8, and 16 number of species, respectively.
Bulk density measured in 2018 at 0 cm to 20 cm had treatment means ± 1 SE of 1.46 g⋅cm−3 ± 0.015, 1.43 g⋅cm−3 ± 0.015, 1.42 g⋅cm−3 ± 0.019, 1.36 g⋅cm−3 ± 0.019, and 1.37 g⋅cm−3 ± 0.018 at 1, 2, 4, 8, and 16 number of species, respectively.
We then used the equivalent soil mass approach to adjust for sampling 20 cm deep across all plots, despite an assumed change in density, by adding mass from the 20- to 40-cm-depth increment or subtracting mass at 0 cm to 20 cm relative to the change in bulk density from the reference value in 1994 (SI Appendix) (50).
The pool of nutrients in aboveground biomass was calculated using the percent of each element in the biomass from the unsorted clipped strip multiplied by the dry biomass in each plot.
Aboveground biomass was calculated as the dry-weight (grams per square meter) average of both sorted and unsorted strips as has been done historically in this experiment.
Plant litter, dead biomass on the soil surface, was not included in this measurement, but there were negligible quantities of litter given that the field is annually burned.
Belowground biomass was calculated as the dry weight (grams per square meter) (0 cm to 30 cm) for each plot.
To reduce sampling noise from interannual variability, the average of aboveground and belowground biomass measured in 2015 and 2017 was used for all statistical analysis and calculations.
To improve readability, we refer to these as 2017 within the text as the year when the plant tissue was chemically analyzed.
The change in ecosystem nutrient pools for N, K, Ca, and Mg was estimated as the change in each plot of each element in the soil from 1994 to 2017 (as grams per square meter of each element in the 0–20 cm soil depth increment) plus the total amount of each element measured in aboveground and belowground biomass (0–30 cm) in 2017 (as grams per square meter).
Statistical Analysis.
Analyses were performed using R version 4.1.1 and JMP 14 Pro.
Linear regressions were used to test the dependence of soil and plant variables on experimental plant biodiversity using the natural log of plant species number (1, 2, 4, 8, 16).
For analysis of the plant biomass pools, the percent increase from the monoculture mean was used as the response variable.
For each set of analysis, a false discovery rate (51) correction was applied to the P value for each regression.
The regression results were robust to a variety of transformations of the y variable and are presented on the untransformed y scale.
The dependance of the sum of aboveground and belowground biomass (total biomass) on the log of plant biodiversity and soil variables (C, N, Ca, Mg, K, P, pH) was tested using a generalized least-squares model with a power variance structure (varPower) on the fitted values (R package nlme).
Multimodel inference (R package MuMIn) was used as a model selection approach with each soil variable and the natural log of plant biodiversity with the conditional average using the Bayesian Information Criterion.
The dependance of ecosystem nutrient pools (N, K, Ca, and Mg) on the presence of different plant functional group sets was tested using a generalized least-squares model with a variance structure for the factor to account for unequal variance (varIdent, nlme).
Differences among means were compared using least-squares means (R package emmeans) followed by a Tukey correction using the Satterthwaite estimation of the degrees of freedom.
As supplemental analyses, we ran these same tests of the effects of functional group presence on the change in soil C, N, K, Ca, and Mg on aboveground and belowground biomass (belowground log transformed) and on the pools of N, K, Ca, and Mg in aboveground and belowground biomass.
A trade-off surface among plant species in their traits was tested by analyzing the dependence of belowground biomass (0 cm to 30 cm) in monoculture on percent aboveground N and percent aboveground K using a linear regression.
The time series mean of belowground biomass for each species' in monoculture was the response variable, and the average tissue chemistry (%N and %K) for each species measured in its monocultures and five 16-species plots were the explanatory variables.
R graphical package rgl was used to generate a regression plane in Fig.
4 with an aspect ratio of 1:1:1 (x:y:z).
Purpose of Review Lowering the impact of forest utilisation on the forest environment is a part of the improvement in sustainable forest management.
As part of forest utilisation, timber harvesting can also cause environmental implications.
The main impact of forest operations is on the soil, on regeneration and on the residual stand.
The aim of the present review was to identify the state of the art in forest utilisation, identifying how and how much forest operations affect forest soil, regeneration and the remaining stand.
Particular attention was paid to the level of impact and potential to limit this.
Recent Findings There are a large number of publications tackling forest harvesting, but most of them do not give a comprehensive framework and they mainly focus on one or very few aspects of forest damage.
In order to improve general knowledge of the impact of forest operations, it was proposed that the scope of recent findings should be examined and a compilation of the available results from different regions should be presented in one paper.
Summary It was found that the least impactful machine-based forest operations were harvester–forwarder technologies, while a larger scale of damage could be expected from ground-based extraction systems (skidders) and cable yarders.
Animal power, if applicable, tended to be very neutral to the forest environment.
A decrease in damage is possible by optimising skid trail and strip road planning, careful completion of forest operations and training for operators.
The existence of legal documents controlling post-harvesting stand damage are rare and have been implemented in only two countries; there is no post-harvesting control on soil damage and natural regeneration.
Similar content being viewed by others  Land use change and forest management effects on soil carbon stocks in the Northeast U.S. Article Open access 06 February 2024  Effect of Deforestation and Forest Fragmentation on Ecosystem Services Chapter © 2022  Impact of Forest Operations in Four Biogeographical Regions in Europe: Finding the Key Drivers for Future Development Article Open access 02 August 2024 Explore related subjects Discover the latest articles, books and news in related subjects, suggested using machine learning.
Agroecology Arboriculture Environmental Impact Forestry Forest Ecology Forestry Management Introduction One of the main and essential aims of the last 20 years within the forestry sector was to improve sustainable forest management (SFM) [1].
SFM includes the ecological aspects of forest operations, and it aims to develop new methods and technologies for sustainable use of forest resources and to minimise any negative impact on the environment [2].
Focusing on forest harvesting, it is important to consider high productivity (economic aspects), a low negative impact on the environment (environmental aspects) and safe working conditions for forest operators (ergonomic and social aspects) [3••].
Forest logging is an impactful operation which could lead to possible implications in forest ecosystem.
In particular, in recent years, forest researchers have focused on the impact of forest operations in relation to the soil, the regeneration dynamics and the stand conditions.
It is important to underline that soil is highly sensitive to improper logging activities [4], and the soil environment could suffer substantially over a long period of time thereby affecting forest productivity and ecosystem efficiency [5].
Forest soil impacts with a higher intensity in terms of area are mainly linked to ground-based extraction systems, such as skidding and traditional cable yarding; however, growing harvester and forwarder use, especially in Europe [6], has also impact on soil compaction.
With this in mind, one of the most important ecological issues for the forest sector is a minimisation of the ground disturbance caused by forest operations [7].
If not properly implemented, forest operations with extraction based on skidders or large forwarders could lead to high soil compaction [4], and later to soil erosion and rutting, particularly evident along skid trails and strip roads.
The impact on forest regeneration is more complex to evaluate directly.
Some studies reported that soil compaction due to the passing of machinery often leads to an inhibition of potential tree regeneration [8, 9•].
On the other hand, in other studies the improved recruitment of seedlings and saplings was observed in areas where soil had been scarified or modified by logging activities [10, 11].
So, this particular aspect of forest operation sustainability is very difficult to analyse unequivocally in the short period of time after an operation.
The impact on the residual stand may decrease the quality of residual trees but also increase tree mortality due to insect and disease infestation [11] and fungal decay [12] as well as lead to stem deformity and significant losses in final crop volume and value [13].
Furthermore, excessive damage to residual trees during logging operations may change aesthetic value and directly influence other ecosystem services, including recreational ones.
Taking into consideration the abovementioned dangers, the methods of felling, processing, bunching and extraction should be planned on a larger scale and for a longer period of time, with consideration to environmental, economic and social contexts [14].
In recent years, much scientific research has been focused on assessing the impact of logging in relation to sustainability, assessing forest ecosystem resilience and suggesting best practice.
In light of the large but scattered number of scientific publications on this topic, this paper is an attempt to bring together the in-depth knowledge and insights of experts within an integrated and comprehensive framework using research collated over the last decade with special attention to the last 5 years.
In particular, the aim of this paper was to find out how contemporary studies and good practices contribute to the mitigation of environmental impact due to forest operations, such as soil damage and injuries to natural regeneration and the remaining stand.
Materials and Methods Literature Research One of the basic techniques to search for particular documents in a complex database is the use of Boolean Operators.
The Boolean search method is a symbolic logic system that creates relationships between expressions and words.
The use of Boolean search has the aim of analysing all studies in a specific research field.
The research of papers for this review was performed using the databases of Science Direct, ISI Web of Knowledge and Google Scholar.
Using the search string “Forest operations impacts” and related synonyms expressions four specific categories, returned, in total, over 944,000 findings, while over 72,000 findings appeared once the search was restricted to research during the last 5 years (Fig.
1 figure 1 Schematic representation of bibliographic research, detailed for the four specific thematic groups (soil damage; regeneration damage; residual stand damage; multiple aspects evaluation) and contextualised to the long period of time and to the period between 2013 and 2019  Full size image However, many items identified in the search were not completely related to the addressed topic.
Eventually about 90 papers published in the last 5 years were selected and analysed with the focus on the evaluation of forest operations and the results of their impact on the environment, i.e. the soil, regeneration and the remaining stand.
Results and Discussion Harvesting-Soil Interaction Soil plays a crucial role in forest ecosystems by transmitting nutrients and water, providing energy flows that are linked to forest productivity and sustain biodiversity [15].
Features of Forest Soil After Harvesting In terms of the visual features of the soil after a forest operation and the condition of the canopy cover, these can be included in one of the four following types: (I) undisturbed soil, canopy cover not removed (NDS-NCR), e.g. normal control samples; (II) undisturbed soil, canopy cover removed (NDS-CR), e.g. logging gaps without winching corridors; (III) disturbed soil, not canopy cover removed (DS-NCR), e.g. winching corridors; and (IV) disturbed soil, canopy cover removed (DS-CR), e.g. disturbed skid trails, landing sites and processing sites.
How The physical, chemical and biological properties of the forest soil change as a result of harvesting operations, and this is commonly referred to as soil disturbance [4, 16,17,18,19].
Chemical and biological changes occur in the soil after physical modification.
Therefore, changes in the physical properties of the soil are the most prominent indicator of soil disturbance following the use of logging equipment [4, 20].
Detrimental soil disturbance associated with ground-based extraction often includes compaction, rutting, lateral soil displacement, topsoil mixing and the formation of puddles.
A large number of factors influence the extent and severity of soil compaction.
As found by many authors, overall harvesting operations can lead to a reduction in soil porosity [14, 19,20,21,22,23], increased soil erosion [20,21,22,23,24] and a decrease in root penetration and length expansion [19].
Soil compaction can lead to reduced water infiltration and hydraulic conductivity, which contributes to increased waterlogging on flat terrain and soil runoff with erosion on slopes.
Soil compaction can reduce the access of plant roots and microorganisms to water, oxygen and nutrients.
Long-lasting damage to the soil system can negatively affect forest productivity and ecosystem functionality [5].
One way to estimate the severity of logging damage to the forest soil is to measure soil bulk density before treatment and compare it with its critical level after harvesting operations [25, 26].
[19] reported higher soil penetration resistance 10 years after skidding.
An increase in the bulk density of soil should not always be regarded as equivalent to a detectable decrease in tree growth.
Changes in soil bulk density that have led to some decline in the biological and vegetative development of beech and maple seedlings have been observed when increased by 0.15 to 0.43 g cm−3 [19].
Depending on soil type and tree species, the number of changes in soil compaction that will result in reduced plant growth varies.
In this context, specific surveys are necessary to assess the real occurrence of the negative effects of bulk density increment on tree growth.
An important factor differentiating soil changes after harvesting is the impact of different machinery.
[27] compared the influence of different logging machines on soil compaction and reported that all wheeled machines caused the same amount of soil compaction in the ruts, despite differences in tires, machine weight, etc.
[28] studied the effect of bogie tracks on the physical properties of the soil during forwarding operations in a coniferous stand in north-eastern Italy.
The authors reported a clear difference in the physical parameters of the soil before and after operations.
[29] studied the effects of four timber logging techniques (cable yarder, skidder, manpower and chute system) on some physical and chemical properties of the soil in Turkey’s forests.
It was found that logging by skidder can have a clear influence on soil permeability, bulk density and soil water balance, and that skidding can reduce the content of organic matter and nutrient levels in the soil.
[30] studied the influence of mechanical site preparation treatments on the physical properties of disturbed soils in harvested wet lands.
Their results showed that macroporosity had not recovered to the pre-harvest levels for any site preparation treatments except Mole-Plowed; bulk density and total porosity recovered to near pre-harvest levels for all treatment combinations, but saturated hydraulic conductivity rates remained lower than the pre-harvest values.
Summarising, forest operations usually lead to changes in the soil’s physical, chemical and biological characteristics.
One of the most important factors influencing soil impact intensity is the level of mechanisation, as well as machine weight and type of operation (i.e. skidding or forwarding).
Soil compaction can be reversed; however it may take more than 10 years for full rehabilitation [31].
How Much The extent and severity of soil disturbance during harvesting operations depends on several factors that can be divided into three groups:  1.
Stand conditions: extracted timber volume [28, 32], soil type and texture [33,34,35], soil moisture content [25], soil’s organic matter content, site topography [34, 35], stand density and canopy extension [34, 35];  2.
Yard logistics: harvesting system, advanced level of logging operation planning, type of machines, logging method [28, 32], machine and load mass, tire pressure, vibrations transmitted by vehicles [20], intensity of machine traffic [32], weather conditions during skidding operation, training, experience and expertise of operators as well as planning and worker proficiency [36];  3.
Forest road network characteristics: density of roads and skid trails, slope gradient of skid trail [20].
Expansion of soil damage by logging depends on the type of technology used [4, 17].
More pressure, slipping and a lower speed can dramatically increase soil disturbance on a steep slope trail.
[37] demonstrated that physical, chemical and biological features of the soil can be greatly impacted by harvesting operations and consequently, eventually soil mesofauna could be changed.
In particular, heavy ground-based logging equipment can cause severe and long-lasting damage of the soil system, which can negatively affect forest productivity and ecosystem function [5, 16, 38].
The results of various studies of the impact of mechanised harvesting on forest soil show that changes to the soil can be very different, from low to very high, including values that exceed 100% (Table 1).
Table 1 Magnitude of soil changes as published by selected authors Full size table In addition, at a low level of mechanisation, Jourgholami and Majnounian [39] reported that mule logging had a statistically significant effect on soil bulk density along mule trails before and after extracting.
Soil bulk density increased significantly as animal passes increased in number; however, the degree and level of compaction did not differ with increasing trail slope.
In contrast, Badraghi et al.
[53] evaluated soil disturbance and compaction caused by mule extraction and reported that only 1% of the harvested area was disturbed, and soil bulk density increased only by 0.3%.
Limiting and Preventing Disturbance One goal of forest managers in harvesting should be to minimise the impact of vehicles on the soil, the negative effects of which can be significant and long lasting, although often unrecognised or neglected [4].
The ongoing trend to constantly increase the size, power and load of machines makes it even more imperative to plan logging logistics in order to limit soil disturbance and stand damage [11].
In the available studies, suggestions to reduce soil damage due to forest operations can be grouped into the following:  1.
Machine traffic should be carried out (if possible) during dry and favourable weather conditions [27, 44, 54,55,56], and it is important to reduce the number of load passes.
The proper design of forest roads can play an important role in reducing soil disturbance [18, 55,56,57,58,59], and it is important to reduce the trail slope gradient.
Both training and supervision can be efficient in soil impact mitigation [12, 14].
Employing ameliorative site preparation could contribute to initial survival and an increase in early growth on harvested stands with wet soil conditions [16, 30].
Applications of straw and sawdust mulch following skidding operations can reduce surface runoff and sediment on skid trails [16, 49].
Traditional animal power with a low impact on the soil can be used for timber extraction in steep terrain conditions [39].
Harvesting-Tree Regeneration Interaction Timber harvesting represents also a key factor in the ecological management of stands, changing (in negative or positive way) stand structure and species diversity [13, 60].
Availability to sunlight, reduction in plant competition and scarified soils are needed for tree regeneration, and these favourable conditions can be created by harvesting operations [10, 61•].
Proper harvesting operations not only control the amount of sunlight that reaches the forest floor but also make the soil and site conditions ideal for the successful natural regeneration of trees [61•].
Forest managers applying close-to-nature silviculture plan harvesting systems to control the available light on the forest floor in order to obtain regeneration species diversity.
In addition to the positive impact of harvesting, mechanical damage to young trees is often an inevitable side effect.
With this in mind, good forestry practice should consider ways to mitigate these negative effects.
How Effect on Seedling Growth The felling of trees and the opening of the forest canopy increases the intensity of light reaching the forest floor, and the establishment and growth of a tree’s regeneration is positively affected [13].
Disturbances that open small canopy gaps create environmental heterogeneity, particularly the amount of light and water reaching the forest understory, and thereby provide a range of regeneration niches for trees and other plants [60].
In addition, scratches on the surface of forest soil due to skidding create favourable conditions for seed germination and further sapling growth [10].
However, in some research it was found that the germination rate had a strong negative correlation with an increase in soil bulk density [22,23,24, 62].
Moreover, germination rates and growth could be significantly reduced by the number of passes and the trail slope gradient [19, 22, 23, 55].
The height of seedlings was also found to be lower on machine operating trails than in undisturbed areas [63].
The effects of soil compaction may create particularly challenging conditions for seedling survival during drought periods, because seedlings with short roots may be unable to access water at deeper soil levels [44, 55].
Mechanical Damage Forest regeneration can be affected by mechanical damage during harvesting [18].
The extent and severity of damage to forest regeneration can be influenced by several factors, from which the logging system and harvesting intensity seem to be the most influential (Table 2).
Table 2 Affective factors in level of damage to regeneration by harvesting operation Full size table In forest with a natural regeneration system, after shelter-wood and selection cuttings, damage to saplings is common and usually inevitable.
When timber harvesting has advanced planning and the developed forest operation is applied, a reduction in damage to regeneration may be more feasible.
Damaged regeneration by tree felling operations is usually in the form of stem breakage, while the winching operation usually causes uprooting [18].
When trees are growing, stem flexibility decreases, the probability of uprooting reduces while the probability of stem breakage increases [18].
The amount of regeneration damage in the winching stage is usually higher than in the felling and skidding stages.
This was also confirmed by Picchio et al.
[63], where bunching (during winching) was the main cause of damage to regeneration during cable skidder logging, and the amount of regeneration damage on steep slopes was higher than on gentle slopes.
The amount of damage to regeneration can decrease when workers have more experience [61•].
Soil scarification can increase the success of natural regeneration [10], but at the same time soil compaction may reduce the establishment of regeneration [44] and growth of regeneration [23].
Compacted soil layers due to forest machine traffic are the most common problem affecting seedling regeneration after forest harvesting [23, 432, 44].
García-Orenes et al.
[68] reported that salvage logging may damage the bank of seedlings and affect plant regeneration after fire, reducing plant density.
Salvage logging can also decrease the amount of natural tree regeneration [24, 69].
Fernández and Vega [70] found no detrimental effect of a salvage logging treatment compared with natural regeneration.
These contradictory results could be due to factors such as the type of soil, when and how the salvage logging treatment is carried out and meteorological conditions which can be decisive.
How Much The share of regeneration that can be damaged during different logging systems can vary from several percent to more than 60% (Fig.
The mean frequency of damage on seedlings, small saplings and large saplings were 8.8%, 12.8% and 19.5%, respectively, in skidder extraction in mixed beech stands [18].
A lower level of damage was observed after cable-skidding and ranged from 4.9 to 7.1% [18].
Stańczykiewicz et al.
[74] studied the damage of regeneration using two systems: (1) a tower cable system combined with farm tractor and (2) a skidder in a mature spruce stand.
The damage of regeneration using the tower cable system (23.9%) was lower than using the skidder system (61.3%).
The tower cable system mostly destroyed regeneration, while during skidder logging, it is usually stem and side-branches that can be broken.
Most damage to regeneration using the tower cable system occurred on the shortest regeneration (up to 0.5 m from the ground), while skidder logging usually affected the regeneration of medium height (0.5–4.0 m).
2 figure 2 Damage intensity of regeneration in different forest types after silvicultural treatments provided by various forest operations.
Results presented as average values ± standard deviation.
Abbreviations used on bars: Hw-Sc-CH [53]: hardwood forest, selection cutting with chainsaw and horse skidding, published in [53], damage 6% ± 2.3%; Hw-Sc-CS [18]: hardwood forest, selection cutting with chainsaw and skidder, published in [18], damage 6% ± 4.1%; Sw-Th-C/PT [71]: softwood forest (pine forest), thinning with chainsaw and processor with tractor skidding, published in [71], damage 9% ± 6.6%; Sw-Th-CT [71]: softwood forests (pine forest), thinning with chainsaw and tractor skidding, published in [71], damage 11%± 7.9%; Hw-Sc-CS [18]: hardwood forest, selection cutting with chainsaw and skidder, published in [18], damage 12%± 0.6%; Hw-Sc-CT [72]: hardwood forest, selection cutting with chainsaw and tractor skidding, published in [72], damage 13% ± 4.9%; Mx-Th-CT [73]: mixed forest, thinning with chainsaw and tractor skidding (with snatch block), published in [73], damage 24% ± 6.5%; Mx-Fc-CY [67]: mixed forest (spruce-beech forest), final cutting with chainsaw and cable yarder [67], damage 24%± 6.8%; Mx-Th-CT [73]: mixed forest (pine and other hardwood species), thinning with chainsaw and tractor skidding without snatch block, published in [73], damage 43%± 5.2%; Mx-Fc-CS [67]: mixed forest (spruce-beech forest), shelterwood cutting with chainsaw and skidder [67], damage 61%± 18.8%  Full size image Limiting and Preventing Damage to Regeneration Damage to regeneration can be limited by introduction of the following:  1.
Identifying and Marking fragments of regenerated stands for protection and avoiding winching through these stands; planing of skid trails and lay out landings should be carried out before harvesting operations begin.
Focusing on protection of the residual stand rather than on the trees being removed.
Considering the felling season, there is usually less damage during the winter months.
Matching machine/equipment type, size and deployment to stand and site conditions [19].
Limiting or concentrating machine activity on skid trails and access corridors.
Increasing awareness of the consequences of mechanical injuries to trees and forest stands.
The use of the snatch block could positively improve the winching operation.
Alternatively, when possible and when financially acceptable, different forms of extraction should be used, for example, cable cranes or traction-winch-supported forwarders [74].
A detailed planning strategy will reduce damage to a level which is acceptable and predictable [12].
For a post-harvesting assessment of a logging operation, obtaining an accurate measure of residual stand damage is recommended [12, 18].
A post-harvest inventory of soil and stand damage, and prioritisation of contractors that have a good level of training, should be carried out for reduced impact logging (RIL) [19].
Harvesting-Stand Interaction Forest operations influence the stand condition, which can be measured by taking into account several factors, mainly environmental, social and economic [3••], as well as ergonomic factors and those linked to product quality [75].
It may be considered that the level of damage depends on the machine operator’s skills; however, there are certain objective reasons that can cause a higher probability of damage.
The level of damage caused to residual trees during forest operations has been described by several authors and many factors influencing damage level have been indicated.
As a summary of these factors from different findings, Siren et al.
[76] quote in their publication that the level of damage depends on the forest characteristics, such as the amount of timber removed during harvesting, stand density and basal area.
In addition, well designed access to the forest can limit the probability of damage, such as skid-trail spacing or road density [12].
Extracting timber on steeper slopes usually causes more damage [19, 77, 78].
It was also found that tree injuries depend on the season, and can be higher in summer [79], as well as affected by stand structure: in uneven-aged stands, damage can be more frequent, especially among younger trees [76].
Mechanised harvesting tends to cause less damage than using a chainsaw for felling and more damaged trees are observed near strip roads [80, 81].
The harvesting system definitely influences the level of damage: the long wood system (LWS) is usually associated with a higher probability of damage compared with the short wood system (SWS) [82].
Wounds created due to bark and cambium removal can heal; however, bark pockets or stone pockets are created, defects difficult to detect many years after wounding, especially if they occurred on a young tree.
Newly grown wood tissue can cover the wounded area, but the disjunction between the old and the new tissue can create ring shake.
Generally, wounds negatively impact diameter growth which may slow down by 8–13% [12, 83].
The healing rate is faster on younger trees if the wound is higher on a tree and at a lower elevation [18]; a slower healing process was observed on bigger wounds as well as on southern slopes [18].
In addition to discontinuity in the wood, sometimes irregular stem forms, local grain deviations and colour variations (not necessarily pathological) can be observed.
However, injured trees can have a high risk of pathogen infections following harvesting damage, since open wounds with missing bark and cambium can be susceptible to fungi.
Bark inclusions reduce the mechanical strength and the aesthetic appeal of artefacts; therefore, they are not accepted in timber for packaging or for flooring.
Wounded trees are affected negatively, they produce lower-quality timber [84] and a lower diameter increment can be observed [12, 83].
An analysis of the presented findings shows that the most important and principle injuries to the remaining stand are bark and cambium removal from trees.
Most of the damage is observed close to the skid trails.
Trees with damage will produce lower quality timber and are vulnerable to fungi and rot development.
How Damage to the remaining stand can be observed after thinning, selective cutting or another partial tree removal from a stand [76].
Damage is generally understood as bark and cambium removal with partial wood tissue disturbance, also a broken tree.
It is considered that damage can occur due to felling, processing or timber extraction [76]; however, it was also confirmed that rolling rocks in hilly areas can be a reason for damage to remaining trees [85•].
Additionally, another cause of damage which is as frequent as injuries generated by harvesting, can be animal browsing which affects ca.
3–4% of wounded trees in the stand, or twice as many in spruce stands [86].
During harvester–forwarder operations, it is usually the felling and pulling of trees by the harvester boom which injures the remaining trees [76].
In motor manual operations with a chainsaw in LWS, it is usually skidding rather than felling which creates more damage [12, 84].
If winching and skidding are analysed as two separate operations, it can be seen that skidding causes more damage to the remaining stand [78].
How Much In practice, thinning or selective cutting operations are rather associated with some level of damage to the remaining stand, although it is occasionally possible to complete the extraction of short logs using animal power without causing damage [53].
However, in order to keep damage at an acceptable level, legal requirements or limitations have been implemented in some countries to control damage to the trees.
In Finland, for example, if the percentage of trees with damage is over 15%, it exceeds the limit of the Forest Act [76].
In Poland, the usual acceptable level of damage to the remaining stand after thinning is 5%.
Usually, there are financial consequences when a higher share of trees is injured.
Short Wood System vs Long Wood System Less intensive damage is usually observed in CTL in thinning, and on average only 7–8% trees can be affected, with no particular difference between older (70–75 y.o.) and younger stands (30–35 y.o.) or species: oak or spruce [87].
[48] confirmed a lower level of damage, 4–6% in thinned stands, where CTL was used, and 9–12% for chainsaw felling with skidding in the late thinning of pine stands.
This was also mentioned by Siren et al.
[76], who compared studies from Slovenia from the last decade, where CTL caused 13–15% and 17–19% when motor-manual technology was used.
A similar level of damage (14–17%) was observed after skidding in an even-aged stand of Corsican pine [73].
An interesting feature of this study was that, 10 years after harvesting/skidding, more damage was revealed (17%), which was explained by the fact that some trees may be hit but have no bark removal, and the consequences of this (dead cambium) may become visible after many years.
Further studies, after 20 years, revealed nearly 18% of damage and that increase was explained by the mortality of some trees [11].
This study also confirmed that skidding caused more damage than felling, and the same was confirmed by Tavankar et al.
[88] (16.3% and 5.2% by skidding and felling, respectively).
To reduce the level of damage while skidding, the short wood system (SWS) may be applied.
In studies carried out by Jourgholami [89], there were 44% fewer damaged trees when SWS was used during skidding.
There were also ca.
twice as many trees with damage when LWS was applied compared with SWS in close proximity to the skid trails (up to 3 m).
This study, however, does not present the productivity when SWS was used.
Nevertheless, there was a substantial difference when LWS was used with skidding as extraction, which left 18% of trees with damage and more than double (45%) the number of injured trees when large and long logs from a much older stand, i.e. 110 y.o. oak were skidded [87].
The same authors observed that a higher thinning (or shelterwood cutting) intensity can cause a higher level of damage.
More injured trees were also observed closer to the strip or skid roads [87].
When tracked machines were used more damage to the roots was observed, although studies were carried out in spruce stands, and these trees have roots which are only partially under the surface of the soil [87].
[76] also provided an interesting method for damage estimation, which considered monitoring the number of trees with damage during the whole life of the stand.
According to these authors, modelling showed that during a 160-year rotation period and after 10 thinnings, the total number of damaged trees continuously grew and reached 90% at the end of the rotation.
[76] also mentioned that in old stands, a higher share of damaged trees (64–70%) can be recorded.
Furthermore, in the study by Sirén et al.
[76] in uneven-aged stands, the percentage of damaged trees (according to the classification of the Forest Act) was 13.8%.
Usually in selection cuttings it is very difficult to reach low damage levels typical for even-aged stands.
Full Tree System The full tree system (FTS), in which felled trees with branches are extracted, can also leave a substantial share of the trees with damage.
In a study carried out in Italy, there were 35–50% of the trees with damage after the skidding or yarding of whole trees using various methods.
The use of snatch blocks when skidding and semi-automatic carriage when yarding were effective in limiting the damage level, while snatch blocks also turned out to be effective in limiting damage without a loss in productivity [17].
A high level of damage was also observed when a feller–buncher was used in Spain, where up to 50% of the remaining trees in coppice stands had some damage [90].
A lower harvesting intensity could cause a lower level of damage in FTS, i.e. up to 22% (in tropical forest conditions) [91].
However, in that study, less than one tree per hectare was harvested, albeit of large DBH sizes ranging from 60 to 216 cm [91].
Animal Power A very low level of damage can be observed when animal power is used.
Animal extraction was completed without any damage [53] when short wood was extracted by carrying, or very low, ca.
3% when animal skidding on the ground was provided.
Limiting Stand Damage Taking into account the studied literature, there are few proposals for limiting stand damage.
Basically, many authors suggest careful harvesting and skidding with particular attention to areas close to skid roads.
However, a suitable design of skid roads can limit the level of damage.
There is also the more objective possibility of using CTL technology and animal force, which tend to cause very low levels of damage to up to 5% of the remaining trees in the stand (Fig.
A high level of damage is mainly observed during skidding, when long wood is extracted or a whole tree system is applied (Fig.
These systems require particular attention when timber extracting is in operation.
3 figure 3 Damage intensity to remaining stand in different forest types after silvicultural treatments provided by various forest operations.
Results presented as average values ± standard deviation.
Abbreviations used on bars: Hw-ThSc-CS [89]: hardwood forest, thinning or selection cutting with chainsaw and skidder, published in [89], damage 3% ± 1.0%; Hw-Sh-HF [48]: hardwood forest, shelterwood cutting with harvester and forwarder, published in [48], damage 5% ± 1.1%; Hw-Sh-HF [87]: hardwood forest, shelterwood cutting by harvester and forwarder, published in [87], damage 8% ± 1.0%; Hw-Sc-CS [13]: hardwood forest, selection cutting with chainsaw and skidder, published in [13], damage 8% ± 1.4%; Hw-Sh-CS [48]: hardwood forest, shelterwood cutting with chainsaw and skidder, published in [48], damage 10%± 2.8%; Hw-Th-CS [11]: hardwood forest, thinning with chainsaw and skidder, published in [11], damage 14% ± 2.0%; Sw-Th-CS [73]: softwood forest (pine), thinning with chainsaw and skidder, published in [73], damage 16% ± 2.1%; Hw-Sc-CS [88]: hardwood forest, selection cutting with chainsaw and skidder, published in [88], damage 21% ± 1.0%; Sw-Sc-HF [76]: softwood forest, selection cutting with harvester and forwarder, published in [76], damage 21%± 2.6%; Hw-Sh-CS [91]: hardwood forest, shelterwood cutting with chainsaw and skidder, published in [91], damage 22% ± 2.0%; Hw-Sh-CS [87]: hardwood forest, shelterwood cutting with chainsaw and skidder, published in [87], damage 32% ± 4.9%; Sw-Th-CY [17]: softwood forest, thinning treatment by chainsaw and cable yarder, published in [18], damage 43%± 10.6%; Hw-Th-CS [90]: hardwood forest, thinning treatment by chainsaw and skidder, published in [90], damage 50%± 5.0%  Full size image Conclusions Felling and extracting of timber from forests has an inevitable impact on the environment.
This impact is either in the form of soil disturbance, regeneration or stand damage.
Soil Damage Soil damage seems to be the most difficult to avoid.
Any machine (or animal power) has impact on the soil, especially at the stage of timber extraction.
Soil disturbance includes a change in the physical properties, followed by modifications in the chemical and biological properties.
Common methods used to estimate soil damage severity include the measurement of bulk density or penetration resistance which is compared with critical values, when possible.
For example, regarding bulk density, critical values are limiting factors for root growth, depending on the type of soil, and they vary from 1.4 Mg m−3 for clay soils to 1.8 Mg m−3 for sand and loamy sand soils.
The organic carbon or CO2 concentration and QBS-ar index are parameters which also appear in the latest research widening the knowledge of soil reactions to forest operations.
Damage expansion generally depends on the method of forest operation and the machines used, mainly their weight, load and number of passes.
Weather conditions, tyre variations and size are also essential in limiting rutting and general soil erosion.
Good forest roads and skid trail (strip road) networks, as well as their quality, can be essential in limiting soil damage.
Nevertheless, damage and erosion on slopes with greater gradients are difficult to control.
However, erosion control can be achieved when brushwood, straw or chips/sawdust mulch are applied on skid roads during and after extracting.
In any cases of changes in soil properties, it is worth noticing whether soil regeneration takes place, and if not, a reclamation process can be put in place to return the soil to the pre-harvest state.
Regeneration Damage Forest operations can be very severe for forest regeneration.
However, it is worth mentioning that harvested trees open the canopy and initiate soil scarification which contributes to future tree growth.
On the other hand, germination, young tree growth and root development can be negatively affected after forest operations, where an increase in bulk density was observed after high traffic intensity or on steeper slopes.
Ground-based extraction-transport systems, where timber has direct contact with the soil, usually cause more damage to regeneration than other systems such as forwarding or aerial transport systems.
Limiting damage in natural regeneration is difficult as young trees grow at a higher density.
Using forwarders and sky yarders should limit injury, as well as the planning of skid roads and winching corridors before felling and extracting.
Stand Damage The presented results have shown that it is possible to restrict the level of damage to the remaining stand at a low level by using mechanised CTL forest operations.
In harvester–forwarder-based thinnings, damage should be at level of over several percent of the remaining trees, although it can occasionally reach ca.
This level, however, should be treated as exceptional.
A higher share of injured trees can be observed when skidding is used, and it can vary from ca.
10 to 20% in the long wood system.
However, this may double when full trees are extracted.
When yarding is used, the expected damage can also vary from 35 to 50%.
Post-Harvesting Assessment According to the studied literature, there are local prerequisites that may be helpful in limiting damage to the remaining stand.
Taking into account best practice, there are two European countries that have legal prerequisites to control stand damage: in Poland, no more than 5% of the remaining trees should have injuries.
If the percentage is higher, financial penalties may be imposed on the entrepreneurs carrying out forest operations.
In Finland, legal regulations accept damage no higher than 15%.
The literature analysis presented shows that there is no control on the amount of soil damage as well as natural regeneration.
The area of soil damage can be controlled naturally by the design and establishment of permanent skid trails (for skidders) or strip roads (for forwarders).
However, in both cases, there is still the possibility of additional damage due to unskilled operators.
The same can be observed in natural regeneration.
Therefore, the setting of maximal limits, as in the case of stand damage, should further limit soil disturbance and injuries to natural regeneration.
Abstract Coral reef restoration is an increasingly important part of tropical marine conservation.
Information about what motivates coral reef restoration as well as its success and cost is not well understood but is needed to inform restoration decisions.
We systematically review and synthesize data from mostly scientific studies published in peer-reviewed and gray literature on the motivations for coral reef restoration, the variables measured, outcomes reported, the cost per hectare of the restoration project, the survival of restored corals, the duration of the project, and its overall spatial extent depending on the restoration technique employed.
The main motivation to restore coral reefs for the projects assessed was to further our ecological knowledge and improve restoration techniques, with coral growth, productivity, and survival being the main variables measured.
The median project cost was 400,000 US$/ha (2010 US$), ranging from 6,000 US$/ha for the nursery phase of coral gardening to 4,000,000 US$/ha for substrate addition to build an artificial reef.
Restoration projects were mostly of short duration (1–2 years) and over small spatial extents (0.01 ha or 108 m2).
Median reported survival of restored corals was 60.9%.
Future research to survey practitioners who do not publish their discoveries would complement this work.
Our findings and database provide critical data to inform future research in coral reef restoration.
Implications for Practice  Most published coral reef restoration research is focused on improving the restoration approach and answering questions of ecological concern.
Coral reef restoration is feasible but can be costly depending on the site selected and technique applied.
A standardized reporting on cost would benefit development of new projects.
Reporting on the social and economic benefits of coral reef restoration is needed.
There is likely a substantial knowledge and communication gap between scientific researchers and practitioners which needs to be breached to move the field of coral reef restoration forward.
We need to know the cost for employing a specific technique and its likelihood for success in order to invest our money strategically and maximize the outcome.
Introduction The world's coral reefs are under threat from stressors such as destructive fishing practices, overfishing, coastal development, and water pollution (Burke & Spalding 2011).
These stressors are exacerbated by climate change (Hoegh-Guldberg et al.
2007; Hughes et al.
2017), which will increase the frequency of severe coral bleaching events and reduce the extent of healthy and mature reef assemblages globally in the future (Frieler et al.
Active restoration (the process of actively assisting the recovery of an ecosystem that has been degraded, damaged, or destroyed; SER 2004) may be necessary when natural ecosystem recovery is precluded (Perrow & Davy 2002).
Coral reef restoration is often regarded as a small-scale emergency action to buy time (Shaver & Silliman 2017) while we tackle climate change and poor water quality at larger spatial scales (Hughes et al.
2017; IPCC 2018).
However, repeated restoration might be necessary to promote recovery of reefs after successive bleaching events.
Under these circumstances, reefs providing sources for new coral larvae would play an important role in accelerating the recovery of damaged systems (Hock et al.
In order to conserve coral reefs and maintain ecosystem functions in the face of external threats, we may even need to consider new interventions such as engineered habitats or assisted evolution (Anthony et al.
When assessing the published scientific literature, the specific objectives of coral reef restoration projects are dominated by investigating the biological response of corals to transplantation (Hein et al.
2017), yet the underlying motivations are unknown (Bernhardt et al.
2007; Aradóttir et al.
Motivations for restoration are defined as “answers to the question of why ecosystems should be restored” (Clewell & Aronson 2006).
Similar to restoration of other marine coastal ecosystems (Bayraktarov et al.
2016), publicly available data on the cost and success of restoration techniques are sparse and inconsistently reported (Edwards & Gomez 2007; Iacona et al.
Given the recent investments in coral reef restoration globally, knowing the cost of employing a specific technique and its likelihood of success are essential for planning for and developing of new restoration projects.
In this article, we review and analyze empirical results from mostly peer-reviewed published coral reef restoration projects (including some gray literature and personal communications) to explore the motivations for the projects using the framework developed by Clewell and Aronson (2006) (and used in evaluating terrestrial restoration by Hagger et al.
2017) and the ecological, economic, and social outcomes measured according to Wortley et al.
We report on coral reef restoration success by synthesizing a database (available online doi:10.5061/dryad.sv798dm) containing information on cost, survival, project spatial extent, and duration for projects employing six common coral reef restoration techniques.
Methods Data Collection We conducted a systematic literature search using Web of Science (Core collection; Thomson Reuters, New York, New York, U.S.A.) and Scopus (Elsevier, Atlanta, Georgia, U.S.A.) and the title search terms “(coral reef* OR coral*) AND restor*”, as well as “(coral reef* OR coral*) AND rehab*”.
The search returned 141 studies spanning 27 years (1991–March 2018).
An EndNote (Version X7.0.2; Thomson Reuters.) search was then performed within the full text using the search terms (cost* OR feasib* OR surviv*).
Additional information was gathered by following on citations, personal communication with three practitioners, and inspecting diverse restoration databases and webpages.
The systematic literature search returned 87 studies.
Information on the restoration technique employed, cost per hectare of the restoration project, project spatial extent and duration, and survival of restored corals was extracted as “observations.” A data source may contain more than one observation, e.g. if a different coral species was examined or the restoration was carried out at multiple sites.
Data from plots and figures were extracted graphically by using WebPlotDigitizer (https://automeris.io/WebPlotDigitizer/).
Data for costs and survival were calculated for the database as follows.
Where only cost per coral colony was provided, calculations for the restoration cost per hectare were estimated by assuming a transplanting schedule with four coral colonies outplanted per m2, or 40,000 coral transplants per hectare (Edwards & Gomez 2007) to convert cost per colony into cost per unit area.
Based on a survival rate of restored organisms of 60.9%, 65,681 coral transplants would be required to populate 1 ha and yield 40,000 live corals.
This median survival of restored corals was calculated from all observations reporting on survivorship in the database.
Each survival value was averaged over the reported pre-transplant, transplant, and post-transplant survival per observation.
All reported costs were adjusted for inflation in each respective country based on consumer price index (CPI) to a base year of 2010 prices.
Data required for economic conversion were downloaded from the World Bank Development Indicators (The World Bank 2019a, 2019b, 2019c).
For a subset of countries, CPI data were unavailable, and these observations were excluded from further analyses, with the original data retained in the database for reference.
If the CPI for a particular year was unavailable, CPI information for the next closest year to the year of data collection reported in the study was employed.
If the study did not report the data collection year, the year preceding the publication date was used.
For restoration costs incurred in 2018, the previous year CPI (2017) was used for conversion.
For studies where local currencies were reported, data were first converted to U.S. dollars using the foreign exchange rates from the Penn World Tables (Heston et al.
2012) and later adjusted to the respective country's inflation based on CPI to a base year of 2010 prices.
A second economic conversion was carried out to account for effects based on differences in the countries' income.
This conversion was based on the gross domestic product as a function of purchasing power parity (GDP [PPP]).
Therefore, we first converted U.S. dollar to the local value of one U.S. dollar in the developing country and then adjusted for inflation to obtain international dollar (Int$) at a base year of 2010 prices.
The difference in cost from economic conversion based on CPI versus GDP (PPP) highlights the greater value (i.e. purchasing power) of one U.S. dollar relative to the official exchange rate of the foreign currency in countries with less developed economies.
Motivations for Coral Reef Restoration For restoration motivations, variables measured, and reported outcomes, one set of response variables was extracted from primary studies (publications describing original research) where one study describes one restoration project.
An exception was the study by Edwards and Gomez (2007), which contained information on five restoration projects.
We searched within the abstract and the introduction of each study for the primary, secondary, and tertiary reasons for the restoration project using categories adopted from Clewell and Aronson (2006) and Hagger et al.
Motivations for each coral reef restoration project were classified as idealistic (social, political, or cultural reasons seeking atonement for environmental degradation or reconnection with nature), experimental (seeking experimental data to answer ecological research questions or improve restoration approach), pragmatic (focusing on the ecosystem services that can be derived from a restored coral reef into the future), legislative (related to legal and policy requirements of governments and other large institutions to recover ecosystems which have suffered environmental impacts, e.g. habitat loss from development, mining, or ship grounding), and/or biotic (motivations aligned with the desire to enhance biodiversity).
The categories idealistic, experimental, pragmatic, legislative, and biotic are not necessarily mutually exclusive but comprise a typology that facilitates their systematic description (Clewell & Aronson 2006).
Variables Measured Variables measured were grouped into “attribute categories” and “sub-attribute categories” (Table S1, Supporting Information) modified from the International Standards for Ecological Restoration by the Society of Ecological Restoration (McDonald et al.
Variables measured during monitoring of the restoration site were categorized as related to ecosystem function and processes (e.g. survival, growth, and productivity) but also the physical environment of the restoration site (temperature, water currents, turbidity, and pH) and the level of threats (invasive species, predators, and physical damage).
Note that the International Standards classify variables such as survival, growth, and productivity under the attribute “ecosystem function” while these would be categorized as variables measuring the biological response of the ecosystem to the restoration intervention in other studies (e.g. Hein et al.
Restoration Outcomes We searched in the abstract, results, and discussion of each study to identify the type(s) of outcomes reported as results.
These were categorized as ecological, economic, and/or social (sensu Wortley et al.
2013) to provide an understanding of the broader outcomes being addressed.
Coral Reef Restoration Techniques Information on six major techniques for coral reef restoration was extracted from the studies reviewed: Direct transplantation: harvesting of coral colonies or fragments from a donor site and the transplantation of these to a restoration site without the intermediate step of growing coral fragments in a nursery (Edwards & Clark 1998).
Larval enhancement: flow-through facilities are used to aid fertilization and competent coral larvae are then seeded to a reef restoration site.
The reared coral larvae can be either free swimming or attached to substrate (Chamberland et al.
Coral gardening: involves two phases (Rinkevich 1995, 2000, 2005, 2008, 2014, 2015a, 2015b): (1) the collection of coral fragments from donor colonies and growing these in field-based (in situ) or land-based (ex situ) nurseries and (2) outplanting the nursery-grown corals to the degraded reef using materials such as epoxy, cement, or cable ties to attach the corals to the substratum (Montoya-Maya et al.
The analyses were carried out for “Coral gardening” indicating the whole process using this technique for restoration and for its components “Collection and nursery phase” and “Transplantation phase” since this is how data were reported by the studies.
Note that the individual components of the coral gardening approach cannot be considered as standalone restoration approaches.
Substrate addition (artificial reefs): utilizes structures deployed on the seabed to mimic characteristics of a natural reef and is often followed by active coral transplantation (Clark & Edwards 1994, 1995).
Substrate stabilization: damaged substrate (e.g. after storms or ship groundings on reefs) is restored to facilitate natural coral settlement and reef recovery (Lindahl 2003).
Substrate enhancement with electricity: mimics the chemical and physical properties of reef limestone deposition, by encouraging the precipitation of calcium and magnesium on artificial substrates using electrical currents (Goreau et al.
The technique was originally developed by Wolf Hilbertz in the 1970s and has led to the commercial product Biorock.
Results Of the 87 studies extracted, 71 were primary sources (publications describing original research) and 16 were secondary sources (studies referring to original research published elsewhere, e.g. reviews).
The 71 primary sources reported on 75 separate restoration projects.
A single study could contain more than one observation.
A total of 335 observations were retrieved from all primary and secondary studies.
The motivations and reported outcomes were recorded at the restoration project level taking into account primary sources only.
One-third of the studies (n = 25) were from less economically developed countries (low income and lower middle income), 13 were from countries with an upper middle income, and the remaining studies were from high-income countries (n = 45) (Fig.
Four studies contained no information on the country in which the restoration project was carried out.
Details are in the caption following the image Figure 1 Open in figure viewer PowerPoint Map of coral reef restoration projects reported in countries with different income categories and Human Development Index (HDI).
Classifications are defined as those with a gross national income (GNI) per capita, calculated using the World Bank Atlas method: low-income economies of 995 US$ or less in 2017; lower middle-income economies with between 996 US$ and 3,895 US$; upper middle-income economies with between 3,896 US$ and 12,055 US$; and high-income economies with 12,056 US$ or more (Source: The World Bank 2019a, 2019b, 2019c).
For all countries, the HDI with time series data from 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2013, 2015, and 2017 are shown.
Categories are 0.354000–0.499999 (very low), 0.500000–0.549999 (low), 0.550000–0.699999 (medium), 0.700000–0.799999 (high), and 0.800000–0.953000 (very high) (Sources: The World Bank, UNDESA, Barro and Lee, UNESCO, UN Statistics Division, UN Population Division, IMF, Census reports (from National Statistical Offices), Eurostat, Secretariat of the Pacific Community, US Census Bureau, Natural Earth).
Reasons for Coral Reef Restoration The dominant primary motivations for the restoration of coral reefs in the restoration projects reviewed were experimental reasons, such as to improve the restoration approach and answer ecological research questions, accounting for 65.3% of the projects (Fig.
A total of 17.3% of the projects carried out coral reef restoration because of an environmental impact such as hurricanes, ship groundings, or heavy storms and were inspired by legislative reasons.
Restoration for biodiversity enhancement (biotic reasons) was the motivation for 10.7% of the projects.
Pragmatic reasons for enhancing ecosystem services such as fisheries production motivated 4.0% of the projects.
Social reasons (idealistic), e.g. restoration for education purposes or awareness of the general public and restoration for biodiversity offsetting (legislative), were negligible (<2.0% of the projects).
The secondary and tertiary motivations, where reported, were dominated by experimental reasons to restore coral reefs (Fig.
Details are in the caption following the image Figure 2 Open in figure viewer PowerPoint Motivations reported for restoring corals reefs categorized as idealistic, experimental, legislative, pragmatic, and biotic (n = 75).
Variables Measured and Reported The majority (70.7%) of projects measured variables relating to ecosystem function (Fig.
3), including survival of restored corals, growth, and productivity (Fig.
This was followed by species composition (25.3%) indicated by metrics such as species present, richness or distribution, and physical conditions (2.7%) e.g. water temperature, salinity, turbidity, and water currents.
The number of projects reporting on social aspects of restoration, such as measuring environmental awareness or community engagement was negligible (1.3%).
Details are in the caption following the image Figure 3 Open in figure viewer PowerPoint Primary categories of variables measured within n = 75 restoration projects.
Details are in the caption following the image Figure 4 Open in figure viewer PowerPoint Word cloud of variables categories that practitioners have measured to report on the outcomes of coral reef restoration (n = 75 restoration projects).
Coral Reef Restoration Outcomes Reported The majority (76.0%) of coral reef restoration projects reported an ecological outcome only (Fig.
Some studies reported on social and ecological outcomes (13.3%), followed by ecological and economic outcomes (8.0%) while the least number of studies reported on all three outcome categories (2.7%).
All projects reported at least an ecological outcome.
Economic outcomes were not reported at all.
Details are in the caption following the image Figure 5 Open in figure viewer PowerPoint Categories of outcome reported and grouped into ecological, social, and economic outcomes (n = 75 restoration projects).
Project Cost, Spatial Extent, Duration, and Survival The median reported cost from all observations (n = 58) was 404,147 ± 18,927,043 US$/ha (at base year 2010), while the project spatial extent (n = 91) was 0.01 ± 0.454 ha (108 ± 4,542 m2) with a survival (n = 288) of 60.9 ± 32.2%, and a project duration (n = 276) of 1.0 ± 1.7 years (all median values ± standard deviation [SD]).
Out of a total of 335 observations, 17.3% (or 29.9% of 87 studies) reported on project cost and 14.3% (or 27.6% of the studies) described what restoration components these costs included.
From all 58 observations (26 studies) reporting on cost, 37.9% of the observations (or 38.5% of the studies) reported on both capital (planning, purchasing, land acquisition, construction, financing) and operating (maintenance, monitoring, and equipment repair/replacement) costs highlighting that the cost values reported here are likely lower than the real total project cost.
Costs, survival rates, and project spatial extent varied substantially among the six restoration techniques (Table 1, Fig.
The median cost for substrate addition − artificial reef were highest with 3,300,000 ± 44,000,000 US$/ha (n = 10; median ± SD; Table 1).
The cheapest restoration technique was the collection and nursery phase component of the coral gardening approach with median cost of 28,000 ± 20,000 US$/ha (n = 5; Table 1) and a survival of 52.1 ± 31.5% (n = 85; Fig.
The variability in cost estimates was large and spanned five orders of magnitude (from 6,000 to 143,000,000 US$/ha) between the different restoration techniques (Table 1).
The five case studies reporting on project duration of substrate stabilization projects lasted longest with 2.0 ± 3.6 years while studies employing artificial reef enhanced by electrical field were of shortest project duration with 0.3 ± 0.3 years (n = 10; Fig.
The techniques of larval enhancement (n = 3) and substrate addition (n = 12) were deployed over the largest spatial extents with median values of 1,500 ± 849 m2 and 2,342 ± 5,270 m2, respectively (Fig.
The 12 observations reporting on the coral gardening approach in its entirety and the six observations on building artificial reefs enhanced by electrical fields were reported for the smallest spatial scales and had median values of 12 ± 3,854 m2 and 5 ± 0 m2 of reef restored, respectively (Fig.
Because the area of coral reef that is ultimately restored depends on the restoration schedule and is not directly related to the spatial area covered by a coral nursery, our reported observations on the collection and nursery phase of the coral gardening approach do not contain area estimates (Fig.
Range of cost (2010 US$/ha) for coral reef restoration observations with sample size (n), minimum, median, maximum, and standard deviation (SD).
Cost converted based on consumer price index to a base year of 2010 prices.
Restoration Cost (2010 US$/ha) Restoration Technique	n	Median (±SD)	Minimum	Maximum 1.
Direct transplantation	20	 218,305  (±2,339,609)  9,198	8,382,653 2.
Larval enhancement	6	 523,162  (±1,878,894)  6,262	4,333,826 3.
Coral gardening (overall)	3	 351,661  (±136,601)  130,000	379,139 a.
Collection & nursery phase	5	 28,075  (±20,472)  9,262	56,150 b.
Transplantation phase	2	 761,864  (±1,033,831)  30,835	1,492,893 4.
Enhancing artificial substrates with an electrical field	0			 5.
Substrate addition (artificial reef)	10	 3,341,754  (±44,100,144)  14,076	142,667,803 6.
Substrate stabilization	8	 370,986  (±9,040,923)  91,044	26,100,000 Details are in the caption following the image Figure 6 Open in figure viewer PowerPoint Range of costs (A), survival of restored corals (B), project duration (C), and spatial extent of area restored (D) reported for coral reef restoration observations (n = 335) categorized by restoration methods and represented as box and whisker plots with sample size (n), minimum, quartiles, median, maximum, and outliers.
Restoration cost (US$/ha at 2010) are displayed on a logarithmic scale.
The median reported cost from all observations (n = 59) using the gross domestic product as a function of purchasing power parity GDP (PPP) was 72,861 ± 18,810,155 Int$/ha (at base year 2010).
Cost in Int$/ha for the different coral reef restoration techniques are shown in Table 2.
Range of cost (Int$2010/ha) for coral reef restoration observations with sample size (n), minimum, median, maximum, and standard deviation (SD).
Cost converted based on the gross domestic product as a function of purchasing power parity.
Restoration Cost (2010 Int$/ha) Restoration Technique	n	Median (±SD)	Minimum	Maximum 1.
Direct transplantation	21	 37,154  (±1,571,433)  425	5,166,146 2.
Larval enhancement	5	 427,607  (±751,925)  2,020	1,850,727 3.
Coral gardening (overall)	3	 91,778  (±17,651)  72,861	108,133 a.
Collection and nursery phase	5	 5,730  (±14,186)  2,041	36,314 b.
Transplantation phase	2	 336,835  (±474,510)  1,306	672,364 4.
Enhancing artificial substrates with an electrical field	0			 5.
Substrate addition (artificial reef)	10	 914,755  (±44,331,070)  4,078	142,667,803 6.
Substrate stabilization	8	 44,834  (±9,196,689)  7,995	26,100,000 Motivations for coral reef restoration differed between cost ranges.
We separated the 27 observations from studies that reported both on motivations and cost into ranges of (1) <100,000 US$/ha, (2) between 100,000 and <1,000,000 US$/ha, and (3) >1,000,000 US$/ha.
The primary motivation for (1) was to improve the restoration approach and answer ecological research questions (9 out of 12 observations).
For (2) motivations covered biodiversity enhancement (n = 1), biodiversity offset (n = 1), improve restoration approach (n = 2), and restoration after environmental impact (n = 2).
For (3) motivations were biodiversity enhancement (n = 1), improve restoration approach (n = 3), and restoration after environmental impact (n = 5).
Discussion Here we present information on the most commonly applied coral reef procedures from published literature for which motivations, variables measured, cost, success, project spatial extent, and duration have been reported.
The techniques described here are not exhaustive (e.g. the method of micro-fragmentation [Forsman et al.
2015; Page et al.
2018] has not been considered), but are in broad agreement with those described by the coral reef restoration review by the Australian Reef Restoration and Adaptation Program (Boström-Einarsson et al.
Coral gardening is among the most commonly used methods to restore coral reefs and consists of two subsequent phases (Rinkevich 1995, 2000, 2005, 2008, 2014).
However, few studies report on the whole process from harvesting coral fragments from donor colonies, growing them in intermediate nurseries to outplanting corals to the degraded reef.
Therefore, we report on the overall approach and on each phase individually.
The coral reef restoration projects assessed in this study are dominated by experimental motivations inspired by improving restoration approaches and answering questions of ecological concern.
Our findings suggest that there is still ongoing development in the methods used to restore coral reefs.
However, given that those charged with the task of carrying out large-scale coral reef restoration may rarely publish restoration results and most studies in the literature examined here were conducted by academics, we may be missing a substantial body of knowledge related to coral reef restoration.
Bridging the divide between academic researchers and practitioners is a challenge in many conservation fields (Sunderland et al.
2009; Milner-Gulland et al.
2010); doing so will help advance the field of marine restoration ecology.
The majority (71%) of restoration projects in this review measured variables which can partly inform on ecosystem function (Fig.
3) such as survival of restored corals, growth, and productivity.
This concurs with Hein et al.
(2017) who described that 88% of studies in the published literature measured survival and/or growth of restored corals as an indicator of coral reef restoration effectiveness.
In comparison, a study on terrestrial restoration suggested that measurement of at least diversity, vegetation structure, and ecological processes would be necessary to assess the long-term persistence of an ecosystem (Ruiz-Jaen & Mitchell Aide 2005).
It is questionable whether measuring item-based success indicators such as survival of restored organisms will be able to provide any information about the holistic ecological perspective of restoring ecosystem function and services.
Although many studies (Yap 2000; Van Diggelen et al.
2001; Epstein et al.
2003; Hernández-Delgado et al.
2014) recommend the assessment of social, economic, and cultural factors when assessing the effectiveness of coral reef restoration, this study confirms that the numbers of studies assessing social or economic factors have been negligible or are not existent.
Reported coral reef restoration outcomes in this study were largely ecological (76%) and rarely focused on economic (e.g. job creation, obtaining higher fishing yields) or social aspects (community involvement, awareness, and environmental education) of the restoration project.
This is in agreement with the study by Wortley et al.
(2013) showing that over 90% of the ecological restoration projects spanning many terrestrial ecosystems and as reviewed from the scientific literature reported on ecological attributes while only 1% reported on social, economic, and ecological attributes altogether.
This may reflect the relatively recent history of coral reef restoration and the small scale of the projects.
There is a need to assess variables related to ecosystem services provided by the restoration of coral reefs which have positive economic impacts.
Future restoration projects could make this a priority, particularly if social and economic outcomes (e.g. environmental education, changes in perception/behavior due to awareness, community empowerment and stewardship, creation of jobs, capitalization of ecosystem services such as tourism, fisheries, coastal protection, etc.) are used as justification for these projects.
Our review of published scientific literature, reports and other available sources shows a large variation in cost reported for the different techniques used in coral reef restoration.
While the median reported cost over all observations is around 400,000 US$ to restore 1 ha of coral reef habitat, costs reported for the techniques most commonly applied ranged between 6,000 and 4,000,000 US$/ha.
Because coral reef restoration studies rarely report on cost in a consistent manner, it is important to note that the values provided here are estimates only.
Reporting on the total cost of coral reef restoration projects can be challenging.
This is especially true because not all restoration projects are carried out for the same reasons or have the same specific objectives.
For costs that have been reported, there is a large variation within and between intervention type, location, and study species.
Estimates of total restoration cost (including both capital and operation costs to account for the different components of a restoration project) require a standardized approach when reporting on cost.
Similar issues with extracting restoration costs from the literature were also noted for other marine coastal ecosystems, e.g. seagrass, mangroves, saltmarsh, and shellfish (Bayraktarov et al.
Coral reefs, as particularly charismatic ecosystems, attract volunteers willing to participate in the restoration work which adds to the difficulty to account for the real cost of labor.
A productive approach for further work would be to design a survey to elicit information from coral reef restoration practitioners to collate total restoration costs in a standardized way.
Ideally, guidelines for standardized reporting on costs for management interventions need to be followed (e.g. by Iacona et al.
2018) in order to compare restoration to other conservation interventions.
Survival of restored organisms is often reported as an item-based success indicator by studies on marine coastal restoration (Bayraktarov et al.
Here, survival differed between the life stages of corals at which the restoration technique is targeted, with high survival rates (>50%) for coral gardening and low survival rates (<25%) where techniques are focused on coral larvae.
Yet, survival has been assessed only in the short term (1–2 years after restoration) and the number of long-term studies such as Haisfield et al.
(2010) and Garrison & Ward (2012) is small.
Previous work has highlighted that survival of restored organisms is not a good indicator for the overall project success (Bayraktarov et al.
2016) because of the different life histories among species and lack of standardization between restoration projects.
In addition, coral reef restoration literature is likely biased toward studies reporting on success (Bayraktarov et al.
2016), while only a few studies have described failures (e.g. Fox 2004; Fadli et al.
2012; Cooper et al.
Here we propose an avenue toward setting clear objectives and quantifying success in achieving those objectives.
Ideally, overall restoration project success should be measured as progress toward the specific project objectives.
These should be specific, measurable, achievable, realistic, and time-bound (SMART) (McDonald et al.
At least one of the objectives should aim at returning the ecosystem function and resilience of an ecosystem through restoration (Ruiz-Jaen & Mitchell Aide 2005).
The project would also need to account for the effect of environmental stochasticity (extreme events such as floods, heat waves, hurricanes), which is why the selection of the site for restoration is critical.
Of equal importance are social factors related to whether local communities will adopt and maintain the restored ecosystem—thus an early involvement of local stakeholders is crucial for overall restoration success into the future (McDonald et al.
The fact that biological responses to the restoration intervention such as survival together with growth and productivity continue to be the dominant variables measured, as we report in this review, may indicate that coral reef restoration is still at an early phase (Hein et al.
With a median restored area of 0.01 ha (108 m2) coral reef restoration reviewed here has been mainly practiced on small, experimental scales.
However, restoring corals at larger scales is possible (e.g. 0.52 ha and 0.15 ha; Montoya-Maya et al.
2016; Chamberland et al.
Because studies in this article are mainly research-based, they have inherent limitations such as the period of funding.
This may be one of the reasons why the projects reported here tend to be relatively short and over small experimental scales.
For instance, a review that evaluated non-peer-reviewed sources and surveyed practitioners reported a median restored area of 300 m2 (Boström-Einarsson et al.
2018) in comparison to the 108 m2 reported here.
This gap may be closed by gathering data from those charged with the task of carrying out large-scale coral reef restoration by either a survey or other means.
Implications for Practice Coral reef restoration has been practiced at small experimental scales while a transition to large, whole reef system scales is poised to occur.
Innovation enabling coral reef restoration at an industrial scale is already happening by harvesting wild coral spawn slicks (Doropoulos et al.
2019) and employing assisted evolution to make restored corals resilient to climate change (van Oppen et al.
A fast advancement of coral reef restoration is driven by international agreements toward restoration such as the Aichi Biodiversity Target 15 and Sustainable Development Goals by the Convention on Biological Diversity, The Bonn Challenge, or the recently announced United Nations 2021–2030 Decade on Ecosystem Restoration.
These agreements stimulate increased funding for restoration.
In Australia for example, funding of AUD100 million has been recently allocated toward the research and development phase of the Reef Restoration and Adaptation Plan, which aims to develop, trial, and deploy coral reef restoration interventions for the Great Barrier Reef (GBR) (https://www.gbrrestoration.org/the-program).
While being a substantial investment, this amount of funding may appear rather small when taking into account the size of the GBR (35 million hectares) and the median cost of 400,000 US$ to restore 1 ha of coral reef as we found from the published literature.
Although this figure may discourage in a first instance, the range of costs observed in this study differs by orders of magnitude for different restoration techniques, which represents an important source of information for the coral restoration community and could be used to target future provision of limited funds.
Further research and development in the coral restoration space should focus on interventions that are both inexpensive and successful.
A wide range of costs within intervention categories offers hope for future minimizing of costs to a level where restoration projects can become achievable at scale.
This review reveals that there is a large variability in the cost reported for different coral reef restoration techniques from the primary literature, reports, and published data repositories.
These cost ranged from a median value of 28,000 US$/ha for the collection and nursery phase of the coral gardening approach to 4,000,000 US$/ha for substrate addition to build an artificial reef.
Cost values were relative estimates only and did not always report on the total project cost.
Survival of restored corals, often reported as the major variable monitored, ranged between 17.3% and 77.5%, depended on the life history that the technique targeted, and was largely documented for short time frames only (1–2 years after restoration).
Most published projects were motivated by the desire to elicit experimental data for the purpose of increasing our knowledge or improving the methodological approach and reported an ecological outcome while social and economic aspects of the restoration were rarely assessed.
Published literature may be biased toward experimental small-scale restoration projects carried out by academics while large-scale projects by restoration practitioners may not be captured—this remains to be assessed and is an important area of future research.
A comparison of costs and success between the interventions used in coral reef restoration could be enabled by reaching out to those charged with the implementation of coral reef restoration projects and eliciting their knowledge through a survey on cost and success.
Abstract Coral reefs are widely recognized for concentration of biological activity, fisheries and tourism, coastal protection, geological processes, and aesthetic wonder.
A principal cause of reef damage in Florida is ships running into reefs.
The other major human impact on Florida’s reefs is dredging for beach renourishment and channel maintenance.
In response to chronic reef damage, federal and state agencies and consultants have developed techniques to restore, as best possible, reefs impacted by human disturbance.
These efforts include salvaging sponges and corals, removing loose debris from the reef, rebuilding three-dimensional (3-D) structures onto leveled-scarified reef surfaces, and transplanting sponges and corals back on the cleared reef surfaces.
This paper presents an overview of restoration approaches; a discussion on legal and administration to both damage and restoration of these essential fish habitats; a brief review of some case studies; and a discussion of restoration success criteria.
Salvage of corals and sponges is critical to the success of any reef restoration effort.
If a living surface is allowed to sit on the sand for a few days, that surface will die.
Often the grounded vessel will have crushed the reef, excavating sediments and rubble that end up as a berm of material behind the ship’s resting position.
Dealing with massive amounts of rubble debris is challenging.
The options include leaving it in place and stabilizing it with cements; moving it a long way from the site and dumping it in deep water; or reconfiguring it by moving it off reef and building piles where it can do no harm.
After the debris is moved off the reef platform, corals and other sessile benthic organisms (salvaged resources) can be transplanted on the damaged area.
Monitoring is important to determine the success of the restoration and to look for ways to improve future projects.
Sampling sites for monitoring should include restored areas plus a reference area (undamaged habitat of a relatively similar nature that is in close proximity) for comparison.
The following questions should be addressed for any reef restoration project: are the transplanted organisms still secured to the reef?
Is the vitality (color, disease, algal competition) of the transplanted organisms equivalent to the organisms in the reference sites?
Is recruitment (settlement of juvenile organisms) similar in the restored areas and the reference areas?
Monitoring should be tied to decision making so corrections can be made.
Previous article in issue Next article in issue Keywords Coral reefRestorationBiological activity 1.
Introduction Coral reefs are deterministic phenomena of sedentary organisms with high metabolism living in warm marine waters within the zone of strong illumination.
They are constructional physiographic features of tropical seas consisting fundamentally of a rigid calcareous framework made up mainly of the interlocked and encrusting skeletons of reef building corals and calcareous red algae’ (Wells, 1957).
Coral reefs are found throughout the world in a band that is generally bounded by the Tropics of Cancer and Capricorn.
Individual coral species grow at rates that range from about 1 to 10 cm annually.
Overall, coral reef growth is slow, ranging from about 1 to 5 m per 1000 years.
Coral reefs are widely recognized as significant habitat providing structural heterogeneity and serve as refuge for a multitude of sessile and mobile organisms.
Coral reefs have high gross primary productivity; however, net primary productivity is not great (Sournia, 1977, Gladfelter, 1985).
Unlike most ecosystems, the primary producer is not a stand-alone autotroph; instead, a symbiotic complex of microscopic algae (zooxanthellae) living within the tissues of sponges and Cnidarians (corals, anemones, zooanthids) contribute a significant portion of the fixed carbon.
Reef structures are impressive natural breakwaters; they dissipate prodigious wave forces that strike their frontal masses.
This protects low-lying coastal areas that would otherwise experience severe flooding during tropical cyclones or major frontal storms if the coral reef barrier were not present.
Coral reefs exhibit high biological diversity and concentrated biomass within the benthic communities.
They are characterized as unpredictable communities (Slobodkin and Sanders, 1969, Connell, 1997), and their biological diversity is maintained by intermediate magnitude and frequency disturbance (Connell, 1978, Done, 1997).
Coral reefs are often characterized as an underwater tropical rain forest: high biodiversity, rapid nutrient recycling, many forms of symbiosis, and layered structure of canopy, under-story, and surface (Hubbell, 1997).
The upper reef layer is composed of large branching or massive corals that rise above the reef framework; there is an intermediate layer of moderate-sized corals, sea fans, sea whips, and sponges; and at the sea floor level, algae and small sessile invertebrates dominate.
Beneath the surface, there are caverns providing niches for cryptic organisms.
As with the situation in an old growth forest, older corals are often partially deceased, and the non-living surface areas are covered with many different kinds of plants and animals.
Coral skeletons are often excavated by algae, fungi, sponges, mollusks, and other organisms, generating a labyrinth of tunnels.
Sponges also provide a refuge for smaller crustaceans, polychaeates, and even fish.
Coral reefs have resident, semi-resident, and seasonally resident mobile species, especially fish.
In the last 20 years, the popularity of coral reef tourism has surpassed the economic benefit derived from coral reef fisheries, and the term ‘eco-tourism’ has been adopted to describe the activity of visiting unique natural areas to enjoy the setting and to observe the flora and fauna.
Coral reefs are a major destination for eco-tourists, especially Australia’s Great Barrier Reef, Micronesia, French Polynesia, the Greater and Lesser Antilles, Central America, the Bahamas, and the Florida Keys.
The opulent diversity in color, form, and texture on coral reefs has immense appeal to the viewers of natural history television programs.
Dissemination of this information has resulted in greater social awareness of coral reef problems and conservation.
‘The Year of the Reef’ occurred in 1996 and conservation groups throughout the world focused attention on coral reefs and their problems.
National and international coral reef initiatives have come into being to help conserve coral reef resources (McManus and Chua, 1990, Wilkinson et al., 1997).
Resource damage The principal natural events that physically restructure coral reefs include tropical cyclones (hurricanes and typhoons), earthquakes, and lava flows.
The magnitude of the change is proportional to the strength and duration of the event.
A reef exposed to a class five hurricane may be totally destroyed as a high profile coral reef, for example, Hurricane Hattie in Belize and Hurricane Allen in Jamaica wrought havoc and virtually destroyed reefs (Stoddart, 1962, Woodley et al., 1981).
Smaller storms and large storms that do not linger are less destructive; for example, Hurricanes Donna and Betsy (1960 and 1964) damaged coral reefs off the Florida Keys; but reefs recovered within ten years (Springer and McErlean, 1962, Shinn, 1976).
Winter frontal passages in high latitude reef systems can stress the biota by chilling waters to sub-lethal and lethal temperatures (about 14°C) (Davis, 1982, Porter et al., 1982, Roberts et al., 1982).
Summer doldrums associated with ENSO phenomena stress flora and fauna because of elevated sea water temperatures (about 30–32°C) causing mass coral bleaching where the zooxanthellate organisms lose their algal symbionts and appear stark white (Jaap, 1979, Jaap, 1985).
Anthropogenic, physically destructive activity impacting coral reefs includes dredging channels and harbors, dredge mining sand for beach renourishment, vessel groundings, and anchoring on coral reefs.
Any of these incidents may fundamentally change a reef or a portion of a reef.
Dredging impacts typically involve a dredge cutter head running into the reef, ground tackle and pipes from the dredge damaging the reef, and dredge materials being dumped on the reef.
In addition, dredging creates chronic high levels of turbidity which can destroy corals from lack of light and sediment smothering (Courtenay et al., 1974, Dodge and Vaisnys, 1977, Salvat, 1987, Rogers, 1990, Lindeman and Snyder, in press).
Ship groundings (Fig.
1) on coral reefs have occurred ever since humans first built boats and began going to sea.
The ship’s impact can dislodge and fracture corals (Fig.
2), pulverize coral skeletons into small debris-rubble, displace sediment deposits, and destroy or fracture the reef platform.
Salvage operations often add damage due to inappropriate methods and poor control of operations.
In some cases, the ship’s hull is ruptured and cargo and fuel are spilled on the reef.
Download: Download full-size image Fig.
R/V Columbus Iselin aground on Looe Key, August 10, 1994.
Photo credit: G.
Download: Download full-size image Fig.
Damaged coral, The hull of the Container Ship Houston, January, 1997, off Maryland Shoal, Florida Keys, cleaved the top off this boulder-brain coral, Colpophyllia natans (Houttyn).
Photo credit: W.
Large ship groundings cause fundamental changes in community structure (Table 1).
Small boat groundings (vessels <100 ft [30 m] long) are chronic in many areas.
In the Florida Keys, ≈500 small vessel groundings are reported annually; however, we estimate at least two to three times that number go unreported.
Patch reefs in the Mosquito Banks area, Key Largo have experienced decline in coral cover as a result of numerous small boat groundings.
Resource losses, Looe Key, Columbus Iselin grounding, survey, 21–23 September 1994a  Sampling site:	East area	West area	Grounding scar No. of Samples (one m2 quadrats)	36	29	34 No. of Cnidaria species	19	15	2 Mean species/m2 (X±S)	3.50±1.36	3.62±1.62	0.09±0.37 No. of Cnidaria colonies	976	536	14 Mean colonies/m2 (X±S)	26.86±26.03	18.48±10.94	0.41±2.20 Shannon Weiner, H’n, Cnidaria (log 2)	1.69	1.54	0.94 Evenness, J’n	0.40	0.54	0.94 Estimated loss of colonies			7977 a Sampling included quadrat census the damage area and two reference sites in the adjacent area.
Anchor damages occur in many areas.
The size of the anchor, weather, and frequency of anchoring are directly related to the magnitude of the damages.
In most tourist areas, chronic anchor damage to coral reefs has been mitigated by installing special moorings that eliminate the need to anchor on the reef by allowing the dive boat to moor to a buoy (Halas, 1985, Halas, 1997).
Fishing fleets that anchor in the same area for relief from adverse weather can cause major impact (Davis, 1977).
In areas where large ships anchor on coral reefs, the damages are significant (Smith, 1988; Fig.
Trawling or deploying other types of fishing gear can be harmful to coral reefs.
The trawls can dislodge and abrade corals.
Destructive fishing practices on coral reefs, in some parts of the world, include dynamite fishing and using toxic chemicals such as sodium hypochlorite and sodium cyanide to harvest fish and invertebrates (Alcala and Gomez, 1987, Eldredge, 1987).
Download: Download full-size image Fig.
Large ship anchor chain and coral damage, Tortugas Banks.
Photo credit: G.
Natural recovery processes Following a major disturbance on a coral reef, natural recovery originates with algae recruitment into the scarified areas.
Typically brown, cyanobacteria (bluegreen), and some green algae are the initial colonizers.
Clarke and Edwards (1994) reported that concrete structures deployed on degraded reef flats in the Maldives recruited green algae in 7 days, barnacles in 14 days, and stony corals in 6.5 months.
The local setting will have significant influence on the rate of recovery.
After 1 or 2 years, crustose coralline algae, sponges, octocorals, zooanthids, and pioneering stony corals begin to settle and exploit the open space.
Pioneering corals such as the Octocoral genus Pseudopterogorgia and the stony coral Favia fragum recruit and start to grow.
After 8 to 10 years an area will have a high density of sponges and octocorals with a moderate density of pioneering stony corals: Agaricia agaricites, Porites porites, Porites astreoides, Favia fragum, and Colpophyllia natans.
Because octocorals recruit and grow at a relatively rapid rate, they may recover to pre-disturbance population densities in 10–15 years.
Stony corals recruit and grow at a much slower rate than the octocorals, and their recovery may require several decades to a century.
Two corals (Acropora palmata and Montastraea annularis) have been documented as the principal reef framework builders in the Florida and many parts of the Caribbean (Shinn et al., 1977).
In Florida, Acropora palmata has an average annual growth rate of 72.5 mm, while M.
annularis has an annual growth rate of 7.3 mm (Fig.
Coral reef growth rate in the Florida Keys reefs is 0.65–4.85 m per 1000 years (Shinn et al., 1977).
Because reef recovery and growth rate is slow even under optimal conditions, restoration actions that will enhance recovery are beneficial.
Download: Download full-size image Fig.
Coral and reef growth, Florida Keys reefs.
Reef growth based on (Shinn et al.
(1977), coral growth based on Vaughan (1916), Hoffmeister and Multer (1964), Jaap (1974), Shinn (1976), and Hudson (1981).
In the coral growth rate, the assumptions include constant growth, no predation, no competition, and no disturbance.
Download: Download full-size image Fig.
Lift bag, moving large boulders, Maasdam restoration, Soto’s Reef, George Town, Grand Cayman, British West Indies.
Photo credit: T.
An unstable substrate and associated poor water quality will retard recovery.
The rubble is dynamic; it will move as a result of storms and strong currents, and fine fraction sediments will be re-suspended during storms.
This reduces water clarity and creates stress for autotrophic organisms (Hubbard, 1973).
Initial coral settlement may occur but survival is poor.
Juvenile corals can be buried or turned over, leaving them in an unfavorable situation.
Predator pressure may be concentrated on the few surviving adults and juveniles (Knowlton et al., 1981).
It is impossible to precisely predict the time required for population and community recovery to the pre-disturbance condition.
Most evaluations have documented at least a decade for recovery following moderate disturbance events (Pearson, 1981, Sheppard, 1982, Connell et al., 1997).
Restoration actions The single most important action in coral reef restoration is the rescue of damaged resources as rapidly as possible by placing them in a safe location until there is an opportunity to transplant them back on the reef.
After a ship runs aground on a reef, it may remain there for days until it is pulled from the reef.
During this time, the major effort on the part of the trustee [government agency(ies) that has jurisdiction] is to conduct a preliminary damage survey and to provide a triage for damaged benthic resources.
This includes righting overturned corals and salvaging broken pieces of coral and caching them into safe areas for temporary storage.
For large formations, lift bags (Fig.
8) and portable winches have proven to be an effective means to move large boulders.
Plastic milk crates work well for temporary storage of smaller coral pieces and can be moved by two divers.
This work is labor-intensive, and, in a large grounding, it might require 2000–3000 h of labor to sort through the debris field.
Once the vessel is moved off the reef, the triage salvage continues, while a restoration plan is developed.
If the responsible party [ship owner(s) and insurance company(ies)] agrees to accept responsibility, a contractor may be hired to execute the restoration.
Removing and/or stabilizing loose debris Initially, the biggest challenge is determining an expedient way to manage loose debris.
Solutions include removing it, stabilizing it with mortar, or capping it with boulders or cement structures.
Barging the material off-site is expensive and requires state and federal permits.
Divers can transport the material from the site, deposit the material in an area that is sand or rubble bottom, and build artificial reefs with piles of debris.
Rubble is often concentrated in piles or berms on the reef and it can be maintained in that configuration, using cement to hold the mass together.
Hudson and Diaz (1988) used Portland cement to stabilize an area at Molasses Reef following the Wellwood grounding in 1984.
Limestone boulders, 3–4 ft in diameter, can be barged to the site and lowered to the rubble field with a crane.
These boulders, which can be placed either in piles or in a layer to cover the area, will help stabilize the rubble surface and keep it from moving.
The boulders provide 3-D structural replacement, and gaps between them provide refuge sites for mobile fauna.
Additionally, the boulders recruit algae, sponges, octocorals, and stony corals.
A method infrequently used to stabilize loose rubble is an articulated concrete mat that was originally designed to reduce soil erosion along the interstate highway system.
The mats are constructed in an open web of cement blocks connected with mylar cables.
They were first deployed to stabilize rubble on a reef flat in the Maldives (Brown and Dunne, 1988, Clarke and Edwards, 1994) and subsequently were deployed at the Houston grounding site (1998) off Maryland Shoal in the Florida Keys.
Mat survivability in hurricanes is moderate.
We found some movement and cable fracture following Hurricane Georges passage at the Houston site.
If the debris is in an area with strong currents and wave surge, it may be advisable to remove the material and take it to an area where it can cause no harm (upland or in deep water).
Structual reconstruction Damages that destroy 3-D relief or severely crack open the reef platform should be repaired and/or replacement modules should be installed.
When large formations are dislodged or turned upside down, consideration should be given to recover these resources and move them back to their approximate, former location.
Caution must be exercised to avoid human injury and further reef damage.
Large structures can be manipulated with multiple lift bags and secured by cement and steel reinforcement rods.
If the damage pulverized 3-D relief, new structures can be fabricated from limestone and/or cement.
The types employed in Florida include molded cement structures, large limestone boulders, and cement materials in combination with natural rock.
(1989) tested a concrete hemisphere, the size and shape of which mimicked moderate-sized boulder and brain corals (≈2–3 ft [0.6–0.9 m] in diameter) with a hollow interior designed as refuge habitat for mobile organisms.
The hemispheres were first deployed off Elliott Key, Biscayne National Park, in 1977, where they have remained in place and recruited an impressive sessile community.
In 1989 the census enumerated: 89 octocoral colonies (15 species) and 45 stony coral colonies (7 species).
Recent improvements to this design include additional openings for improved internal water circulation and limestone rock embedded in the concrete to add rough texture.
Limestone boulders 3–4 ft (0.9–1 m) in diameter and built up in two to three layers on a concrete base, and held together with cement and steel have been successfully deployed off Sunny Isles, Dade County, Florida (Selby and Associates, 1992).
These modules were barged to the dredge damage site and installed with a crane, and have remained stable through a major hurricane, Andrew.
They provide relief that is natural looking as well as refuge areas for large and small mobile organisms.
Another method employed off Dade County was the use of large-diameter concrete culvert pipe.
The pipe’s outer surface was covered with cement and limestone rocks and holes were struck through the culvert to provide better circulation and egress.
At Looe Key, a spur was reconstructed using cement and limestone rock.
Steel and cement will be used to strengthen the reef platform that was severely cracked from the grounding of the nuclear submarine Memphis.
Transplanting sponges and corals Transplanting should be considered in coral reef restoration to benefit recruitment, accelerate recovery, and improve the visual perspective.
Barren areas have low natural recruitment (personal observation).
Experiments done on the Mavro Vetranic, Pulaski Shoal, Dry Tortugas grounding site imply that recruitment of stony corals into barren zones is very low.
Recruitment is, for the most part, from local populations, and large barren areas do not have a local population to produce progeny, and chemical signals that trigger larval settlement may be missing in the barren area.
Transplanting has received little systematic evaluating until recently.
Harriott and Fisk (1988) summarized the results of five transplanting studies dating from 1974 to 1988; survival of the transplanted corals ranged from 0 to 100%.
Success or failure was dependent upon the species, environmental conditions, type and shape of transplants, and if the transplants were attached to the substrate or not.
Those sponges, corals, and coral fragments that were salvaged and set aside should be the first candidates for transplanting following debris cleanup.
Transplant methods include throwing (sowing) bits and pieces into the damaged area or securing individual pieces or whole organisms to the reef platform with cement, epoxy, hardware (such as stainless threaded rod), or cable ties.
Sponges and octocorals (sea fans, sea grounding site whips, and sea plumes) should be transplanted intact with a portion of rock to which they are attached.
At the turn of the century, Vaughan (1916) used cement to attach stony corals to small pillars at Dry Tortugas, Florida, and Goulding Cay, Bahamas, for growth rate experiments.
The method had minimal impact on the individual corals, and Vaughan’s growth rate results are frequently referenced.
A method used to cement corals back on a reef starts with one to four liters of Portland type II mortar mix (Neeley, 1988).
The mixed mortar is put in a watertight container (plastic bag, a bowl with a sealed top, or a length of sealed PVC pipe).
A diver swims the cement to the work site, or it can be sent to the bottom on a line.
The surface area is cleaned, all or part of the mortar is used to build a mound of cement on the reef platform, the coral, sponge or octocoral is inserted into the cement mound, and the diver works the cement around the edges of the transplanted organism (Fig.
If the area experiences currents and wave surge, soft dive weights or a sand bag can be placed around the base of the organisms to stabilize the transplant while the cement hardens.
Adding moulding plaster to the cement during the mixing will speed the cement curing time.
However, care must be exercised, since the plaster is chemically reactive and causes the cement mixture to become hot.
The mixer and diver should wear rubber gloves to protect their hands.
Commercial products such as Water Plug™ will also set up rapidly.
Cement will dissolve underwater, leaving grey silt on the bottom.
Placing soft dive weights around the base of the cemented organisms and fanning the area removes residue from the sea floor.
Download: Download full-size image Fig.
Corals cemented to reef platform following the M/V Mavro Vetranic accident, Pulaski Shoal, Dry Tortugas, Florida, October, 1989.
A mass of mortar was laid down and the corals were set into it.
Photo credit: W.
Marine epoxy works well to reattach small to medium-sized organisms back on the reef platform.
Liquid Rock 500 epoxy and hardener are dispensed from twin tubes placed in an applicator with a nozzle containing internal mixing spirals (Fig.
The surface must be cleaned with a wire brush.
If the organism is going to be transplanted on a vertical surface, a small hole is drilled into the reef surface, the back of the coral, and a small brass or stainless rod is fitted into the hole in the coral.
Epoxy is applied to back of the coral and the rod.
The coral and rod are placed on the reef surface with special care so that the rod is inserted into the holes.
Download: Download full-size image Fig.
Using epoxy to attach corals back on the reef platform, Maasdam restoration, Soto’s Reef, Grand Cayman, British West Indies, February, 1996.
The epoxy is Liquid Rock 500™, the diver is dispensing a small mass of epoxy, a moderate size coral is then inserted into the mass.
Photo credit: T.
Organization is important to ensure efficiency.
Transplant candidates should be transported from their storage cache and placed near where they will be transplanted.
The work team should understand their tasks and should have a set of communication signals.
A rope and buoy can be used to signal topside when to send cement to the bottom.
The transport of the cement from the boat to the sea-floor can be done with a rope to avoid risk (multiple ascents and descents) to divers.
Branching corals grow faster and weigh less than equivalent sized massive corals and frequently recruit by fragments that break, become lodged in the reef, fuse to the reef surface, and may grow into mature corals.
Cement, epoxy, corrosion-resistant hardware, and plastic cable ties have been used to secure coral branches on reefs.
Loose branch fragments may fuse to the reef without securing them.
Sponges, octocorals, and other sessile benthic organisms should be transplanted by transplanting the rock to which they are attached.
Because demosponges, the most common type of sponge found on shallow-water coral reefs, are soft bodied, they cannot be directly transplanted.
Octocorals are flexible and some species (Eunicea spp) are quite sensitive to Portland cement.
Recent technological advances The process of repopulating an area with organisms is time-consuming and expensive.
At the present time, growing stocks of sponges and corals for restoring damaged habitat is in its infancy.
There has been limited success growing corals in closed systems, proving that it can be feasible to rescue small fragments of corals and sponges and transfer them to closed or open system aquaria or a protected ocean area to grow and be available for restoration projects and experiments.
Currently, the donor stocks are harvested from a nearby site and used to rehabilitate a damaged site.
In several cases federal and state agencies have rescued corals from areas about to be impacted by dredging and moved the corals to safe offshore areas (Bouchon et al., 1981).
Researchers at the University of Guam collected gravid corals from a nearby reef, brought the corals into their laboratory, and maintained the individuals under nominal environmental conditions until they spawned (Richmond, 1995).
Larvae were nurtured in the laboratory until they matured and were ready to settle.
The larvae were taken to a reef that had suffered typhoon damage and released.
The experiment concluded that many larvae settled and grew.
Retention structures can be temporarily placed on the reef and the larvae are placed within the structures to maximize settlement.
(1994) and Morse and Morse (1996) isolated the chemical glycosaminoglycan (a sulfated polysaccharide) from a coralline algae (Hydrolithon boergesenii) that signals Agaricia agaricites hummlis larvae to settle.
The synthesized material, called ‘coral flypaper,’ has proved effective for attracting larvae.
Presumably chemical signals for other species can be isolated and synthesized to develop other larval settlement stimulators.
Littler and Littler (1995) demonstrated that the Caribbean coralline alga Porolithon pachydermum had accelerated growth when grazed upon by the chiton Choneplax lata.
The chiton also grazes on the macro-benthic algae.
Experiments should be undertaken to see if seeding a disturbed area with C.
lata would reduce macro frondose algae, stimulate coralline algae growth, and enhance coral settlement.
If so, this is another method to speed recovery.
Moderate to dense cover of fleshy-benthic algae is a deterrent to coral recruitment.
The major grazing animal on the reef was the black, spiny sea urchin (Diadema antillarum); however an epidemic resulted in a population collapse in 1983 (Lessios et al., 1984).
A damaged reef could be rejuvenated by culturing Diadema, putting them on the damaged site, and allowing them to graze the algae away (Sammarco, 1980).
A pilot study to look at rearing Diadema is underway.
Although the technique has merit, it requires complex timing and coordination.
Mitigation In some incidents, it may be virtually impossible to execute restoration on-site, because the accident occurred in an area that is virtually inaccessible, the wave surge is always present and impossible to work in, or the depths are so deep that it is impossible to conduct safe diving operations.
Appropriate alternatives to restoration include improving aids to navigation, public education programs, and restoration on orphan sites (an area where an accident occurred and the responsible party had no assets to make restitution) in the adjacent area and research in restoration and monitoring.
Administrative and legal issues In state waters, the Florida Department of Environmental Protection (FDEP) is the designated trustee.
Southwest of Miami, jurisdiction is complicated (Table 2) by federal parks, wildlife refuges, state parks, aquatic preserves, and the Florida Keys National Marine Sanctuary (FKNMS).
For example, in Dry Tortugas National Park, the seafloor jurisdiction is totally retained by Florida, while in Biscayne National Park, the jurisdiction is totally under federal authority.
The largest reef area (FKNMS) is under joint federal and state jurisdiction.
Coral reef trustee jurisdictional responsibilities  Area	State of Florida Department of Environment and Protection	Department of Interior	NOAA — National Marine Sanctuary	NOAA — NMFS Magnuson Act State waters	XXX			 Federal parks	XXX	XXX		 Fed.
wildlife refuges		XXX		 Federal waters				XXX Fla.
Keys National Marine Sanctuary	XXX		XXX	 Until recently, the typical large-ship grounding in FKNMS was pursued legally.
The vessel was impounded and a bond was received.
An injury survey with accompanying damages based on economic models (market value, lost use, or habitat equivalency) was generated for litigation.
Little effort was put into triage or emergency restoration.
The legal process was an exercise in which the trustees and the responsible party played brinkmanship: holding out until the court appearance was immanent then, at the last minute, reaching a settlement.
Only one (USA) coral reef grounding case has been settled in court: the Windspirit, 130 m-long sailing cruise ship that anchored on coral, Francis Bay, Virgin Islands National Park in 1990.
Judge T.K. Moore ordered the cruise ship owner to pay $300 000 in 1995 (Caroline Rogers, USGS, BRD, Personal Communication).
Large monetary settlements in vessel grounding incidents have resulted in a significant change in attitude.
The insurance companies have been more willing to consider taking proactive tactics (offering to take responsibility for the injuries and restoration).
Recent restoration projects The groundings that occurred in the Florida Keys between 1984 and 1989, with one exception, did not receive immediate restoration.
Recovery on these sites was poor (Gittings et al., 1988, Hudson and Diaz, 1988, Hanisak et al., 1989, Gittings and Bright, 1990, Gittings, 1991a, Gittings, 1991b, Gittings, 1991c, Gittings, 1991d).
Five recent incidents have occurred (three in Florida, one in the Cayman Islands, and one at St. John, USVI) where the responsible party has taken a proactive stance.
In each case, a large ship caused injuries ranging from a few toppled corals to massive reef damage.
The responsible party (RP) accepted responsibility, hired contractors to execute restoration, and funded a monitoring program.
This process reduced protracted legal debate and expedited recovery.
The RP paying for the restoration operation is usually more efficient than the government’s since it eliminates the bureaucratic contractual procedures (requests for proposals, formal bidding, writing contracts, and other time consuming, and non-productive elements) mandated by law for a government agency to hire a contractor.
The RP and the trustee technical staff develop a restoration plan, hire the contractor with the advise of the trustee, the work commences, and the trustee monitors performance.
If performance does not meet standards, the trustee may elect to stop operations and consider either continuing restoration after corrections are made or moving toward legal proceedings.
For the RP, the costs are less because the time scale is reduced, divers and biologists do not command the same salaries as lawyers and accountants, and the principal efforts are focused on restoring the reef.
Case histories 12.1. Firat The Firat ran across a reef and beached, following passage of Tropical Storm Gordon, near Port Everglades in Broward County, Florida, 15 November 1995.
The insurance company quickly hired a contractor to salvage the ship and tow it offshore without doing additional reef damage and hired a contractor to conduct a reef injury survey.
The survey included bottom mapping with differential GPS and diving to locate dislodged corals.
Within 6 weeks, 600 corals were transplanted, mapped, and identified.
The responsible party and trustee technical staff instituted a monitoring plan, which included a five-year program to evaluate the success of the work (Continental Shelf Associates, 1999).
12.2. Maasdam January 12, 1996, the cruise ship Maasdam struck (but was not aground) Soto’s Reef, George Town, Grand Cayman Islands, British West Indies.
The damaged area was determined by the Cayman Island Department of the Environment to be ≈1000 m2 of reef (planar area), including anchor scaring, crushed coral formations, and large chunks of reef platform that were broken and toppled onto a sand bed adjacent to the reef.
The RP accepted responsibility and worked with the Cayman Island DOE staff to develop a restoration plan, including a monitoring.
Work commenced in late January 1996 and was completed in April 1996 after an estimated 9000 h of underwater work: sorting coral and rubble, taking rubble off site, moving large boulders back atop the reef, and reattaching ≈3000 individual corals.
Monitoring of the project included a baseline (Jaap and Morelock, 1996), 6 months (Jaap and Morelock, 1997a), 1 year (Jaap and Morelock, 1997b), and 2 years (Jaap and Morelock, 1998).
12.3. Ryndam In January 1997 the cruise ship Ryndam dropped an anchor within the no-anchor zone in the Virgin Islands National Park, St. John, USVI.
The National Park Service determined that damage occurred to reef resources.
The vessel owner dispatched a consultant to independently verify the injuries.
The anchor and ground tackle had dislodged several corals and cut a shallow trench through a sedimentary-algal community.
The toppled corals were set upright, and a fine was paid for anchoring in the no-anchor zone.
12.4. Houston In February 1992 the container ship Houston ran aground because of a navigating error near Maryland Shoal in the lower Florida Keys.
The ship was successfully removed with minimal collateral damage.
The vessel operator and insurance companies agreed to assume responsibility, hired contractors and responded with multifaceted restoration.
The initial work entailed defining the damages, salvaging corals, and reattaching corals to the reef platform.
In the second phase, large rubble berms were stabilized with epoxy cement.
Large limestone boulders and articulated concrete mats were used to cover or buffer loose rubble fields on the site.
The RP also agreed to install six radar response transmitters (Raycon beacons) on navigational aids that are situated between Dry Tortugas and Fowey Rocks to provide additional warning to vessels plying the Straits of Florida.
Hurricane Georges damaged some of the restoration and the RP agreed to take remedial action to correct the problems.
12.5. Memphis The Memphis, a Los Angeles-class attack submarine, ran aground on a reef off Dania, Florida, 25 February 1993.
The Navy and Department of Justice were unwilling to take responsibilities and contested the reef damages.
After three years of legal maneuvering, the case was settled for $750 000.
These examples illustrate, working with the responsible party to initiate restoration quickly is a policy that can be beneficial.
The goals of coral reef restoration should be to maximize resource recovery as soon as possible.
The goal should not be this is a source of funds to support government programs and infrastructure.
Restoration success criteria The monitoring of a site should have a time scale relative to the potential for full recovery.
For example, if the site is expected to recover within 10 years, monitoring should be for that time span, with more intensive sampling at the onset and reduced effort toward the end (Table 3).
Monitoring is the only way to determine success of the restoration, observe status and trends, and correct problems (Gomez and Yap, 1984, Likens, 1988, Connell et al., 1997).
If a project is worthy of executing a restoration, it is worthy of monitoring the progress of the recovery.
13.1. Stability The reconstructed elements should be stable enough to withstand nominal waves and currents.
If 20%1 or more of the structures have moved, broken up, deteriorated, or caused collateral damage, remedial action should occur.
If there is high risk of human injury, the repair or remedial action should be taken as soon as possible.
13.2. Toxicity If there is an obvious zone around the structure where plants and animals are dead or showing signs of stress because of materials leaching from the structure, it will be necessary to re-evaluate the structure and the need to remove it.
13.3. Aesthetics Where feasible, it is recommended that the reconstruction should match the natural habitat characteristics.
Limestone rock is a better replacement than steel or concrete.
Ships, airplanes, and other waste materials should not be used as replacement structures for restoring a shallow-water coral reef.
13.4. Rubble stability If 20% of a rubble berm or loose materials have moved, remedial action should be executed.
13.5. Transplanting organisms Inspecting the status and condition of transplanted organisms requires visual observations, photography, and video.
During transplanting operations, a map of transplanted organism sites with installed reference markers and GPS coordinates should be compiled.
The status of attachment adhesion is important.
If 20% or more of the reattached organisms are dislodged, remedial action is called for.
Equally important is the vitality of the transplanted organisms.
Assessment should include color, bleaching, competition with benthic algae, disease, and percentage of cover by functional groups (stony coral, sponge, octocoral, benthic algae, rock).
The sampling must include sampling sites and corals (same taxa) from an adjacent undamaged area to provide a reference sample for vitality.
If the condition of transplanted organisms has deteriorated compared to the reference organisms, causes for the deterioration should be investigated.
Coral condition from the Maasdam restoration monitoring, 2 years after the restoration was finished, is presented in Fig.
Data were collected using 35 mm photographs.
Each photograph was scored for color, bleaching, and algal competition, and the amount of cover present in the photograph was evaluated using point count analysis (Curtis, 1968).
The fate of individual coral colonies following transplanting used planimetric analysis.
The individual corals were evaluated at baseline (about 1 month), 6 months, 1, and 2 years following restoration.
There appears to be moderate fluctuations about the central tendency (Fig.
The restored stations were consistently lower in coral cover because transplanting did not attempt to restore to pre-accident status.
In other studies, the success of transplanting corals to rehabilitate degraded reefs range from moderate to high success.
Guzman (1991) reported 79–83% success for 110 fragments of Pocillopora transplanted on a reef off the Pacific coast of Costa Rica.
Download: Download full-size image Fig.
Monitoring results, Maasdam restoration, Soto’s Reef, Grand Cayman, British West Indies.
Coral color, bleaching, and algal competition evaluations were qualitatively scored, coral cover is quantitative based on point count (n=36 photos at each reference, and restored site).
The abbreviations are: C: control, T: transplants.
Download: Download full-size image Fig.
Planametric analytical evaluation of coral cover, Maasdam restoration, Soto’s Reef, Grand Cayman, British West Indies.
Data based on ten restored (14 m2) and five reference (7 m2) photo quadrats.
Abbreviation: R=restored, C=reference.
13.6. Coral recruitment Defined as: settlement of sessile benthic organisms, resulting in spatial occupation of the damaged areas.
Visual observations, photographs, video, and experiments are typically employed to evaluate this.
The damaged area is compared to an undamaged reference site(s) to judge progress.
10 presents data collected six months, one year, and two years after completion of restoration at the Maasdam, Soto’s Reef site.
There is good indication that coral recruitment on the restored areas is quite similar to the reference sites.
Download: Download full-size image Fig.
Coral recruitment at the Maasdam restoration, Soto’s Reef, Grand Cayman, British West Indies.
The abbreviations are: C: Control, T: Transplant, R: Rubble piles, NR: a remote reef, several miles from Soto’s Reef.
The Soto’s Reef project had a short monitoring component that documented the restoration actions was relatively successful, did not cause harm, and functioned as intended.
Ideally, we would have preferred that the monitoring be continued for at least 10 years (sampling to include a baseline, 6 months, 1, 2, 4, 6, 8, and 10 years) considering the magnitude of the damage.
Abstract Major changes in society have led to a call for structural changes in forestry, also in Europe.
Urbanisation as one of the major driving forces has had a clear impact on European forestry.
One of the new approaches emerging in response is the concept of urban forestry.
It was developed in North America during the 1960s as innovative approach to managing natural resources in urban environments.
Aimed at the integrated planning and management of all tree-based resources in cities and towns, the concept found broad support in North America after initial resistance from both foresters and urban green professionals.
Similar resistance was met in Europe, and here it took until the early 1990s before the concept of urban forestry found broader acceptance and support.
Since then, a European urban forestry research community has emerged, as have policies, programmes and higher education incorporating elements of urban forestry.
Urban forest resources in Europe might be small in relative terms compared to other natural resources.
They do, however, cover millions of hectares of land and provide multiple, highly demanded goods and services.
Forestry can benefit from urban forestry experiences and innovations, for example in terms of better meeting the expectations and demands of urban society.
Urban forestry, on the other hand, is firmly rooted in some of the basic concepts of traditional forestry, such as sustained yield.
Review of a decade of urban forestry in Europe shows that strong links should be maintained for the benefit of both.
Previous article in issue Next article in issue Keywords Urban forestryUrbanisationForest scienceForest policyEurope 1.
The new face of forestry With the major socio-economic transition of the Western world into an urban, post-industrial and global economy and society, traditional forestry and natural resource management have been facing considerably public scepticism and re-evaluation (Kennedy et al., 1998).
The legitimacy of foresters has been challenged and many long-standing public forest and natural resource policies and practices have been questioned (Kennedy et al., 1998, Otto, 1998).
An adaptation of professional values and management concepts constituting a major paradigm shift has been called for (Kennedy et al., 1998).
The need for change has led to various developments and adaptations.
In North America, for example, ‘new forestry’ in the shape of sustainable ecosystem-based management or stewardship was developed as a new guiding concept for forestry.
Similar developments have taken place in Europe, where multiple-use management and sustainable forest ecosystem management now are accepted and leading concepts (e.g. Kennedy et al., 1998).
These new approaches recognise the importance of the socio-cultural and environmental values of forests, apart from the economic values (i.e. timber production) that have traditionally been prioritised.
Rather than managing tree stands, complex forest ecosystems are the subject of management.
The human dimension of these ecosystems in terms of multiple users and stakeholders is an integral part of this.
Not only foresters but also public land managers, in general, are increasingly turning into social value brokers and conflict management facilitators (Kennedy and Ward Thomas, 1995, Kennedy et al., 1998).
The significant changes in forestry are can also be derived from the changes in definitions of terms as ‘forest’, ‘forestry’ and ‘forester’ over time (Helms, 2002).
(1998) conceptualised the ongoing paradigm shift in forestry through the transition from a machine model to an organic model.
In the new, organic model, the complexity of forest ecosystems with their interdependent subsystems and many relationships is recognised and appreciated rather than distrusted, and focus is on forest function or process.
Rather than the rigid, hierarchical and monodisciplinary forestry institutions of the past, new forest management institutions are needed.
These should be flexible, accepting and open organisations, involving a wide range of disciplines and interests being actively involved in a collaborative dialogue.
Broader and more inclusive visions and goals are formulated, but science and scientists provide one set of values and skills.
As community-level participation and conflict management are increasingly important, diverse social science and people skills are recognised and developed.
The role of urbanisation in the change of forestry should not be overlooked.
Large parts of the world have become highly urbanised and the majority of the world's population now lives in cities and towns (WRI, 2001).
Although some forests have been under the direct influence of cities and towns for ages, and especially in Europe (Hosmer, 1922, Konijnendijk, 1999), the dramatic ‘urbanisation’ of the forest is a more recent phenomenon.
Paris (1972) spoke of the ‘citification’ of the forest: conflict situations between ‘industrial’ and ‘societal’ use of forests have been occurring to an increasing extent, and urban societies have been imposing their ideas, values, perceptions and life styles on the countryside and its forest areas.
Although a growing part of the forest resource has come under urban influence, both directly (i.e. becoming incorporated into the interface or located at the interface with urban areas) and indirectly (as urban uses and values have also come to dominate more remote forest areas), forestry has been rather hesitant to recognise its urban mandate.
It has considered itself as a primarily rural activity, most forest resources are situated in rural (or natural) areas and the production process had much in common with agricultural production.
Töpfer (2001) mentions how the traditional urban–rural controversy (one was either pro- or anti-urban) has obstructed with more effective and sustainable land use planning, for example at the urban fringe.
Institutions such as the Food and Agriculture Organisation of the United Nations, and state forestry agencies even in the most urbanised countries have only recently recognised their urban mandate (e.g. Konijnendijk, 1999, FAO, 2002).
Policy-makers, planners and managers, however, have expressed the lack of forestry concepts, approaches and methods adapted to the urban environment (Krott, 1998, Konijnendijk, 1999).
This article aims to explore the status and prospects of the incorporation of the urban dimension into forestry, as important element of the overall paradigm shift occurring within the field.
It reviews the emergence and status of the concept of urban forestry in Europe, as an attempt to accommodate forestry and the need for an urban scope.
Finally, urban forestry's possible value for the development of forestry at large is analysed.
Development and definition of the urban forestry concept The most broadly accepted definition of urban forestry, based on Miller (1997) is ‘the art, science and technology of managing trees and forest resources in and around urban community ecosystems for the physiological, sociological, economic and aesthetic benefits trees provide society’ (Helms, 1998, p.
This definition already makes it clear that urban forestry is more than just ‘forestry’ in (or near) urban areas.
Apart from forest resources, for example, other tree-dominated vegetation is included in the scope of urban forestry.
2.1. Brief history of urban forestry in North America The term ‘urban forestry’ was first used in 1965 as title for a graduate study on the success and failures of municipal tree planting in part of Metropolitan Toronto (Johnston, 1996).
Before that, graduates of forestry schools in North America were more frequently hired to manage municipal tree management programmes because of their biological, quantitative and managerial skills (Miller, 2001).
Problems caused by for example introduced pests and diseases had called for more integrative tree management approaches (Johnston, 1996).
In spite of recognition of the concept by the Society of American Foresters, and the hosting of National Urban Forestry Conferences, it took some time for urban forestry to become accepted by a broader group of experts.
For example, many foresters were reluctant to see a role for forestry in urban areas.
Many arborists and other urban green space professionals were hesitant to embrace urban forestry, as they felt that foresters used it as a way into their domain (Johnston, 1996, Miller, 2001).
The benefits of using the integrative and interdisciplinary concept, however, were increasingly recognised.
Helped by the lobbying efforts of interest groups such as American Forests, political support for the approach was gained.
A rather extensive funding scheme was developed to support urban forestry research, policy and practice.
The American urban forestry research scene today is very well developed, with high-level research being undertaken at universities together with federal and state research agencies (Johnston, 1996, Miller, 2001).
Higher education in urban forestry exists through, for example, 30 Baccalaureate programmes, mostly offered by forestry faculties or departments (Miller, personal communication).
2.2. Brief history of urban forestry in Europe It took longer for the concept to gain hold in Europe, although Europe can pride itself on a long tradition of urban green space planning, design and management.
Developments such as the growing demands for urban green functions and increasing pressures on green areas led to an interest in more strategic and integrated approaches, such as urban ecology and urban green structure planning, during the 1970s and 1980s.
Researchers interested in the tree dimension of urban green got to know the concept of urban forestry as applied in North America, e.g. through study visits and conferences.
Some of the North American urban forestry pioneers were involved in organising the symposium ‘Trees and forests for human settlements’ in Norway (1976), jointly with the United Nations’ Habitant Forum and the International Union of Forest Research Organizations (IUFRO) (Johnston, 1997a, Johnston, 1997b).
Initial resistance against the concept also existed in Europe.
Even though the scientific Arboricultural Journal was given the subtitle ‘International Journal of Urban Forestry’ in 1981, its publisher the British Arboricultural Association saw the term as an unnecessary ‘Americanism’ (Johnston, 1997b).
Support for the concept came from interested landscape architects and especially foresters.
Researchers at the Dutch state forest research institute undertook several study tours to North America in order to get familiar with the approach during the early 1980s (Heybroek et al., 1985).
Britain, however, became the first European stronghold of urban forestry.
Representatives of NGOs and other interest groups involved with urban tree planting and management schemes helped promote the concept based on close collaboration with American counterparts, e.g. by setting up several large-scale urban forestry projects in various cities (e.g. Johnston, 1997b).
Governmental interest followed, e.g. through the nation-wide Community Forests developed during the late 1980s.
Forest and tree planting and management were to be used as tools for environmental, social and economic development of 12 urban agglomerations and their surrounding areas.
The Community Forests programme draws heavily upon elements of the urban forestry concept, such as focus on social values and a broader concept of ‘forest’ (Davies and Vaughan, 1998).
The National Urban Forestry Unit (NUFU) was set up in 1995 as an independent organisation championing the need for integration of tree planting, conservation and management with different agendas, such as health, land reclamation, built development, heritage and education (NUFU, 2002).
Initially, Ireland was the only country to follow Britain in embracing the concept of urban forestry.
The first Urban Forestry Conference, held in Dublin in 1991, led to government recognition for example via a grant scheme for urban woodlands.
The first major review of urban forestry in Ireland was carried out in 1994 and the first urban tree resource in Ireland (for Dublin) started in 1993 (Johnston, 1997b).
Networking and international contacts proved crucial in the British, Dutch, Irish as well as other cases.
The International Society of Arboriculture, set up in the United States in 1924 as the National Shade Tree Conference, gradually increased its international member base and activities to meet part of the networking demand (Johnston, 1996).
Several new networks of urban forestry researchers emerged in response during the 1990s.
The Nordic Forest Research Cooperation Committee (SNS) supported a first Nordic workshop on urban forestry held in Reykjavik in 1996 (Nilsson and Randrup, 1996).
SNS continued to support urban forestry networking through funding joint Nordic–Baltic seminars in Tallinn (Sander and Randrup, 1998) and Kaunas (Randrup et al., 2001).
The European Forest Institute (EFI), an independent non-governmental organisation conducting forest research, also became involved in urban forestry research during the mid-1990s.
It undertook a comparative European study of urban woodland policies, conservation and management (Konijnendijk, 1999).
The Danish Forest and Landscape Research Institute then initiated what proved to be an important step for the advancement of urban forestry in Europe.
A network for the promotion and coordination of urban forestry in Europe was set up in 1997, under the European Union-funded COST programme (European Cooperation in the field of Scientific and Technical Research).
COST Action E12 Urban Forests and Trees ran until 2002 and involved more than 100 experts from 22 European countries.
The Action organised a series of seminars as well as two conferences on urban forestry topics, often with the participation of experts from outside Europe.
It reviewed the status of research and higher education on urban forestry in Europe, issued a long list of publications and started compiling a first European reference book on urban forestry.
A strong European network resulted from the Action and led to several new initiatives (Nilsson and Konijnendijk, in press).
One of the direct spin-offs of COST E12 as well as EFI's activities concerning urban forestry was the establishment of the European Urban Forestry Research and Information Centre (EUFORIC) in 2001.
EUFORIC operates as one of six so-called Regional Project Centres of EFI.
These are centres without walls focusing on a topic of specific interest within European forestry.
EUFORIC aims to act as a clearinghouse and coordinator within European urban forestry.
Activities so far also included organising conferences such as ‘Forestry serving urbanised societies’ in Copenhagen (2002), and the launch of a new scientific journal (Urban Forestry and Urban Greening) to serve the urban forestry research community.
A number of additional new, international initiatives emerged within European urban forestry during the late 1990s and early 2000s.
Various international projects, for example under the European Union's Fifth Framework Programme for research have used the term, although still seldom in their title, were started.
Conferences on urban forestry topics such as indigenous vegetation and plant health in urban horticulture were held.
From a non-scientific perspective, IUFRO's European Forum on Urban Forestry, organised annually since 1998, can be mentioned.
The Forum brings together urban forestry practitioners to exchange experiences and ideas (Krott, 1998).
2.3. Defining urban forestry in Europe The emergence of an urban forestry research community at the European level might suggest that broad acceptance of the concept has been achieved.
The definition of urban forestry within the European context is still under debate.
One of the problems faced related to the difference between ‘concept’ and ‘term’.
While concepts are the cognitive representation or perceptions of objects or facts, terms are their linguistic expression or linguistic label (ISO, 2000).
While broad agreement seems to exist about the relevance of the urban forestry concept, the term has evoked confusion in Europe.
‘Urban forest’ can be translated into different European languages into terms such as Stadtwald (German), stadsbos (Dutch), bynær skov or byskov and taajamametsä (Finnish).
These often have had a longer tradition as referring to only the woodland element of urban green structures (Konijnendijk, 1999).
Urban woodlands in the form of communal, city or town woodlands are a very European phenomenon, with a long history of woodland conservation and management (Hosmer, 1922, Konijnendijk, 1999).
The wide variation in definitions of ‘urban forestry’ and ‘urban forests’ still used in Europe is illustrated in Table 1.
The more traditional meaning of terms similar to ‘urban forest’ can be noted.
English-speaking countries have been the first to incorporate urban forestry as a more integrative and broad concept.
Through its activities and discussions, COST Action E12 ‘Urban Forests and Trees’ has helped to make at least the concept of urban forestry more accepted amongst European researchers (Nilsson and Konijnendijk, in press).
The concept applied is very similar to the definition of urban forestry as mentioned at the outset of this article (Helms, 1998).
Examples of definitions of urban forestry and urban forests provided by the national experts of COST Action E12 ‘Urban Forests and Trees’ (based on Forrest et al., 1999)  Country	Definition of urban forest and/or urban forestry Finland	Urban forests have been defined as forests located in or near an urban area where the main function is recreation.
They consist mainly of natural forest vegetation and therefore, the definition excludes for example, man-made parks with lawns.
Germany	No adequate term is existing to cover urban forests and urban forestry.
A tradition exists with using the term ‘Stadwald’, referring to the forest element.
Urban forest mostly would refer to man-made forest on formerly agricultural or even derelict land specifically designed and managed for the recreation of the urban population.
Greece	Urban forests refer to urban green spaces and include: (a) the trees along the streets of towns and cities; (b) the parks and gardens within city boundaries; and (c) the forests around towns and cities.
Iceland	Urban forestry is the planting of trees and tree stands within the legal boundaries of urban areas with the purpose of providing amenities for the population, namely shelter, recreation, landscaping, beauty and even production of timber or other products, where it does not detract from other amenity values.
Ireland	An extensive definition, similar to North American concept, is applied for urban forestry.
Recognised are e.g. the adoption of forestry principles, the inclusion of the entire tree and woodland resource in and around an urban area, the fact that trees are managed as part of an overall resource, urban forestry being a social discipline, the need for coordinated involvement, etc.
Italy	The term urban forest has hardly been used.
The concept of ‘urban forests and trees’ is related to the wider, inclusive of the term ‘urban greenery’, defined as any designed open space in urban areas, concerned with—as a whole or in part—vegetation elements and regularly managed.
Lithuania	Urban forestry includes forests, street trees and other green areas.
The focus of urban forestry in Lithuania has mostly been municipal.
Slovenia	Urban forests represent forests, parks, i.e. woodland resources in urban areas, which have environmental and social rather than production functions and benefits for the citizens.
The urban area is regarded as the area of a (town) municipality.
The owner of the urban forest should in principle be the municipality.
The Netherlands	Approximately 10% of all Dutch forests considered urban woodlands.
The term ‘urban forest’ would translate as ‘stadsbos’ (Borgesius, 1992), i.e. referring to urban woodland.
For urban forest at large, the term ‘urban green’ is most commonly used.
Public urban green areas include nature areas, urban woodlands, parks, green areas, public gardens and street and roadside trees.
United Kingdom	Urban forestry is a multi-disciplinary activity that encompasses the design, planning, establishment and management of trees, woodlands and associated flora and open space, which is usually physically linked to form a mosaic of vegetation in or near built-up areas.
It serves a range of multi-purpose functions, but it is primarily for amenity and the promotion of human well-being.
‘Forest’ within ‘urban forest’ thus has been given a different meaning than the traditional forest concept encompasses.
By including small woods, parks and gardens with area size and/or canopy cover below thresholds for ‘forest’, as well as individual trees the traditional forest concept has been broadened considerably.
Status and significance of urban forestry in Europe 3.1. Urban forest resources Urban forests refer to all forest and tree resources in (and close to) urban areas.
This concept is difficult to operationalise for the purpose of reliable resource inventories.
Questions to be answered include how to define ‘urban’, ‘forest’, as well as ‘close to’.
Different countries use very different definitions of ‘urban’ (Forrest et al., 1999) and ‘forest’ (Helms, 2002).
As we have seen, moreover, the ‘forest’ in urban forest related to more than forest in its more traditional definition.
‘Other wooded land’ and ‘trees outside forests’, categories used by FAO for its forest resource assessments (FRAs) (FAO, 2002), in the shape of for example parks, gardens and street trees are to be included when they are located in (or near) urban areas.
Problems with operationalising the urban forest concept hamper sound resource inventories and monitoring.
Moreover, FAO's FRAs have not paid any particular attention to urban forest resources so far, although ‘trees outside forests’ were mentioned in the FRA 2000 as an important area for future assessments (FAO, 2002).
A first national, comprehensive assessment of urban forest resources was carried out by the United States Forest Service (Dwyer et al., 2000).
It applied a combination of methods, including satellite imagery, national statistical data and assessments for particular cities or metropolitan areas.
Tree canopy cover was used as a more reliable indicator than land use types.
The assessment showed that 74.4 billion trees cover 33.4% of the metropolitan areas (urban countries) in the 48 adjacent states, i.e. approximately 8% of land area and 1/4 of all trees in the 48 states.
In urban areas in a more narrow sense (i.e. cities, towns, villages, etc.), 3.8 billion trees cover 27.1% of the land, i.e. approximately 1% of the entire adjacent United States.
No comprehensive, comparative assessments of urban forest resources in Europe (international or national level) seem to be available at the time.
Table 2 includes information about some (partial or less reliable) assessments of urban green space cover.
The European Environment Agency has provided statistics on urban green area cover in selected European cities, but mentioned that statistics are unreliable and not easy to compare (EEA, 1995).
It is uncertain, for example, what types of green areas (category?
ownership?) have been included.
Moreover, total green structure, with its non-tree-dominated elements, will be larger than the urban forest resource.
The survey by Ottitsch (2002) faced similar problems, while the study by Pauleit et al.
(2002), attempting to use tree canopy cover, seems more informative, although the authors also expressed their concern about data quality and comparability.
Data on urban green space cover in Europe (examples)  Region/country	Information on urban	Reference Empty Cell	green space resource	Empty Cell Europe	Green space cover of selected cities	EEA (1995) varied between 5% (Madrid) and 60% (Bratislava).
Tree (canopy) cover in cities in 8	Pauleit et al.
(2002) European countries: ranging from 1.5 to 62%.
Green area cover for 14 European	Ottitsch (2002) cities surveyed varied between 5% (Thessaloniki)	 and 56% (Ljubljana); average of	 approximately 30% for all cities.
Green space per	 inhabitant from 6 to approximately 7000 m2.
Belgium	Flanders region: 9% of municipalities	Basiaux et al.
(1999) covered by green areas (1991 survey).
Brussels region: 14% (2300 ha)	 of land area covered by green space.
Great Britain	Green areas cover approximately 14% of urban areas.
DTLR (2002) Parks and green spaces estimated	 to account for 120 000–150 000 ha.
The Netherlands	Average municipal green space cover	CBS (1998) of 19% for 22 of the largest	 Dutch cities (i.e. average of 228 m2/inhabitant).
Johnston and Rushton (1999) also noted the lack of records and inventories of urban tree resources, as did the British Green Spaces Taskforce.
The latter called for a green space typology and more reliable and comprehensive inventory of green spaces (DTLR, 2002).
In the Netherlands, the national statistical data for municipal land use include green areas as consisting of a wide range of elements, such as parks and gardens, woodlands and cemeteries (CBS, 1998).
From a forestry perspective, the woodland element of urban forests has special interest.
In this case, it is not much easier, however, to obtain comparative data, although the definition of these woodlands as ‘forests’ under the national law should facilitate inventory.
The major difficulty is to determine what woodlands are to be classified as ‘urban’.
Table 3 provides the results of some assessments made.
In many cases, urban woodland area and/or cover are assessed by only including the areas defined as ‘forest’ within the municipal boundaries.
The study by Konijnendijk, 1999, Konijnendijk, 2001 is an example of this.
Scientists have attempted to assess the wider urban woodland resource at country level by including peri-urban or urban fringe forests, as well as by including all municipally-owned forests, as shown in the table.
Data on urban woodland area and cover in Europe (examples)  Region/Country	Information on size of	Reference Empty Cell	urban woodland resource	Empty Cell Europe	Average woodland cover of 18.5%	Konijnendijk (2001) within municipal boundaries of	 26 larger European cities (104 m2/inhabitant)	  Belgium	Flanders region: approximately 4.5% of municipalities	Basiaux et al.
(1999) included in 1991 survey covered by woodlands.
Walloon region: 25 000 ha of forests located in	 suburban areas and managed for community uses.
No data on municipal forests available.
Brussels region: 1950 ha (12%)	 of land area covered by woodlands.
Czech Republic	Fifteen percent of all forests owned by municipalities	Záruba (1998) and cooperations.
100 larger cities own	 between 500 and 8000 ha of forests.
Finland	Municipalities in Finland own 430 000 ha of forests.
Löfström (1999) cited by Tyrväinen (1999)  France	270 000 ha of forests in the Greater	Moigneu (2001) Paris region; 80 m2 of forest per	 inhabitant (compared to 800 m2 for France as a whole).
Latvia	0.8% of all Latvian forests considered	Donis (2001) urban forests (owned by cities and towns).
Twenty percent of urban areas covered by forests.
The Netherlands	Average municipal woodland cover of	CBS (1998) approximately 7% for 22 of the largest Dutch cities.
Larger cities usually have municipal forest	 cover of between 0 and 5% (1993 data).
Slovakia	Ten percent (186 000 ha) of Slovakian	Graus (1998) forests owned by municipalities.
Sweden	300 000 ha considered ‘urban fringe forests’, i.e. more	Carlborg (1991) cited by Rydberg (1998) than 1% of the overall Swedish forest cover.
United Kingdom	Community forests programme aimed	Ball et al.
(1999) at achieving a 30% woodland cover (≈119 000 ha)	 around 12 large agglomerations	 over next decades.
Actual cover in 1999 was 6.5%.
Similar tables could be drawn up for other components of the urban green structure or urban forest resource, for example public parks and gardens, street tree population, and so forth.
Again, comparative data are difficult to obtain (Johnston and Rushton, 1999, Pauleit et al., 2002).
The limited data presented here at least provide some insight in the significance of urban forest resource in Europe.
Table 3 suggests that Nordic and Central European countries assess their urban woodland resource to one or several percents of their overall forest resource.
This share is considerably higher in the more urbanised parts of Western Europe, and increasing through afforestation near large agglomerations (Mather, 1990, Konijnendijk, 1999).
In some local cases, urban woodland resources are very significant: Berlin owns approximately 27 000 of nearby forests, and the city of St. Petersburg is responsible for a 142 000 ha forest greenbelt (Konijnendijk, 1999).
In absolute terms, urban woodland resources are significant, covering millions of hectares in Europe.
As the work by Dwyer et al.
(2000) indicated, the actual urban forest resource is significantly larger when other tree-dominated lands are included.
3.2. Provision of goods and services Urban forest resources might be small compared to e.g. total forest land in many European countries, their are of high importance in terms of providing goods and services to society, even although timber production is often of minor importance (Konijnendijk, 1999).
Urban woodlands and other parts of the urban forest are the most popular outdoor recreation environments in Europe.
Between 1/4 and 1/2 of all annual forest visits in France take place in the 80 000 ha of forests in the Greater Paris region (Moigneu, 2001).
In Sweden, an estimated 55% of all forest visits are to urban woodlands (Rydberg, 1998).
Urban woodlands in Europe often attract several thousands of visits per hectare per year (Konijnendijk, 1999), as the large majority of all recreational visits to forests are paid to sites not more than 1–2 km from the home (e.g. Hörnsten, 2000).
The impact of urban forests on physical and mental human health, e.g. through offering environments for exercise and reducing stress, also has been given research focus lately (Grahn and Stigsdotter, 2003).
The presence of trees and woodlands close to where many people live can also cause problems, as in the cases of fires occurring at the urban fringe, as well as of health threats such as diseases carried by animals, and allergies.
Urban trees and other vegetation intercept particles and gaseous pollutants (Harris, 1992, McPherson et al., 1997) and act as carbon sinks in the equations relevant within the context of global warming (McPherson and Simpson, 1999).
They reduce stormwater runoff and many European cities have established and conserved forests for protecting their drinking water resources (Konijnendijk, 1999).
Urban green protects soils and moderates harsh urban climates, e.g. by cooling the air, reducing wind speeds and shading (McPherson et al., 1997).
The level of biodiversity of urban green areas is often surprisingly high (Milligan Raedeke and Raedeke, 1995).
National parks are found at the gates of large cities such as Warsaw, Moscow and Vienna (Konijnendijk, 1999).
Cities have often turned to green areas for providing attractive environments for businesses to settle and people to live (Konijnendijk, 1999, Konijnendijk, 2001).
The generally positive impact of nearby forests and green areas on house prices has become documented, e.g. by Tyrväinen (1999).
Price (2002) provides a review of ways to assess the aesthetical values of urban forests.
3.3. Policies Attention for urban forestry at the European level has been limited so far, although sufficient access to public green space is seen as an important indicator for sustainable cities (EEA, 1995).
At the national level, however, new policies have incorporated the importance of urban forests and/or urban forest elements.
Countries such as Belgium (Flanders), Denmark, Ireland, The Netherlands and Great Britain issued afforestation policies in which urban agglomerations have the highest priority.
Woodland grant schemes thus favour urban settings.
Social and environmental services such as providing opportunities for outdoor recreation and protection of drinking water for primarily urban populations have become prioritised in national forest policies (Konijnendijk, 1999).
Urban and community forests are described as a priority and powerful tool in the England Forestry Strategy issued in 1998 (Forestry Commission, 1998).
Some European cities with a long history of woodland ownership developed strategies and policies for their woodlands, while most other cities have contented themselves with forest management plans only (Konijnendijk, 1999).
Comprehensive local urban forestry strategies are even less common, especially outside of Britain and Ireland.
Krott (personal communication) mentions that is has been problematic to develop true urban forestry policies at city level due to for example funding problems, political struggles and different priorities.
3.4. Research and education The described networking initiatives helped urban forestry research establish itself in Europe.
Reviews of the status of urban forestry research and higher education in Europe carried out within the framework of COST Action E12 acknowledged the increasing level of activity (Konijnendijk et al., 2000, Andersen et al., 2002).
A survey of 20 European countries identified more than 400 recent or ongoing research projects on trees and/or forests in the urban environment.
A wide range of topics had occupied researchers, while attention for three main components of urban forests—woodlands, parks and individual trees—had been about equal (Konijnendijk et al., 2000).
Higher education (i.e. at Bachelor level or higher) on urban forestry has been less developed so far.
One hundred and eighty educational institutions in 28 countries offered 31 full degree programmes and 191 courses and modules.
Only very few, however, were regarded ‘urban forestry’ in the true sense of the concept by the researchers, as mostly only some elements were touched upon, primarily from a monodisciplinary perspective.
An increase in the number of programmes and courses offered, however, was noted (Andersen et al., 2002).
Discussion: urban forestry's relation to forestry Urban forestry has gradually established itself in Europe as integrative and innovative approach towards the tree-dominated part of urban green structures.
The urban forest resource is relatively small compared to overall forest resources, but expanding and already covering a significant area of land.
They provide multiple essential benefits to urban societies.
A research community has emerged during the past decade, higher education is under development and policy attention is increasing.
But, what has made urban forestry innovative and in what way can it be a valuable contributor to the ongoing development of modern forestry.
Moreover, how does urban forestry build upon and benefit from traditional forestry concepts and approaches?
As outlined in the first section, structural changes in forestry are called for.
The very concept of forest, for example, has been under continued scrutiny (Helms, 2002).
It has broadened over time to take an ecosystem perspective, but a further crossing of boundaries has been called for, as different land uses need to be regarded in a more integrated way (Kennedy et al., 1998).
The traditional urban–rural divide, for example, has unproductive and gives wrong sense of alternative development options.
More regional and landscape concepts are needed to strengthen the links and complementarities between cities and rural areas (Töpfer, 2001).
New concepts and approaches such as landscape ecology and management, sustainable land use, urban ecology, and urban agriculture all take a more integrative perspective on different land uses, land covers and ecosystems.
Urban forestry does the same by crossing the boundaries between woodlands and other elements of urban (and peri-urban) green structures.
Initiatives such as the English Community Forests go even further.
Building on the concepts of urban and community forestry, new types of ‘forest landscapes’ are created, where woodlands are only one—be it important-element of land use mosaics (Davies and Vaughan, 1998).
This also provides a suitable platform for multiple disciplines to work together.
Urban forestry is multidisciplinary, and ideally even interdisciplinary.
The earlier mentioned review of research on urban tree resources in Europe identified 38 disciplines being involved, including basic as well as applied sciences, natural and social sciences, the humanities as well as planning sciences (Konijnendijk et al., 2000).
Multifunctionality in forestry is also called for.
By focusing on other goods and services than the traditional output of forestry, i.e. timber production, urban forestry provides an interesting perspective.
Urban forestry, by its very nature, can only be successful if meeting the multiple demands of ever-present urban societies.
In this way, urban forests have been described as ‘hotspots’ for forestry at large (Krott, 1998).
They act as testing grounds for forestry at large attempting to meet changing societal demands.
It has shown that the soft values of forests and trees are in fact very important, socially, environmentally as well as economically.
The possible negative effects of having trees and forests close to people, as in the case of wildfires, should not be neglected in this respect.
Modern forestry should manifest itself more as social value broker and conflict manager.
Again, urban forestry provides a valuable example.
Social services are in focus, as providing healthy recreational, living and working environments is prioritised.
High demands for urban forest goods and services have to be met by a small resource base, and conflicts have been a logical consequence.
Thus urban foresters have had to develop their people skills as well as conflict management capacities.
They are learning how to involve other stakeholders in their decisions and activities.
In high-pressure urban environments, partnerships are a necessity.
Teamwork with fellow professionals is required, as well as close collaboration with non-experts.
Urban forestry can become a powerful tool for community building.
The integration of fringe groups, for example, can be promoted through urban forests and forestry (Dwyer et al., 2000, Krott, personal communication).
As areas of collaboration and demonstration, urban forests can improve transparency and forestry's image in society (Rydberg, 1998, von Gadow, 2002).
This brings us to developing new, flexible institutions for managing forests and other natural resources.
Urban forestry has faced the same need and new types of institutions have been created.
The independently-operating project teams that coordinate the 12 English Community Forests, for instance, operate in close collaboration with a range of public and private actors, combining skills such as forestry, ecology, planning, marketing and community relations and involvement.
Funding has been a growing problem for public and private forestry in Europe.
Urban green space management has traditionally been dependent on municipal budgets, which have been reduced over time.
As a consequence, innovative ways of raising income and reducing costs have been explored.
Infiltration of alternative funding programmes, from the local level to the European Union, has been one strategy.
Marketing of goods and services other than timber or of locally produced certified timber has been attempted, with variable success.
Urban foresters have demonstrated that they produce services in a very efficient way.
Management of the municipal forests of Wuppertal, Germany costs less than €1 per forest visit, which compares favourably to the cost of other recreational activities (Vosteen, 2002).
In some cases, urban forestry elements have been built into large-scale projects such as new housing schemes, landscape development, and industrial developments (e.g. Konijnendijk, 2001).
Krott (personal communication) believes that this ‘greening’ of major development projects is very important for the success of urban forestry.
Programmes such as the English Community Forests, the England Forestry Strategy and various national and local policies and programmes promoting urban forests also relate to another demand placed on forestry at large: the need for bolder and long-term strategies connecting to agendas other than those of traditional forestry.
The relationship between forestry and urban forestry is based on mutual benefits and not on ‘one way traffic’.
Forestry has been the driving force behind the development of the concept of urban forestry, for a start.
Foresters were brought into cities because of their more holistic and strategic insight (Miller, 2001).
Today, forestry is still the leading discipline in European urban forestry research and education (Konijnendijk et al., 2000, Andersen et al., 2002).
This it not strange, as explained by Collins (1997) who outlines the links of urban forestry with traditional forestry.
Urban forestry has adopted the principle of sustained yield, which underpins forestry; it sets out to achieve and maintain a balanced age structure within each urban locality, ensure continuous tree cover, and hence sustained provision of goods and services for current and future generations.
Trees are managed as part of the overall resource, and by means of long-term planning based on secure resource allocation and detailed surveys.
Urban forestry and forestry at large thus are closely connected and should remain so in order to benefit from each other's efforts in better meeting the demands of changing societies.
Abstract Urban forestry is generally defined as the art, science and technology of managing trees and forest resources in and around urban community ecosystems for the physiological, sociological, economic, and aesthetic benefits trees provide society.
First mentioned in the United States as early as in 1894, the concept underwent a revival during the 1960s as a comprehensive and interdisciplinary approach to the specific challenges related to growing trees in urban environments.
Later, urban forestry evoked the interest of scientists and practitioners in other parts of the world.
However, harmonization of urban forestry terminology has been complicated by, for example, the involvement of different disciplines and translation difficulties.
In many European languages, for example, the direct translation of ‘urban forestry’ relates more to forest ecosystems than to street and park trees.
Efforts in North America and Europe defining ‘urban forest’, ‘urban forestry’ and related terms are introduced.
A comparative analysis of selected urban forestry terminology in both parts of the world shows that urban forestry has a longer history in North America, based on traditions of shade tree management.
Moreover, urban forestry has become more institutionalized in North America.
Urban forestry in Europe has built strongly on a century-long tradition of ‘town forestry’.
In both parts of the world, definitions of urban forestry and urban forest have become more comprehensive, including all tree stands and individual trees in and around urban areas.
Agreement also exists on the multifunctional and multidisciplinary character of urban forestry.
These similarities offer opportunities for international harmonization of terminology.
Previous article in issue Next article in issue Keywords Urban forestryUrban forestTerminologyCommunity forestry Concepts for comprehensive urban greenspace management Those planning and managing woodland, parks, gardens, street and square trees, and other green areas within urban agglomerations (here collectively identified as urban greenspace) are operating in highly complex environments, facing multiple and rapidly changing urban demands (e.g., Miller, 1997; Konijnendijk et al., 2005).
Urban sites are often harsh, characterized by many pressures and threats, from limited growing space to adverse climatic conditions and air pollution.
Greenspace planners and managers are often struggling to keep greenspace issues on the political agenda.
In response, comprehensive and integrated land use concepts and approaches have emerged, building on the expertise and skills of various professions.
Urban forestry is one of the approaches that gradually has found recognition internationally.
It looks at urban greenspace from an integrative perspective, considering individual greenspace elements as part of an integral whole (Miller, 1997; Konijnendijk and Randrup, 2004).
Urban forestry focusses on urban greenspace comprising of tree stands as well as individual trees.
It is multidisciplinary and does not only involve foresters.
Although there is international agreement that it deals, at least, with forests or forest-like systems in urban areas, there is still considerable scientific debate on the contents of the concept and related terms.
Which parts of greenspace are seen as the domain of urban forestry?
What areas does ‘urban’ encompass?
How does urban forestry relate to other relevant concepts and what are its strengths?
This paper aims to provide insight in how the concepts of urban forestry and urban forest have developed in North America and Europe.
Similarities and differences in history, definition, and use of the concept will be discussed.
This comparative analysis should aid international harmonization of urban forestry terminology.
Comparison and harmonization of urban forestry terminology Importance of terminology harmonization Terminology aims at clearly describing and delimiting the meaning of special language in a particular field of knowledge.
It distinguishes between concepts and terms.
Concepts are mental representations of objects within a specialized context or field not bound to particular languages, but influenced by social or cultural backgrounds.
Terms are words or expressions used to designate a single concept in the language of a specialized subject field (ISO 704, 2000).
Typically there is more than one term for a given concept.
The terms ‘woodland’, ‘bush’, ‘rainforest’ and ‘plantation’, for example, are all closely linked to the concept ‘forest’ (Randrup et al., 2005).
Definitions are verbal representations of concepts that identify the characteristics of a concept and permit its differentiation from other concepts.
There evoke considerable debate as experts might not agree on a common definition of a certain concept for strategic and other reasons (Lund, 2002).
Moreover, concepts change over time as conditions change (Schanz, 1999).
For example, the shift in societal appreciation of forest goods and services has also affected the definition of the forest concept (Helms, 2002).
Terminology harmonization is important in natural resource management, as for example, agreement on resource definitions is required for national and cross-boundary inventories and assessments.
Thus, harmonization aims for improved comparability, compatibility, and consistency among definitions, establishment of linkages, and a description of relationships among terms.
The harmonization process involves documentation of similarities and differences among definitions (FAO, 2002).
Framework for comparing urban forestry terminology The scope of urban forestry can be described by looking at three key components: the structural (or vegetation) elements included; the locations considered on the continuum urban, suburban, peri-urban and rural; and the benefits generated by urban forestry (Randrup et al., 2005).
These elements are considered in the present description and comparison of selected urban forestry terms for North America (here Canada and the United States only) and Europe.
However, definition of concepts is also highly dependent on the historical and cultural context.
The descriptions and comparison of urban forestry terminology in North America and Europe is structured as follows: The origins of urban forestry, including the role of different professions in introducing and developing the concept.
Definitions of urban forest and urban forestry.
Locations considered; what does the ‘urban’ in urban forestry stand for?
Relevant concepts with a close relation to urban forestry.
In this paper, the authors have based their assessment of urban forestry terminology on literature reviews and their personal experiences as members of national and international networks and research projects.
Development and definition of the urban forestry concept in North America The origins of urban forestry in North America It is well established that an explosion of activity in urban forestry occurred in the 1970s and 1980s and this may have led researchers to claim that urban forestry in North America got its start during this period (Johnston, 1996; Jorgensen, 1993; Miller, 1997; Koch, 2000).
Whereas volunteer involvement in urban forestry activities, such as tree planting, occurs throughout the history of the US (Campanella, 2003; McCullough, 1995), there is much evidence that urban forestry has its professional origins in the late 19th century and is tied to the beginnings of professional forestry (Ricard, 2005; Williams, 1989).
This historical oversight may be due to challenges of definition much like urban forestry is wrestling with today.
For example, ‘shade’ and ‘ornamental’ were words applied to public trees and the tasks associated with their protection and care throughout the 1800s (Campana, 1999).
In fact, since the late 1800s there have been urban forestry professionals who practiced at the municipal level but are identified as city forester, city arborist, municipal forester, municipal arborist, or tree warden (Harris et al., 2004; Jorgensen, 1986; Miller, 1997; Ricard, 2005).
Important landmark, urban forestry state legislation was also passed in the 19th century in the US.
For example, New Jersey passed a law in the 1890s that enabled communities to appoint shade tree commissioners (Kinney, 1972) and state laws in New England enabling or requiring municipalities to appoint a tree warden to care for public trees were enacted (Fernow, 1910; Ricard, 2005).
During the early and middle years of the 20th century, many states and municipalities had shade tree programs and professionals and there were also a number of shade tree conferences (Johnston, 1996); arboriculture has its professional origins during this period (Campana, 1999).
This activity may have been driven by the increasing number of introduced pests and diseases that were decimating both woodland and urban trees.
While no academic programs specifically identified as urban forestry or even arboriculture had yet developed as forestry had at the beginning of the 1890s, universities did produce faculty who devoted much of their careers to municipal tree care.
These academics and researchers occasionally became the entrepreneurs who founded several arboriculture companies and organizations (Johnston, 1996; Harris et al., 2004).
Urban forestry defined A true representation of what is urban forestry is historically contextual and has been a challenge to define.
A century since the first documented use of the term urban forestry first appears in 1894 (Cook, 1894), there have been numerous definitions developed.
These may have emerged in response to changing political and institutional environments.
Broadening the historically narrow definition of urban forestry is supported by studies that indicate that urban forests account for about 25 percent of the total land mass in the US (Dwyer and Nowak, 1999; Nowak et al., 2001).
McPherson (2003) states that most ecological measures used to describe forest structure can be applied to urban forests equally well.
Soil, climate (macro and micro), associated vegetation, fauna, and the built landscape vary significantly throughout urban areas.
Variations in urban forest structures change along urban-to-rural gradients that can be visualized from urban cores, through suburban developments, and into villages and rural areas.
The tree is the smallest unit in this scenario, and is managed in parks, along streets, and in median strips.
However, an increasing recognition of the environmental, economic and social benefits of the urban forests comprised of these individual trees (on private and municipal lands) in and around communities will continue to bring together the arboricultural approach to single-tree management with an ecosystem-based approach to urban forest management.
This need, for example, generated a landmark symposium of internationally acclaimed ecologists who coined the term suburban forestry (Waggoner and Ovington, 1962).
Jorgensen first used the term urban forestry in Canada in 1965 in response to interest from graduate students at the Faculty of Forestry, University of Toronto.
He provided the following definition in 1970 (Jorgensen, 1986, p.
173): Urban forestry is a specialized branch of forestry and has as its objectives the cultivation and management of trees for their present and potential contribution to the physiological, sociological and economic well-being of urban society.
These contributions include the over-all ameliorating effect of trees on their environment, as well as their recreational and general amenity value.
Urban forestry as a term appears in the title and the papers of the proceedings of several urban forestry conferences in the 1970s (e.g., Little and Noyes, 1971; SUNY-ESF, 1973).
Importantly, one of the first and widely quoted definitions of urban forestry in the modern era is provided in the federal Cooperative Forestry Act of 1978 as ‘… the planning, establishment, protection and management of trees and associated plants, individually, in small groups, or under forest conditions within cities, there suburbs, and towns’ (Miller, 1997, p.
This legislation is generally credited with launching the US Forest Service's direct involvement in urban forestry with states, municipalities, and non-governmental organizations (Robbins, 1985) and has been responsible for much of the recent expansion of urban forestry in the US, especially since 1990.
One of the more commonly cited definitions has been the one developed by the Society of American Foresters first in the early 1970s and more currently defined as ‘The art, science, and technology of managing trees and forest resources in and around urban community ecosystems for the physiological, sociological, economic, and aesthetic benefits tree provide society’ (Helms, 1998, p.
1) state that ‘Urban forestry is the management of planted and naturally occurring trees in urban and urban-interface areas.’ Miller (1997, p.
27) describes the urban forest as ‘the sum of all woody and associated vegetation in and around dense human settlements, ranging from small communities in rural settings to metropolitan areas.’ By extension then, urban forestry is the establishment and care of this resource.
Interestingly and uniquely, Miller (1997, p.
353) provides a definition of urban silviculture as …the art of reproducing and managing forests continuously to obtain sustained yields of forest benefits in urban regions through the application of ecological principles.
Traditional silviculture places emphasis on wood production, while urban silviculture has as primary functions recreation and environmental protection, but does not preclude wood fiber production.
The transition in management concepts from arboriculture to silviculture becomes somewhat arbitrary in urban forest management.
Care of individual trees is arboriculture and management of tree communities is silviculture, but in urban forestry a forest community may be manipulated as a whole, while a tree in that community receives individual attention.
In Canada, Ontario is the only province that specifically recognizes the practice of urban forestry in its legislation.
The Professional Foresters Act of 2000 (Province of Ontario 2000, Sec.
3) defines the scope of practice of professional forestry as ‘… the provision of services in relation to the development, management, conservation and sustainability of forests and urban forests where those services require knowledge, training and experience equivalent to that required to become a member under this Act.’ Membership refers to The Ontario Professional Foresters Association which regulates the practice of professional forestry through the Act (Sec.
3(1)) ‘in order that the public interest may be served and protected.’ This recognizes the importance of urban forests and their sustainable management to the public at large and not simply as trees adorning streetscapes and private yards.
The Act simply defines urban forests as ‘… tree-dominated vegetation and related features found within an urban area and includes woodlots, plantations, shade trees, fields in various stages of succession, wetland and riparian areas.’ (Sec.
The first Canadian Urban Forest Strategy was recently completed (Kenney, 2004).
This document has adopted a somewhat more detailed definition of urban forest than that used in the Ontario legislation.
The Strategy considers urban forests to be: ‘…trees, forests, greenspace and related abiotic, biotic and cultural components in and around cities and communities.
It includes trees, forest cover and related components in the surrounding rural areas (peri-urban forests).’ (CUFN, 2005).
Some practitioners believe that the urban forest consists only of those trees found in parks and along roads and streets that are under the jurisdiction of the municipality.
Since most of the ecological, social and economic benefits of the urban forest accrue to the community as a whole, then clearly the portion of the urban forest that is located on private property (as much as 80–90% of the forest (Sampson et al., 1992)) must also be considered.
The term municipal forest is sometimes used to differentiate this later component from the urban forest as a whole.
The term community forestry is sometimes combined with urban forestry as in ‘Urban and Community Forestry’.
In the United States, where this use is more common, the Cooperative Forestry Assistance Act of 1978 appears to use the terms interchangeably.
The United State Forest Service's Urban and Community Forestry website states ‘[the] Urban and Community Forestry Program enhances the livability of towns, communities, and cities by improving the stewardship of urban natural resources’ (USDA Forest Service, 2005).
Presumably, this is intended to reflect a more inclusive form in which the members of the community play a direct role in the management of their urban forest.
In Canada the term is less commonly used in conjunction with ‘urban forestry’.
When used in a stand-alone context, ‘community forestry’ more commonly refers to ‘forestry-dependent communities’ or those communities that have a strong economic dependency on the forest industry.
For example, Duinker et al.
(1994) provided an overview of community forestry in Canada which was strongly skewed to this use of the term with no mention of what we consider as urban forestry in the current discussion.
This division in urban and conventional forestry perspective is still strong in Canada and may reflect the gulf that still persists between what earlier definitions of urban forestry clearly recognized as two sub-disciplines of the same (forestry) profession.
Location – urban, peri-urban, rural Urban is increasingly defined as anywhere people live in communities (Bradley, 1995; Edwards and Bliss, 2003) and many of the definitions of urban forests and urban forestry used in North America recognize the discipline's jurisdiction into the interstitial areas between these communities.
As Jorgensen (1986, p.
178) points out ‘The politically established boundaries for municipalities rarely include the entire geographical area influenced by urbanization.’ Statistics Canada, the governmental body responsible for the national census, defines urban areas as areas with ‘…a minimum population concentration of 1000 persons and a population density of at least 400 persons per square kilometer, based on the current census population count.
All territory outside urban areas is classified as rural.
Taken together, urban and rural areas cover all of Canada.’ (Statistics Canada, 2001, p.
In some cases, the interstitial areas can be thought of as ‘rural’.
However, if we are to use the Statistics Canada definition of urban, then the entire country is either urban or rural.
Therefore, the interstitial areas would certainly be rural but so would areas clearly well beyond the direct influence of urbanization, of which Canada has plenty.
Interestingly, one author (Kenney) has experienced the wrath of ‘rural’ landowners who have escaped the city and are offended when it is suggested that their forested property 10 km from the city boundary is part of the urban forest!
In Canada, the term ‘peri-urban’ is gaining usage to describe the regions adjacent to urban areas and clearly under their influence.
Amalgamation of smaller municipalities has meant that the boundaries between urban forestry in the truly urbanized area and traditional forestry in the peri-urban areas have become blurred.
Since amalgamation, a municipal body must consider traditional forestry (or urban silviculture as described above) and the arboricultural approach to single-tree management.
Several peri-urban forests now fall under the jurisdiction of the same departments that traditionally had only dealt with street and park trees.
Development and definition of the urban forestry concept in Europe The origins of urban forestry in Europe Europe has had a long and rich history of greenspace design and management (e.g., Forrest & Konijnendijk, 2005).
Many cities, especially in Central Europe, have owned and managed nearby woodland for centuries, a phenomenon known as ‘town forestry’ in several languages.
Initially, many of the larger parks and gardens in cities and towns were established by the nobility and well-to-do and public access to these areas was very limited.
Although there are earlier examples of city authorities becoming concerned with providing public greenspace, more cohesive action emerged during the 19th century, when industrialization led to a boom in Europe's urban population.
Urban parks were seen as important contributors to the quality of urban life and the health of the – working class – population.
New greenspaces were established and existing and private parks and gardens were opened to the public during the second half of the 19th century.
The planning and management of public greenspace in Europe had been rather sectoral, with city parks, street trees, woodland, flowerbeds etc.
often having their own experts and/or municipal unit or department.
Only later did more comprehensive approaches to greenspace planning and management emerge, for example under influence of the fields of urban and landscape ecology, especially during the 1970s (Werquin et al., 2005).
Urban forestry was one of the concepts that also evoked interest as part of this ‘wave’ of more integrative and holistic perspectives.
Inspired by visits to the US and international conferences, British, Irish and Dutch experts were among the first introducing the term ‘urban forest’ to their country during the early 1980s (Johnston, 1997a, Johnston, 1997b; Konijnendijk, 2003).
City-wide urban forestry projects, based on North-American examples, were subsequently implemented in cities such as London and Belfast (Johnston, 1997a, Johnston, 1997b).
Urban forestry had to overcome initial resistance from foresters (who did not see cities as their domain) and the professions traditionally taking care of urban parks and trees (who where weary of outside interference; Johnston, 1997a).
Gradual recognition of the potential merits of the concept did follow, however, and the period from the mid-1990s saw various national as well as international networks develop that had urban forestry as a central theme.
Nordic activities (Randrup and Nilsson, 1996) developed into a European network of greenspace researchers financed by the European Union (COST Action E12 Urban Forests and Trees).
Its review of ongoing research illustrated the wide range of disciplines and fields of activity involved in urban forestry-related research.
Although about half of all projects were carried out by forestry institutions, other professions such as landscape architecture, (landscape) ecology, and horticulture were also major players (Forrest et al., 1999).
COST Action E12 and other networking activities stressed the importance of achieving common understanding between the many experts with their respective backgrounds on concepts and terms, and most importantly on the lead concept of urban forestry (Konijnendijk, 2003; Randrup et al., 2005).
Histories of European urban forests and forestry, such as those written by Johnston, 1997a, Johnston, 1997b, Konijnendijk (1997), and Forrest and Konijnendijk (2005) provide a background for understanding how the concept was adapted to European conditions.
Moreover, the large variety in approaches and definitions that exists until today can be explained from the diversity of European landscapes and cultures.
Urban forestry defined Europe is a continent characterized by diversity; it is a rich mixture of countries, regions, cities, traditions, cultures, languages, economic development and landscapes.
This is reflected in the difficulties to ‘translate’ the concept of ‘urban forest’ as a term into different languages and cultures.
The long history of town forestry, referring to the conservation and management of woodland owned by city authorities, makes direct translation of ‘urban forest’ difficult (Tyrväinen, 1999; Konijnendijk, 2003).
This may have contributed to the emergence of two main streams defining the urban forestry concept in Europe.
A ‘narrow’ definition links urban forestry primarily to urban woodland (forestry in or near urban areas).
A ‘broader’ perspective includes not only woodland, but also tree groups and individual trees, i.e. the tree-dominated part of greenspaces.
This broader perspective can be recognized from the definition of urban forestry provided by British experts in a European research overview: ‘Urban forestry is a multi-disciplinary activity that encompasses the design, planning, establishment and management of trees, woodlands and associated flora and open space, which is usually physically linked to form a mosaic of vegetation in or near built-up areas.
It serves a range of multi-purpose functions, but it is primarily for amenity and the promotion of human well-being’ (Ball et al., 1999, p.
Although this dichotomy of definitions is an oversimplification, overviews of definitions from across Europe in Forrest et al.
(1999) and Randrup et al.
(2005) do provide evidence for it.
Randrup et al.'s comparative overview of definitions of urban forest and urban forestry showed that virtually all elements of urban greenspace were referred to, be it not always to the same extent.
The majority of the definitions assessed focussed on woody elements, although in most cases non-woody structures were also referred to.
Over time, the concept of urban forestry as referring to a wider, tree-based green resource has become more accepted by European experts, even when the term might still evoke considerable debate (Randrup et al., 2005).
The definition of urban forestry by the former British National Urban Forestry Unit (NUFU, 1999, p.
4) illustrates the comprehensive concept of urban forest(ry) as often used today: ‘‘[the urban forest] collectively describes all trees and woods in an urban area: in parks, private gardens, streets, around factories, offices, hospitals and schools, on wasteland and in existing woodlands’.
Most definitions of urban forestry used in Europe stress its multifunctional character and tend to emphasize urban forest services rather than economic goods such as timber.
Those adhering to the ‘narrow’, forestry-based definition seem to stress biodiversity and recreational benefits of urban woodland (Randrup et al., 2005).
The environmental services provided by urban forests, such as moderation of the urban climate and air pollution reduction, are especially emphasized by those using the wider definition.
Recent years have seen increasing focus on many of the aesthetic and social benefits of urban forests, among which the impacts of urban trees and woods on human health and well-being (Tyrväinen et al., 2005).
This seems to be part of a trend to connect urban forestry issues to broader (urban) agendas and quality of life and environment issues (Ottitsch and Krott, 2005).
Urban forestry mostly has been regarded as a public sector activity, with focus on municipal woodland and other greenspace (Ottitsch and Krott, 2005), but increasing attention is given to the large share of urban trees on private lands, as also emerges from the NUFU (1999) definition provided above.
Location – from urban to urbanized The common denominator of definitions used in Europe is that vegetation within the built-up areas and/or administrative boundaries of larger settlements (cities, towns) should be included (Randrup et al., 2005).
The difficulty to define urban areas and especially to set their boundaries is discussed in a background document to the United Kingdom census 2001 (National Statistics, 2005).
The main ways for defining urban areas are: based on built-up area, based on functional area (i.e. including surrounding areas that depend on it for services and employment), and based on density of buildings or people.
But definitions in Europe vary widely; in Iceland, settlements with more than 200 inhabitants are considered urban (Benedikz and Skarphéðinsdóttir, 1999).
Most experts also seem to agree that not only woods and trees inside urban centres are to be included, but also those located in suburban and peri-urban areas.
But where does one draw the line?
In several studies in the Netherlands, for example, all forests for which decision-making processes were dominated by local urban stakeholders were regarded urban forests (Konijnendijk, 1999).
If urban forests include those woodland areas where urban demands are dominant, then even areas as far away as 100 km from the city centre might be considered, for example when they protect a city's drinking water resources.
Perhaps these more remote woodlands catering for urban populations, very common in Europe, should be defined as ‘urbanized forests’ rather than urban forests.
Related concepts – community forestry, neighbourwood, green-structure planning The term ‘community forestry’ has traditionally been applied as referring to rural areas and communities (Konijnendijk, 1999).
This changed, however, when a name had to be found for a new, national program of woodland and tree planting and management near metropolitan areas in England.
The term Community Forest was introduced to signalize that the new, peri-urban landscapes would be developed in close collaboration with and for providing benefits to local, urban communities (Johnston, 1997b).
The concept of community forestry also links back to the European heritage of town forestry.
Like rural communities, urban communities protected and managed their local woodlands in order to secure the goods and services these woodlands provided.
Other recently developed concepts have also picked up on this heritage, such as the concept of ‘neighbourwoods’.
A European research and development project defined the concept of neighbourwoods as referring to places where trees determine or are significant aspects of the visual, social, cultural and ecological character of the townscape (Salbitano et al., 2001).
The concept includes not only forests but also smaller treed areas (‘woods’), situated on people's doorsteps (‘neighbour’), and managed by and for the local community (‘our’).
The Irish Forest Service was the first to implement this concept in its policies and activities (Forest Service, 2001).
Additionally, a wide range of greenspace concepts have been developed that have no explicit link to urban trees.
‘Green structure’ and ‘green-structure planning’, for example, are concepts that have become established in many parts of Europe (e.g., Sandström, 2002; Tjallingii, 2002).
Green structures are seen as networks of green elements, as a physical infrastructure fulfilling many functions, such as playing a role in water management, protecting biodiversity, and providing a social infrastructure for leisure and the like (Werquin et al., 2005).
Very much in line with this integrative perspective, ‘green infrastructure’ refers to the functioning of the green structure, which provides various services in line with other ‘hard’ types of urban infrastructure (e.g., Davies, 2005).
Another comprehensive concept that has emerged recently is that of ‘urban greening’, originally defined in terms of ‘greening’ of cities with greenspace to improve their quality of life and environment (Kuchelmeister, 1998; Randrup et al., 2005).
Comparison of urban forestry definitions in Europe and North America Table 1 provides a brief comparative overview of the development and definition of the urban forestry concept in North America and Europe.
Greenspace planning and management have much older roots in both parts of the world.
The use of the term ‘urban forestry’ has a much longer history in North America than in Europe.
Finding ways of better, more comprehensive tree care and of dealing with pests and diseases have been major driving forces (Miller, 2004).
In Europe, the term has been applied on a wider scale only since the 1990s.
Its emergence was initially closely linked to Europe's heritage of ‘town forestry’ and the abundance of urban woodland resources.
Differences can also be seen when considering the involvement of various disciplines in the promotion of the urban forestry concept.
Foresters have played an important role on both continents, but arborists seem to have taken a more prominent role in North America than in Europe.
Comparison of origins and definition of urban forestry and related concepts in North America and Europe  Empty Cell	North America	Europe Origins First introduction	First mentioning in 1894; rapid development during 1960s and 1970s.
Main development as an independent (academic) field during 1980s; adapted from North America.
Important historical roots	Shade tree traditions and tree warden schemes.
Town forestry; long history of parks and garden design.
Important driving forces	Need to combat pests and diseases on urban trees.
Search for more integrative approaches.
Definition Domain of urban forestry (i.e. the urban forest)	All woody and associated vegetation in and around dense human settlements, ranging from small communities in rural settings to metropolitan areas.
Traditional focus on street trees.
‘Broad’ definition similar to North American approach.
‘Narrow’ definition focuses on woodland in and near urban centers (managed for amenity values), based on town forestry tradition.
Multidisciplinary character	Highly multidisciplinary.
Arborists have been more prominent than in Europe.
Highly multidisciplinary.
Foresters have played an important role from the town forestry perspective.
Multifunctionality	Urban forestry provides multiple goods and services.
Environmental services have been given increasing focus (e.g., air pollution reduction, climate moderation).
Urban forestry provides multiple good and services.
Social services have been prioritized (recreation, health).
Location ‘Urban’ defined	Urban has become defined very broadly.
Areas in, around and close to cities included in urban forestry.
Urban has become defined very broadly.
Traditional attention for peri-urban woodland areas.
Related terms Related terms that have emerged	Community forestry is increasingly used, often together with urban forestry.
Community forestry less frequently used.
Links to, e.g., greenstructure planning.
Terms such as urban woodland and neighbourwood have come into use.
Urban forestry has gradually become accepted in its broad, comprehensive form as referring to all woods and trees in and around urban centres.
Moreover, general recognition exists that no single profession can claim urban forestry, as it requires cross-sectoral and multidisciplinary approaches.
Still, definitions of urban forest and urban forestry are under debate and show great variety in both parts of the world.
In North America, Nowak and Dwyer (2000) describe urban forestry goals and outcomes as a range from maintaining a single historic public tree to increasing a city's canopy cover by a specific percentage over a specific period of time.
This, rather one-dimensional approach does not reflect the multiple benefits urban trees may have.
As a consequence, what urban forestry is remains somewhat elusive in spite of the diversity of opinions in the historical and modern literature (Edwards and Bliss, 2003).
On an operational basis, urban forestry remains mostly tree care, protection, and replacement because, perhaps, it still is mostly reactive (Groninger et al., 2002).
However, long-term, ecosystem-based approaches to urban forest planning are increasing (Bradley, 1995).
Definitions of the urban forest such as the one in the Canadian Urban Forest Strategy (CUFN, 2005) show this more comprehensive focus, by explicitly including ‘non-treed’ greenspaces.
How one defines urban forestry in North America today may originate one's personal, professional, and political values and motives (Haynes, 2002).
A city forester, for instance, may be inclined to view urban forestry more operationally since their day-to-day work focusses mostly on individual tree care along streets, roads, and parks.
On the other hand, there is a need for a broader view if all benefits of the urban forests are to be explored.
The European research community is also moving towards an understanding of the basic premises of urban forestry.
Moreover, the need to maintain flexibility in defining urban forestry reminds us of the situation in North America.
In ‘Urban Forests and Trees’, Randrup et al.
(2005) show that some common ground has been found, but that too rigid a definition of urban forestry may not be desirable in order to maintain the rich diversity of approaches in Europe.
(2005) suggest a basic framework for further development of the urban forestry concept in Europe which incorporates a wide range of urban forest locations (from paved to unpaved) and human activities (from design and planning to selection and establishment).
In this way it helps define the domain of urban forestry very broadly, recognizing its diverse character.
At the same time it is highly inclusive, inviting different professions and perspectives to play an active role in greenspace development, including the ‘the urban forestry community’.
Urban forestry's multifunctional focus is stressed both in North America and Europe.
The production function (timber) is mostly of minor importance, while social and, to an increasing extent, environmental services are in focus.
In Europe, especially social services, such as the aesthetic, recreational and health benefits of urban forests have had a central role.
Environmental services such as shading and cooling and reducing air pollution have so far been prioritized more in North America than in Europe, as the frequent (past) use of the term ‘shade trees’ also suggest.
On the other hand, many European cities have a long history of protecting nearby or even more remote woodland resources for safeguarding their drinking water resources.
Biodiversity protection is an important function of urban forests as well, although biodiversity is generally seen in the context of allowing urban inhabitants to stay in touch with nature and natural processes.
An important development in both Europe and North America concerns the ongoing attempts to link up urban forestry to wider urban development and environmental programs and policies.
The institutionalizing of urban forestry seems to have progressed further in North America (i.e. the United States), where urban forestry as a concept has become part of policy and legislation.
European countries do make reference to urban greenspace and peri-urban afforestation in their policies and legislation, but the concept of urban forestry is seldom used explicitly.
This could be a language issue, as the term urban forestry is still not very often used in Europe outside academic circles.
Ongoing urbanization has meant that more and more areas have come under direct and indirect urban influence, illustrated by phenomena such as suburbanization and urban sprawl.
This makes it difficult to define the geographical limits of urban forestry, as the traditional dichotomy between city and countryside is no longer very real.
Still, as emerged from North America, more rural municipalities are reluctant to see the term urban forestry being used in their case.
This has resulted in the use of urban and community forestry as an even more comprehensive concept.
It is clear that ‘urban’ can be defined in many ways and that the boundaries of what constitutes an urban area are hard to draw and fluid.
Countries and regions have different definitions of what is an urban area.
This will complicate harmonization of urban forestry terminology.
Community forestry has gained prominence in both parts of the world, although not in all countries.
In North America, the use of community forestry in a more urban context is stronger in the US than in Canada, while in Europe it has mostly been limited to the United Kingdom.
New concepts and terms have been emerging in both Europe and North America in order to take even more comprehensive perspectives of urban greenspace.
Concepts such as green structure and green infrastructure demonstrate how more functional and comprehensive perspectives have gained ground, for example to promote urban green issues at the same level as other municipal services and infrastructure.
The brief comparison of development and definition of urban forestry and related concepts in North America and Europe shows that in spite of differences, common ground exists for international harmonization.
There is wide support for a broad and holistic definition of ‘urban forestry’ and ‘urban forest’, one that incorporates ecological, economic, and sociological elements, and is inclusive of people from cities to suburbs to rural communities.
Recognition of urban forestry's multidisciplinary and comprehensive character can be used for further terminology harmonization.
How to balance this rather broad definition with more operational definitions to be used for, for example, natural resource inventories will pose a next challenge.
Abstract Abstract  Soil compaction can affect seedling root development by decreasing oxygen availability and increasing soil strength.
However, little quantitative information is available on the compaction tolerances of non-crop native species.
We investigated the effects of soil compaction on establishment and development of two New Zealand native species commonly used in restoration programmes; Cordyline australis (Agavaceae) (cabbage tree) a fleshy rooted species, and Leptospermum scoparium (Myrtaceae) (manuka) a very finely rooted species.
Seedlings were grown in a range of soil compaction levels in growth cabinet experiments.
Low levels of soil compaction (0.6 MPa) reduced both the number and speed of C.
australis seedlings penetrating the soil surface.
scoparium seedlings showed improved establishment at an intermediate compaction level.
Root and shoot growth of both species decreased with increasing soil strength, with L.
scoparium seedlings tolerating higher soil strengths than did C.
Despite these results, soil strength accounted for only a small amount of variation in root length (R2 < 0.25), due to greater variability in growth at low soil strengths.
Soil strengths of 0.6 MPa are likely to pose a barrier to C.
australis regeneration.
This is consistent with adaptation to organic and/or soft, waterlogged soils.
Active intervention may be necessary to establish C.
australis from seed on many sites previously in farmland.
INTRODUCTION Soil compaction occurs in a variety of rural and urban situations, as a result of a range of human activities, including construction work, the use of farm machinery, vehicular and pedestrian traffic, and trampling by livestock.
Soil compaction mainly affects plant development through increased soil strength, decreased oxygen availability, and altered (either increased or decreased) water storage and availability.
Greater mechanical resistance increases the force required for the plant root to push its way through the soil.
This is compounded by the reduction in size and continuity of soil macropores through which roots preferentially grow (Kozlowski 1999), leading to slower root elongation, reduced root length and reduction in soil volume exploited (Materechera et al.
1991; Panayiotopoulos et al.
A soil strength of 2 MPa is commonly cited as limiting for the growth of crop plants (Materechera et al.
1991; Day & Bassuk 1994).
However, the literature also shows plant species vary considerably in their tolerance of soil compaction.
The seedling stage may be particularly vulnerable to compaction, with increased soil strength delaying both germination and penetration of the soil surface by the radicle (Court 1985; Smith et al.
2001; Soyelu et al.
A reduction in the volume and continuity of soil pores may decrease oxygen availability, and allow build up of toxic gases (Hillel 1971).
Ten per cent air-filled porosity at −10 kPa tension is commonly cited as limiting for plant growth (Day & Bassuk 1994; Penfold 1998; Drewry & Paton 2000), although this is influenced by factors such as soil temperature, water table height and plant adaptations.
Impeded drainage may exacerbate oxygen deficits within the soil, as water takes up more of the available pore space.
Compaction may also reduce infiltration of water into the soil, thus increasing run-off and mechanical resistance.
Restricted rooting may disadvantage the plant in a number of ways; plants may be more susceptible to drought and environmental fluctuations (Liang et al.
1999), or nutrient deficiencies of particularly immobile nutrients such as phosphorus (Greacen & Sands 1980).
Reduced seedling growth may further contribute to restricted natural regeneration at compacted sites by decreasing competitiveness and increasing susceptibility to weed invasion.
Restricted rooting may impair plant anchorage, increasing susceptibility to wind throw (Kodrik & Kodrik 2002).
Soil compaction may present a barrier to seedling establishment and growth where land managers seek to re-establish native vegetation communities.
However, a lack of quantitative information means it is difficult to assess the extent to which compaction may be affecting regeneration or restoration of native species.
Although much restoration activity within New Zealand is based on container grown plants, effects of soil compaction on seedling establishment and early growth may be important where direct seeding techniques are utilized, and also where natural regeneration is anticipated.
The reported research aimed to assess the effects of soil compaction on the establishment and early growth of Cordyline australis (G.
(Agavaceae) (cabbage tree) and Leptospermum scoparium J.R. et G.
Forst., (Myrtaceae) (manuka) seedlings.
Both are light demanding species widely distributed throughout New Zealand (Metcalf 1991; Simpson 2000), and commonly used in the early stages of revegetation projects.
MATERIALS AND METHODS Three growth cabinet experiments investigated the establishment and growth of C.
australis and L.
scoparium seedlings in a range of soil compaction levels.
Compaction levels were then compared with topsoils within Tawharanui Regional Park, Auckland, to illustrate the likely implications for ecological restoration.
Soil Two soils were used in the study, as compaction has been shown to affect plant growth differently in different soils (McQueen et al.
1994): a Brown Soil (silty clay loam), and an Ultic Soil (silty clay) in the New Zealand Soil Classification (Hewitt 1998).
The relationship of dry density to water content at compaction was assessed using the Soil Bureau Mini Compaction Method (Thomas 1973), to establish the water content at which optimal compaction was achieved for each soil (42% w/w for the Brown Soil and 46% w/w for the Ultic Soil).
Soils were packed into sections of polyvinyl-chloride pipe (200 mm in length, with an internal diameter of 70 mm), in four layers, with cloth taped over the bottom.
The upper surface of each but the top layer was scarified with tweezers to prevent distinct layers forming.
The top layer was cut flush with the surface of the pipe.
Experiment 1 The first experiment was a hierarchical design, with the two soils each being compacted to two bulk density levels.
At each bulk density level there were two air-filled porosity levels, resulting in eight different treatments.
Bulk densities were 0.7 Tm−3 for uncompacted treatments, with compacted treatments being 0.86–0.9 Tm−3 in the Brown Soil and 0.87–0.91 Tm−3 in the Ultic Soil.
All compaction levels tested fell within the range of values reported for Brown and Ultic Soils in the field within the Auckland region (Landcare Research 2003; R.
Tubes were brought to saturation overnight, then drained to pre-determined water contents equating to 20% or 15% air-filled porosity (AFP) for uncompacted soil and 5% and 10% AFP for compacted soil.
Experiments 2 and 3 A second experiment investigated C.
australis seedling responses to three levels of soil compaction, each with a single AFP level, but otherwise following the methodology outlined for Experiment 1 (Table 1).
A third experiment examined the responses of L.
scoparium seedlings to these three levels of soil compaction (Table 1).
Experimental treatments and mean soil physical properties Physical property (mean)	Compaction Level Uncompacted (0 hammer blows)	Moderately compacted (5 hammer blows)	Highly compacted (10 hammer blows) Brown Soil	Ultic Soil	Brown Soil	Ultic Soil	Brown Soil	Ultic Soil Cordyline australis  Bulk density (Tm−3)	 0.71	 0.70	 0.84	 0.84	0.91	0.91  Air-filled porosity (% v/v)	20	20	10	10	5	5  Penetration resistance (MPa)	 0.33	 0.17	 0.43	 0.56	1.24	0.75 Leptospermum scoparium  Bulk density (Tm−3)	 0.72	 0.71	 0.83	 0.77	0.88	0.90  Air-filled porosity (% v/v)	20	20	10	10	5	5  Penetration resistance (MPa)	 0.21	 0.20	 0.50	 0.40	1.00	1.15 Plant treatments and maintenance Seeds of both species were collected from plants growing in regenerating bush on well to imperfectly drained soil on Auckland's North Shore.
Seeds were removed from C.
australis fruit flesh prior to germinating, as the presence of pericarp tissue was expected to impair germination (Fountain & Outred 1991; Burrows 1995).
australis seed weight was 0.004 g (std dev 0.0016 g).
Unusually large or small seeds were discarded to minimize variation in growth resulting from differences in seed vigour.
Seeds were surface sterilized, soaked overnight, and germinated on moist filter paper in Petri dishes in a growth cabinet under 16 h days, with day/night temperatures of 22/18°C.
Germination commenced within 2 days of soaking.
Seeds that had failed to germinate after 4 weeks were discarded.
scoparium capsules were air-dried for 1 week, initiating seed release.
Seeds were treated as for C.
Germination began after 5 days and was completed by day 14.
Two pre-germinated C.
australis seeds, with radicles between 0 and 2 mm in length, were placed on the soil surface of each tube.
scoparium experiment, three seedlings were placed on the surface of each tube, with each seedling less than 2 mm long.
Tubes were arranged in a stratified random design within a growth cabinet (16 h days; day/night temperatures 20/18°C; humidity 80%; irradiance 122 µmol/s m−2 PAR).
Tubes were watered daily.
Every second day each tube was weighed and the water level adjusted to its predetermined level to maintain the desired AFP.
Weeds were regularly cut off at the soil surface.
Seedlings were grown until establishment was largely complete: 34 days in Experiment 1, 27 days in Experiment 2 and 34 days in Experiment 3.
Radicle penetration of soil surface was assessed daily for C.
australis seedlings.
Establishment, defined as when the seedling was able to hold itself upright and was visibly anchored in the soil, was measured for L.
scoparium seedlings.
At the end of each experiment shoot height was measured, from the hypocotyl to the furthest leaf tip for C.
australis, and from the hypocotyl to the furthest leaf node for L.
Root length was measured from the hypocotyl to the furthest root tip for both species.
Soil analysis At the end of each experiment penetration resistance was measured in seven tubes from each treatment, at the water content at which the tubes had been maintained during the experiment, using a Proctor Penetrometer (Model CN-433).
Bulk density and air-filled porosity at −10 kPa were measured on the remaining tubes by tension plate analysis.
This indicated that some settling had occurred in the uncompacted soil, leading to a mean increase in bulk density of 0.03 Tm−3.
Data analysis Results were analysed using R data analysis programme (Ihaka & Gentleman 1996).
Fisher's Exact test was used to test significance where data could be treated as 2 × 2 or 2 × 3 contingency tables of discrete variables falling into mutually exclusive categories (such as survived and died).
Differences in root length and shoot height were analysed using Wilcoxon Rank Sum test.
Regression analyses were used to investigate the relationships between seedling growth and soil strength or AFP, with the data from the two C.
australis experiments being combined for these analyses.
Assessment of soil compaction in the field Five vegetation categories ranging in time since cessation of grazing were chosen within Tawharanui Regional Park, 90 km north of Auckland (grid reference NZMS R09 764345).
These were: currently grazed kikuyu (Pennisetum clandestinum Hochst.
ex Chiov.) pasture, kikuyu from which stock had been excluded for approximately 8 years or 11 years, and native forest from which stock had been excluded for approximately 16 years or 30 years.
Two sites were chosen in each vegetation type.
All sites were gently sloping and topographically low, approximately 20 m above sea level.
The soil at all sites was a Brown Soil (Marua silty clay loam) (Sutherland et al.
1980; Noble 1990).
Four intact soil cores 100 mm in diameter and approximately 75 mm deep were taken at each site from mineral soil 5–80 mm depth, producing a total of eight cores for each vegetation category.
Bulk density and air-filled porosity at nominal field capacity (−10 kPa) were measured by tension plate analysis.
Penetration resistance was measured at this nominal field capacity.
RESULTS Establishment and survival The ability of C.
australis seedlings to penetrate the soil surface was inversely related to the level of soil compaction (Table 2, Fig.
Increased compaction also increased time to penetration for C.
australis seedlings (Table 2).
In contrast, fewer L.
scoparium seedlings established in the uncompacted compared to both compacted treatments (Table 2).
Over 90% of all L.
scoparium seedlings established between days 3 and 7, and there was no evidence that compaction influenced the speed of L.
scoparium establishment (Table 2).
Establishment and survival of C.
australis and L.
scoparium seedlings in three compaction levels Compaction Level Uncompacted	Medium	High C.
australis  Seedlings penetrating soil surface (%)	96***	50***	27***  Mean time to penetration (days)	 3.6***	 5	 5 L.
scoparium  Seedlings establishing (%)	52*	76	63  Mean time to establishment (days)	 5	 7	 6  Survival (%)	46*	74	74 Significant differences shown by *P < 0.05; **P < 0.01; ***P < 0.001.
Details are in the caption following the image Figure 1 Open in figure viewer PowerPoint Penetration of the soil surface by Cordyline australis seedling radicles at a range of soil compaction levels.
( inline image) Uncompacted, () moderately compacted, () highly compacted.
Increased compaction only reduced C.
australis survival in the first experiment (Fisher's Exact test, P < 0.001).
scoparium seedling survival was lower in the uncompacted than compacted treatments (Table 2).
Soil type did not affect the number of seedlings establishing.
However, both species showed higher mortality in the Brown than Ultic Soil (Fisher's Exact test, P = 0.004 for C.
australis, and P = 0.021 for L.
Root length Cordyline australis root length was inversely related to compaction (P < 0.001, d.f. = 51, Table 3, Fig.
Root length at 0.6 MPa was ≤ 27% of the maximum length obtained in the experiments.
Root length was more variable at low soil strengths than at high strengths.
Seedlings growing in compacted treatments not only showed delayed penetration; following penetration, root growth was also slower.
Mean root growth per day decreased steadily with increasing compaction (one-way anova, d.f. = 20, P = 0.038).
australis root length exhibited a weak positive linear relationship with air-filled porosity (P = 0.007, d.f. = 51, Fig.
Maximum root length was greater in the lower of the two AFP levels at each bulk density in Experiment 1, suggesting that seedlings in these treatments were responding to the softer soils provided by higher water contents.
australis and L.
scoparium root and shoot lengths at a range of soil compaction levels Compaction level Uncompacted	Medium	High C.
australis root length (mm)	38***	16***	7*** C.
australis shoot height (mm)	35***	16***	7*** L.
scoparium root length (mm)	23*	15	9 L.
scoparium shoot height (mm)	 6*	 5	4 Significant differences shown by *P < 0.05; **P < 0.01; ***P < 0.001.
Details are in the caption following the image Figure 2 Open in figure viewer PowerPoint Cordyline australis seedling root length as a function of soil strength, as measured by penetration resistance.
Details are in the caption following the image Figure 3 Open in figure viewer PowerPoint Cordyline australis seedling root length as a function of soil air-filled porosity.
Although fewer L.
scoparium seedlings established in the uncompacted treatments, those that did establish had longer primary roots than those in compacted treatments (Table 3).
Leptospermum scoparium root length was negatively related to penetration resistance (P = 0.002, d.f. = 59, Fig.
4), and weakly positively related to air-filled porosity (P = 0.002, d.f. = 59, R2 = 0.16) in linear models with very low R2-values.
Details are in the caption following the image Figure 4 Open in figure viewer PowerPoint Leptospermum scoparium seedling root growth as a function of soil strength, as measured by penetration resistance.
Shoot height Reductions in C.
australis root length were mirrored in reduced shoot height, which was related to penetration resistance by a linear model (P = 0.0092, d.f. = 59, Fig.
A shoot height of 20 mm was used to mark the cut-off between poorly and strongly performing (‘large’) seedlings.
Increasing soil compaction reduced the number of ‘large’ seedlings, with no seedlings in the highly compacted treatment exceeding 20 mm (three-way Fisher's Exact test, P = 0.011, Table 3).
Details are in the caption following the image Figure 5 Open in figure viewer PowerPoint Cordyline australis seedling shoot height as a function of penetration resistance.
Leptospermum scoparium seedling height growth was depressed in the high compaction treatment compared to in the uncompacted soil (t-test, P = 0.042, Table 3).
Shoot height was negatively related to penetration resistance in a linear model (P = 0.02, d.f. = 60, R2 = 0.16) given by the equation:  Shoot height = −1.85x + 6.39, where x  =  penetration resistance.
A linear model showed no evidence of a relationship between L.
scoparium shoot height and AFP.
Field compaction at Tawharanui Regional Park Penetration resistance at nominal field capacity decreased exponentially with time retired from grazing (P < 0.001, Fig.
Only the 30 years fenced forest sites consistently had soil strengths below 2 MPa at nominal field capacity, although values were above the 0.6 MPa shown in the growth cabinet experiments to restrict C.
australis establishment.
The 30 years sites did, however, have well developed humic layers above the mineral soil sampled in the cores.
Air-filled porosity at nominal field capacity was above 10% (v/v) at all sites, indicating that AFP is unlikely to be limiting for plant growth.
Details are in the caption following the image Figure 6 Open in figure viewer PowerPoint Changes in soil strength, as measured by penetration resistance (at nominal field capacity, −10 kPa), with increasing years of stock exclusion, Tawharanui Regional Park.
DISCUSSION Seedling establishment The ability of a plant community to regenerate is one of the key ecosystem functions often used as an indicator of ecosystem health.
The negative relationship between soil strength and successful penetration of the soil surface by radicles of C.
australis seedlings is consistent with the findings of Smith et al.
(2001) with spotted- and red flowering-gum seedlings.
Cordyline australis seedlings appear to be more sensitive to soil strength than other species.
Delayed establishment has the potential to further decrease C.
australis recruitment in the field due to higher risk of seedling mortality from disturbance, pathogens, predators and desiccation.
Improved establishment and survival of L.
scoparium seedlings in moderately compacted soil suggests it is more tolerant of compaction than C.
This disparity is consistent with the wider literature and may partly reflect morphological differences between C.
australis and L.
The thicker roots of C.
australis may be less able to initially penetrate the soil surface than the fine roots of L.
scoparium, as root growth through the soil occurs either by pushing aside soil particles, or growing through existing pores (Costantini et al.
Thick kohekohe (Dysoxylum spectabile) taproots had difficulty penetrating the surface of compacted soil (Court 1985).
(2001) also found that seedlings of thicker rooted tree species showed a greater tendency towards surface rooting, being less able to penetrate the soil surface.
Seedling growth The negative exponential relationship of C.
australis root length to penetration resistance is consistent with the literature.
However, the soil strengths that limit C.
australis root growth are well below the 0.9–5 MPa reported for a range of crop and tree species (Greacen & Sands 1980; Glinski & Lipiec 1990; Materechera et al.
1991; Day & Bassuk 1994; Costantini et al.
1996; Zou 1999).
Rice (Oryza sativa) was the only species restricted at comparable soil strengths.
Both rice and C.
australis are adapted to withstand waterlogged environments, typified by low soil strengths.
The response of L.
scoparium, a plant of both wet and dry soils, is comparable to seedlings of four Australian landscape trees, which had a median root length of approximately 40% of the uncompacted median at soil strengths of 1.5 MPa (Smith et al.
Although soil strength had a highly significant effect on root length and plant establishment, very low R2-values indicate other factors also influenced seedling response.
This may result partly from very high variability in growth in uncompacted soils, possibly as a result of genetic variation.
In contrast, growth of most seedlings was restricted in compacted soils.
These experiments examined AFP levels above and below the 10% generally considered limiting for plant growth.
australis seedlings may be adapted to AFP levels well below 10%, with the relationship of seedling growth to AFP in part due to the effect of soil strength, as these two factors were not independent.
This is in considerable contrast to Pinus radiata seedlings, which displayed a 10% reduction in root length when AFP was as high as 16%, with growth steadily declining with reductions in AFP (Penfold 1998).
Results indicate that restoration techniques involving direct application of C.
australis seed should be restricted to sites with moist, soft soils, or high seeding rates used to produce enough seedlings.
The lower sensitivity of L.
scoparium to soil compaction suggests that moderate soil compaction may not reduce the effectiveness of techniques such as laying L.
scoparium branches with seed capsules on the soil surface.
However, absolute growth rates of C.
australis seedlings in soils approaching 1.4 MPa were similar to those exhibited by L.
scoparium in the uncompacted soils over the same time period, even though L.
scoparium shoot growth was less sensitive to compaction.
scoparium is not necessarily a more attractive option for restoration on compacted soils, as C.
australis has high potential shoot rates in compacted soils where high water contents reduce soil strength.
Longer-term research would be required to determine if the initial establishment advantage of L.
scoparium is maintained, given this slower initial height growth rate.
At Tawharanui Regional Park, even sites retired from grazing for over 15 years had topsoil strengths consistently well above those found to severely restrict C.
australis establishment.
australis regeneration was observed in these areas.
scoparium seedlings were observed in pasture sites retired for more than 8 years, which is consistent with their greater ability to establish in compact soil.
However, other factors, such as different microclimate requirements, and differential dispersal ability between the wind dispersed L.
scoparium and the bird dispersed C.
australis may also have contributed to observed differences in regeneration within the Park.
However, soil compaction is likely to be a barrier to re-establishment of C.
australis in pasture and other compacted sites.
A number of techniques may be useful in minimizing this problem.
Fencing of such areas not only protects plants from browsing by livestock, but also provides suitable soil conditions for regeneration as soft humus layers develop.
Mechanical loosening of soil may improve plant growth.
Further research is required into the long-term growth responses of native species to soil compaction, as results from this study cannot be extrapolated to larger plants, and it is possible that by-passing the establishment phase by planting larger, pre-established plants may minimize the negative effects of soil compaction.
Introduction The ominous status of coral reefs worldwide and active reef restoration Once acknowledging the vital ecological importance of coral reefs and their fundamental roles in sustaining hundreds of millions of people, it is dismaying to realize that over the last four decades ca.
40% of the global coral-reef system has been lost, a process galloping at 1–2% per year [1], not considering the developing global change impacts that are exacerbated by severe anthropogenic pressures.
Thus, coral reefs, while exhibiting exceptional species diversity, are poorly protected, highly degraded, and exposed to multiple persisting and envisaged threats [2, 3].
The stressors, and notwithstanding all traditional conservation management measures implemented [4], would lead to loss of up to 70% of reef area within four decades or to phase shift [1].
The above causes that have led to progressive impairment of the normal course of coral-reefs life and their global contribution to humans, without proper damage control or repair, have prompted the demand for alternative active reef restoration measures, beyond the traditionally employed conservation.
Restoration is defined by the Society of Ecological Restoration as ‘the process of assisting the recovery of an ecosystem that has been degraded, damaged, or destroyed’ [5]; it has also been acknowledged that restoration activities may complement [6], even substitute conservation efforts.
Whereas the restoration rationale is rooted in active approaches to solve ecosystem degradation (‘Ecological restoration is an engaging and inclusive process’; [5]), conservation biology endeavors preservation, counting on long-term ecological succession as the major repairing mechanism for impacted ecosystems.
The literature documents that ecological restoration is a fast developing scientific discipline.
Heeding the invaluable lessons gathered from the failures of traditional conservation, the declaration of the Convention on Biological Diversity that restoration of terrestrial, inland water and marine ecosystems is essential for rehabilitating the ecosystem's functioning, goods and services [6], confirms the wide scientific support of ecological restoration efforts.
In fact, the extent of anthropogenic and global change impacts on coral reefs worldwide renders their active restoration as a major conceptual and practical approach, not just as assistant act to traditional conservation acts [4, 7, 8].
Restoration practices for degraded reefs can be broadly categorized into passive or active restoration [4, 7, 8].
Active restoration, or active human intervention in degraded reef sites, disputes passive restoration, the dependency on natural regeneration and repair with minimal human surrogacy.
Indeed, when analyzing globally employed passive restoration measures, it is evident that the reef management acts have been imperfect, failed to ascertain the right responses to key threats, failed to yield a quantifiable return and are ineffective in ameliorating long-term impairments [4, 7, 8].
More pressing is the realization that regardless of the implication of either practice, the restored ‘reefs of tomorrow’ will be different from the current or past reefs’ constructions (Figure 1).
Download: Download full-size image Figure 1.
Figure depicts multiple ‘restored reef-state’ scenarios (circles no 3–7) showing paths from a degraded reef (low ecological complexity and minimal reef services; circle 2) toward a healthy reef (circle 1), passing through two types of unsuccessful measures (circles 6, 7) and several restored status (circles 3–5).
The unsuccessful measures represent attempts (a) aiming to boost reef services (such as installing artificial reefs for fisheries; circle 6) or whole colonies transplantation acts [9] and (b) aiming to increase biodiversity, such as the concept of ‘assisted colonization’ [10•] (circle 7).
In both scenarios it is more likely that reef environments will revert to their degraded status than advance toward a better state (marked by question marks).
Three different scenarios employing the ‘gardening concept’ [4, 7, 8, 9, 12••, 13, 14, 15•, 16, 17, 18, 19, 20, 21, 22, 23] are defined.
These may result in rehabilitated reefs at different complexity/reef services states (circles 3–5) that could develop into other states and possibly (question marks) will culminate with the primeval reef status.
The gardening tenet Several approaches for active restoration have been suggested; some have been subjected to intensive research manipulations.
One of the first advocated methodologies was the direct transplantation of coral material (entire coral colonies and/or fragments), an approach subjected to a wide range of limitations and pitfalls, such as negative impacts on donor reefs and on transplanted coral colonies [8, 9].
A comparable, more recent approach is the controversial tool of ‘assisted colonization’ or ‘managed relocation’ [reviewed in 10•], claiming active translocation of groups of species outside the species’ historic range for conservation purposes.
One of the most promising active restoration approaches is the ‘gardening concept’ [4, 7, 8, 9], which has surfaced as a means to avoid the pitfalls associated with the traditional management for coral reefs (e.g., reduced negative impacts on donor reefs, high survivorship of transplanted coral colonies, improved state of health of transplants, year round availability of transplants).
This strategy, which derives its rationale from silviculture, is guided by a two-step restoration operation.
The first step entails rearing stocks of small coral fragments in specially designed mid-water floating nurseries, and upon reaching suitable sizes, applying the second step, the transplantation of nursery-farmed coral colonies onto denuded reef areas.
As restoration ecology is rooted in forestation, it is therefore not surprising that silviculture principles, concepts and theories, are intermingled within the ‘gardening’ notion and its associated activities.
During the almost two decades from their first presentation [9], the two gardening tenet steps have been tested in various reefs worldwide (Table 1 discusses the nursery step; studies performed in the Red Sea, Thailand, Singapore, Philippines, Tanzania, Mauritius, Seychelles, Caribbean sites [Jamaica, Florida keys, Colombia, Belize, and more], Japan, Taiwan, Hawaii; much of the outcomes is still unpublished [3, 11, 12••, 13, 14, 15•, 16, 17, 18, 19, 20, 21, 22, 23]).
List of coral species farmed in coral nurseries worldwide ([13, 14, 18, 19, 20, 21, 22, 23, 24•, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], unpublished).
C, Caribbean sites (pooled); E, Eilat, Red Sea; H, Hawaii; J, Japan; M, Mauritius; P, Bolinao, the Philippines; Se, Seychelles, Si, Singapore; T, Taiwan; TP, Phuket Island, Thailand; ZM, Zanzibar and Mafia Islands, Tanzania  No	Coral species	E	P	TP	Si	Se	ZM	M	H	C	J	T 1	Acanthastrea brevis					+						 2	Agaricia agaricites									+		 3	Acropora aspera			+								 4	Acropora austrea							+				 5	Acropora cervicornis									+		 6	Acropora cytherea		+			+						 7	Acropora digitifera				+							 8	Acropora eurystoma	+										 9	Acropora formosa		+	+			+	+				 10	Acropora grantis			+								 11	Acropora hemprichii	+					+					 12	Acropora humilis	+										 13	Acropora hyacinthus		+		+	+						 14	Acropora intermedia										+	 15	Acropora irregularis					+						 16	Acropora lamarcki	+										 17	Acropora macrostoma		+									 18	Acropora millepora				+							 19	Acropora muricata						+					 20	Acropora nasuta						+					 21	Acropora palmata									+		 22	Acropora pharaonis	+										 23	Acropora pulchra			+								+ 24	Acropora selago							+				 25	Acropora squarrosa	+										 26	Acropora tenuis										+	 27	Acropora valida	+	+		+							 28	Acropora variabilis	+										 29	Caulastrea furcata				+							 30	Cyphastrea microphthalma	+										 31	Diploastrea heliopora				+							 32	Diploria labyrinthiformis									+		 33	Echinopora hirsutissima					+						 34	Echinopora lamellosa		+	+								 35	Eusmilia fastigiata									+		 36	Favia favus	+										 37	Galaxea fascicularis	+						+				 38	Goniastrea aspera	+										 39	Goniopora savignyi	+										 40	Heliopora coerulea		+		+							 41	Hydnophora exesa	+										 42	Hydnophora rigida				+							 43	Madracis mirabilis									+		 44	Merulina scabricula		+									 45	Millepora complanata									+		 46	Millepora dichotoma	+					+					 47	Montastraea annularis									+		 48	Montastraea cavernosa									+		 49	Montipora aequituberculata		+	+								 50	Montipora capitata								+			 51	Montipora digitata		+		+			+				 52	Mycedium sp.
+							 53	Oulastrea crispata				+							 54	Oxypora sp.
+							 55	Pachyseris speciosa				+							 56	Pavona cactus	+	+		+			+				 57	Pavona danai							+				 58	Pavona decussata							+				 59	Pavona frondifera		+									 60	Pectinia lactuca				+							 61	Physogyra lichtensteini				+							 62	Platygyra sinensis				+							 63	Pocillopora cylindrica						+					 64	Pocillopora damicornis	+	+	+	+	+	+	+	+			 65	Pocillopora eydouxi					+						 66	Pocillopora verrucosa					+	+					 67	Podabacia sp.
+							 68	Porites astreoides									+		 69	Porites compressa								+			 70	Porites cylindrica						+					 71	Porites deformis				+							 72	Porites divaricata									+		 73	Porites lobata					+						 74	Porites lutea	+			+							 75	Porites palmata							+				 76	Porites porites									+		 77	Porites rus		+	+								 78	Porites sillimaniana				+							 79	Psammocora digitata				+							 80	Psammocora digitifera				+							 81	Seriatopora hystrix	+										 82	Siderastrea siderea									+		 83	Stylocoeniella sp.
+							 84	Stylophora pistillata	+				+						 85	Turbinaria peltata				+							 86	Turbinaria sp.
+										  Species/locality	21	14	8	26	10	9	10	3	13	2	1 The nursery phase of the ‘gardening concept’ has been drawing the most scientific investigation, conceptually and technically addressed in detail, with at least 86 coral species farmed in underwater nurseries, worldwide (117 species when total farmed species in all nurseries is considered, Table 1; only species from literature and personal communication are listed).
Issues, such as nursery structure, nursery types, nursery's set-up, shape and construction, nursery location, maintenance subjects, coral species cultured (types, numbers) and genotypic considerations, spacing of farmed coral colonies, realistic number of generated and farmed colonies, duration of the nursery phase, growth rates of farmed corals, longevity of farmed colonies, pest control and economic considerations are some of the topics studied recently.
The second phase of transplantation, which is still in its infancy, has also revealed promising results ([12••, 13, 14, 15•], unpublished).
The major conclusion which emerged from the above studies is that the application of active restoration protocols may enhance reef recovery [4, 7, 8].
The results obtained from various reefs worldwide cumulatively have revealed that the gardening tenet, with modifications and adjustments per local conditions, can be used as a ubiquitous management instrument for rescuing reefs from the on-going degradation (Box 1).
Box 1 Major considerations when approaching reef restoration project under the ‘gardening concept’ What is needed to know?
• Primeval local reefs’ status  • Getting acquainted with key/dominant species biological patterns  • Population genetics of local species  • Past bleaching events and disease outbreaks, including consequences  • Conferring on connectivity trajectories, resistance/resilience attributes, top-down/bottom-up controls  • Quantified reef services; defined reef stakeholders  • List of natural/anthropogenic threats  • Anticipated climate change impacts  • Evaluation of current conservation acts Issues to be considered:  • Some reefs might not need active restoration (highly resilient/resistant reefs)  • Some reefs should not be restored (reefs under severe anthropogenic impacts)  • Vision for the status of the ‘reef of tomorrow’ for each locality  • Pre-planning of nursery/transplantation scenarios and colonies/genotypes/species numbers  • Different spatial/temporal reef-features require different restoration methodologies  • Close monitoring of each of the restoration acts  • Flexible to revise/change approaches not successfully developed What has been learnt recently from nursery/transplantation acts?
Studies [11, 12••, 14, 15•, 16, 17, 18, 19, 20, 21, 22, 23, 24•] have already revealed that farmed corals not only compete successfully with natural colonies’ performance, but also exhibit improved health status, being free of parasites and diseases (developed and maintained under controlled conditions), with high survivorship under natural reef conditions, and year-round availability, circumventing the need to explore sites for harvesting additional material [3, 12••, 24•].
The mid-water floating nurseries have already been established as a successful farming tool.
It is estimated that >100 000 colonies from 86 coral species (Table 1) of various forms (branching, massive and encrusting species) have already been farmed in these nurseries, worldwide, showing minor mortalities and enhanced growth rates.
These nurseries are usually installed in a protected site, away from major natural reef structures, away from the afflictions of recreational activities and corallivorous organisms.
Under these excellent conditions, fragments from many coral species grew to large colonies within 1–1.5 years [7, 15•, 16, 17, 18, 19, 20, 21, 22, 23].
Furthermore, floating coral nurseries (Figure 2) unexpectedly revealed: (a) that swinging in all directions enhances food and oxygen supplies and facilitates clearing of debris and sediment particles that might accumulate on farmed coral colonies [3, 19]; (b) reduced sedimentation fluxes, since nurseries are above substrate; (c) depth adjustment, ‘tailored’ for any species-specific needs, also allowing acclimatization of farmed corals to conditions in their designated transplantation site [3]; (d) mid-water nursery attracts commensals and coral inhabiting species arriving from the plankton, for the establishment of the entire coral infaunal biodiversity [19]; and (e) early onset of sexual reproduction in farmed corals, changing the nursery into ‘larval dispersion hub’ that can be used as a management tool for natural recruitment enhancement [11].
Above themes attest that the tool of a floating nursery could serve as a ubiquitous platform for developing restoration protocols applicable on a global scale.
Download: Download full-size image Figure 2.
The nursery (a,b,c) and transplantation (d,e,f) phases of the ‘gardening notion’.
(a) Eilat's (Red Sea) underwater prototype coral nursery at the beginning [16, 17].
This nursery is located at 6 m depth, 14 m above sea bottom in blue, clear water.
The nursery is made with rope net (10 m × 10 m size) as the nursery basis (may be situated at various depths, according to the specific needs).
Coral nubbins are glued onto plastic pins (9 cm long, 0.3–0.6 cm width leg and 2 cm diameter ‘head’) which are inserted into plastic nets stretched over PVC frames (30 cm × 50 cm).
The frames carrying corals are tied to the nursery base (photograph by D.
Gada); (b) the novel prototype of the rope nursery in Bolinao, the Philippines [20].
This nursery accommodated small coral fragments attached to a rope, creating an easily constructed nursery bed that is rapid and inexpensive.
The coiling force of the ropes adequately held fragments without adhesives, and the minimal surface area of rope nursery beds provided not only improved water flux around farmed corals, but also reduced proliferation of fouling organisms.
Above two nursery prototypes have been used under various conditions and demands, making the construction of large scale nurseries a very feasible target (photograph by G.
Levi); (c) coral stocking in a vertical rope nursery (Eilat, Red Sea).
Corals are growing on the rope and are often clipped for developing daughter colonies that are farmed in other nursery types (insert photo — a Stylophora pistillata colony growing on the rope).
This nursery further attests to the wide range of nurseries recently developed, each adapted for a specific need (photograph by A.
(d,e) two transplantation methodologies developed recently (out of several) for transplantation of nursery farmed corals on hard and soft substrates.
In Eilat, Dekel Beach (d), the farmed coral colonies were secured to the hard substrates by the attaching devices (plastic pegs and masonry anchors), inserted into pre-drilled holes, secured with a minuscule amount of epoxy glue.
The holes were drilled using underwater driller, powered by pressured air from diving tanks (photograph by Y.
Horoszowski-Friedman).
In Thailand (e), corals were attached on wire metal mesh construction (insert figure) by plastic ties, which is cheap and fast for attaching.
Other studies (unpublished) used environmental friendly materials, like bamboo canes (photograph by G.
(f) A denuded reef patch in the northern Gulf of Eilat (Dekel Beach), five years after coral transplantation.
Many fish and reef-associated invertebrates were attracted and recruited to this restored small patch reef (photograph by Y.
Horoszowski-Friedman).
The transplantation phase has further benefitted from developing a wide array of new methodologies, like transplantation into drilled holes, transplantation on wire mesh, chiselling holes in softer substrate, lining of rope-nursery grown corals on soft and hard substrates, and more ([12••, 15•, 21, 22]; Figure 2).
By using these methods, not only is the coral community rehabilitated, but its entire carrying capacity also increases due to the new ecological and spatial niches added to the site.
However, transplantation methodologies are still challenged by scientific and technical defies.
The scientific part focuses on issues, such as genetics, species combinations, landscape manipulations, biological engineering and key species.
One point to consider and test is spacing of transplants.
Transplants require sufficient space for growth in order to avoid intraspecific or interspecific disturbances.
Allogeneic and xenogeneic interactions can cause damage and growth abatement, influence reproductive activities or cause death.
Clearly, studies on the second phase of the gardening tenet are still very limited and should be increased.
The ‘gardening concept’ as an adaptive tool to combat climate change impacts The literature attests that global climate changes occur and that they differentially alter regional ecosystems, causing unprecedented degradation to coral reefs [25].
Climate changes present new challenges to coral reef scientists and policy makers by creating novel coral assemblages, whose ecological properties, goods and services differ from those characterizing preceding reef ecosystems (Figure 1).
The exacerbated impacts on the reefs lead to the conclusion that current conservation methodologies are failing to support biodiversity and reef services; clearly insufficient for averting reef degradation [4].
These impacts of climate change necessitate the development of unorthodox approaches, led by the notion that ‘restoration efforts once focused on past conditions should become more forward-looking’ [26].
On the basis of this rationale, restoration activities should highlight climate change scenarios, focusing on adaptation strategies that had not been considered in past reef management settings.
This may raise suggestions for more radical approaches like ‘assisted colonization’ [reviewed in 10•] or for focusing only on sites that are, and predicted to remain, under conditions suitable for current coral assemblages.
Both approaches deviate conceptually from the ‘reef gardening’ notion.
The gardening concept is using proactive responses to global changes, incorporating major amendments in current restoration methodologies.
While past restoration studies have focused on establishing key group communities, the gardening concept supports use of coral species/genotypes that would be favorable in the anticipated climate change conditions, overlooking coral species/genotypes that are less tolerant to climatic conditions; therefore reassembling novel coral reef communities that are robust to global change conditions [27].
Other tools incorporate selected ecological engineering aspects [12••, 28], taking into account corals functioning as primary reef ecosystem engineers.
These tools rehabilitate coral reefs with larvae released from nursery-farmed corals, from transplanted coral colonies, considering various techniques for coral transplantation, coral coverage, assorted coral species compositions and engineered seascape [2, 3, 4, 11, 12••, 20, 21].
Whereas neoteric in the coral restoration discipline, the ecosystem engineering approach is deeply rooted in terrestrial restoration measures, revealing, for example, increased bird visitations in reforestation [29] or enriched forest species in grazer-enclosure regenerating forests [30].
Paramount to the success of the gardening concept is the proficiency to harness genetic backgrounds of farmed colonies as an applied tool for restoration that targets global change.
Minimal insight is available for the ways genotypic variation influence adaptive global changes competence [31••].
However, recent scientific interest in the relationships between genotypes and gene expression, as to the kaleidoscope of responses to various stress conditions, has revealed that genetic legacy may serve as a prime applied tool for combating global change impacts [32], further suggesting the accommodation of climate change contingencies in reef restoration practices.
Because of stochastic reproduction and dispersal processes, genetic repertoires presented by marine organisms at any specific time/location may not reach equilibrium with today's climate, providing the opportunity to search for genotypes that are not perfectly adapted to current conditions but better suited for future environmental settings and farm them within underwater coral nurseries.
This is further important as accelerating global change rates, which are notoriously exceeding the evolutionary capacity of corals to acclimatize [33], are primarily relevant to long-lived coral species.
Coral bleaching, for example, is conspicuously patchy between different genotypes, representing a signature of true genetic heterogeneity and revealing an acclimatization response rooted in epigenetics.
Therefore, genetic variation should be a potential reservoir of resilience to climate change, a characteristic that can be actively amplified when developing coral farming/breeding protocols under in situ nursery conditions.
Underwater coral nurseries may also serve as genetic repositories for coral reef restoration, combating the impacts of major natural catastrophes [22, 34•].
The use of the ‘reef gardening’ rationale as global change mediator through nurseries [20, 21, 22, 24•, 34•] has already revealed two novel strategic roles of this instrument, (a) reducing coral mortality during events, such as massive coral bleaching, hurricanes and fresh water floods, the creation of climatic refugia and (b) preserving and propagating diverse coral genotypes from various source materials for the establishment of regional/local ‘gene stocks’ for use in restoration activities, with an eye to initiation of breeding programs.
The ‘reef gardening’ rationale has further disclosed strategic considerations of this instrument ([12••, 15•, 22], unpublished), including re-shaping of coral reefs types, changing of reef rugosity, engineering of coral seeding processes, reducing of fleshy algae allotment in restored reefs and sustaining of ecosystem processes.
Would the coral ‘gardening tenet’ lead to sustainable reefs?
Theoretical and empirical aspects of active reef restoration are still in their nascent stages, awaiting further work.
Active reef restoration holds a number of challenging issues and uncertainties, such as the issues of predicting the scale of transplantation impacts, the responses of transplanted colonies in their new ‘homes’ and the suitability of these acts to combat reef degradation.
The progression of the ‘gardening notion’ has surmounted four major obstructions, all are satisfactorily deciphered: (a) developing the needed credentials for farming a wide variety of coral species in mid-water nursery (Table 1); (b) the ability to develop stocks of coral colonies, employing the ‘nubbins’ methodology [16, 19]; (c) documentation that nursery farmed coral colonies perform well in their ‘new homes’, following transplantation ([12••, 15•, 22], unpublished); and (d) verification of the low cost gardening approach (down to 0.17 and 0.19 US$/coral colony for farming and transplantation, phases, respectively [15•, 20].
Now, the ‘gardening notion’ is facing its fifth challenge, performing a large, ecologically profound restoration act (hundreds of thousands of coral colonies/site) to reveal the ecological engineering capacities of large-scale transplantation acts.
This challenge is the most imperative because it would demonstrate that the gardening approach is supporting the initiation of sustainable coral reefs.
The gardening toolbox may further be used for testing novel approaches, such as developing of improved corals through epigenetics.
Studies (e.g., [35]) have revealed that under a wide range of ecological insult scenarios, organisms modify levels of genome epigenetics that may coincide with increased tolerance to otherwise lethal conditions, further showing that these epigenetic changes may be stable across multiple generations.
Therefore, genome-wide transcriptional plasticity may underlie whole organism adaptation to novel environmental insults, like those presented by global change [36•] and can be used as an applied tool in coral nurseries.
Abstract Indonesia’s coral reefs have been severely damaged by global and local stressors, and a range of active restoration techniques are now being used in attempts to rebuild degraded reefs.
However, it is difficult to summarise Indonesia’s restoration efforts as a whole due to a lack of consistent reporting.
Here, we first discuss Indonesia's legal policy framework concerning reef restoration; this is included in the agenda of two government ministries (Marine Affairs and Fisheries, and Environment and Forestry), and comprises national laws and governmental, presidential and ministerial regulations.
We then provide an extensive review of reef restoration projects in Indonesia, documenting 533 records across the country between 1990 and 2020.
Most (73%) of these records come from the past ten years, and many (42%) are reported in online news articles rather than scientific reports or papers.
This review identified 120,483 units of artificial reef installed across Indonesia, along with 53,640 units of coral transplantation (including both coral nurseries and direct out-planting onto reefs); in total, 965,992 fragments of hard coral have been planted across Indonesia.
The most favoured restoration materials are concrete (46%) and steel structures (24%).
Projects are organised by a diverse range of governmental, NGO, private and community-led organisations.
This review demonstrates that Indonesia’s policy has encouraged a diverse range of practitioners to implement reef restoration, but projects are often not coordinated with wider networks of restoration practitioners or scientists, and only 16% of the identified projects included a post-installation monitoring framework.
Incorporating clear objectives and long-term monitoring programmes in project planning stages, while prioritising knowledge exchange and engagement with international scientific community, will substantially improve restoration outcomes in Indonesia.
This will allow the country to fulfil its considerable potential as a global leader in rebuilding damaged coral reefs.
Previous article in issue Next article in issue Keywords IndonesiaCoral reefRestorationRehabilitationRegulations 1.
Introduction Indonesia’s 39,538 square kilometres of coral reefs account for 16% of the global total reef area and are recognised as being amongst the most diverse ecosystems in the world [1].
Unfortunately, Indonesia’s reefs have also been severely damaged by anthropogenic causes, including local stressors such as pollution, eutrophication, overfishing and destructive fishing practices, as well as mass bleaching linked to climate change [2], [3].
Nearly a quarter of Indonesia’s 270 million population live on the coast within 30 km of a coral reef, which is the largest reef-associated human population of any country in the world.
Due to this high concentration of people near the coasts, over 95% of Indonesian reefs are considered under threat, mainly due to overfishing and destructive fishing [1].
Despite dynamite fishing being illegal since 1985 [4], this practice remains a major and widespread threat to Indonesia’s reefs.
In many of Indonesia’s damaged reef areas, natural ecosystem recovery is precluded by the creation of unconsolidated rubble fields [5].
Rubble fields are hostile environments for coral recovery, because the highly unstable substrate causes young coral colonies to be easily overturned, abraded, or buried [6], [7].
As such, even if rubble field sites have a good supply of coral larvae and favourable water quality, they often show no signs of natural recovery.
Whilst rubble fields are created by a range of degradation processes around the world, this problem is particularly acute in Indonesia due to the prevalence of blast fishing (sometimes referred to as bomb or dynamite fishing).
Many rubble fields that were created by historic blast fishing have not recovered even decades later [8].
A range of active reef restoration techniques are increasingly being implemented around the world, in attempts to rebuild reefs where natural recovery processes are slow or non-existent [9], [10].
Ideally, these efforts are implemented alongside efforts to mitigate local threats to reefs, and targeted at bypassing barriers to natural recovery (such as rubble or reduced recruitment), until the system reaches a point where the coral reef can recover naturally.
In Indonesia, the installation of artificial structures and coral transplantation have become popular restoration techniques and have been carried out for over four decades.
The first documented installation of artificial reefs was by the Indonesian Navy in July 1979, aiming to rehabilitate the coral reef around Seribu Islands, north of Jakarta, by submerging old cars, rickshaws and tires.
It was hoped that this would provide topographic complexity, stable substrate for coral and other invertebrate settlement, and habitat to attract fish [11].
In recent decades, a wide range of restoration projects using a diverse suite of methods have been established in Indonesia’s coastal waters.
The methods and materials used for restoration projects vary significantly, including deployments of repurposed waste material, piles of volcanic rocks, custom-designed concrete structures, branching ceramic modules, electrolytic deposits on shaped wire mesh templates, hexagonal steel structures, and direct fixing of coral fragments onto the seabed.
Projects have been initiated by a range of government initiatives, local and international NGOs, private sector companies and coastal communities.
However, many of these projects have not been officially reported, and reviews of reef restoration projects across Indonesia are outdated and not published in the peer reviewed literature [8].
Further, the deployment of artificial reefs or other restoration methods falls under multiple government policy frameworks, and it is difficult to assess permit requirements and regulations pertaining to reef restoration activities.
In this paper, we present a summary of the policy framework supporting reef restoration in Indonesia, and a comprehensive review of restoration projects across the country from 1990 to 2020.
First, in order to understand the legislative and legal structure that governs and supports restoration in Indonesia, we describe statutes and guidelines taken from government, presidential and ministerial regulations and decrees.
Second, we review Indonesian restoration projects described in both the academic and grey literature, including both traditional and social media, written in both English and Bahasa Indonesia.
To our knowledge, this study represents the first publicly available database of reef restoration projects in Indonesia.
The database and its accompanying interactive visualisation is available at bit.ly/Indonesian_restoration.
Materials and methods 2.1. Legal and policy documents An extensive review of national and ministerial policy documents was carried out to identify those that pertain to coral reef or coastal ecosystem restoration or rehabilitation.
The review analysed the content of each regulation to summarise its core aspects, incentivisation for coral reef restoration and guidelines for best practice.
Most policy documents were available online in Bahasa Indonesia.
Online platforms such as peraturan.go.id (an online platform to disseminate all the laws and regulations managed by the Directorate General of Legislation of the Indonesian Ministry of Law and Human Rights) and jdih.kkp.go.id (a legal documentation and information network of the Indonesian Ministry of Marine Affairs and Fisheries (MMAF)) were used to access policy documents.
A two-category string approach was used to search for policy documents, by combining pairs of words from each of two categories: one that described a legal framework; and one that described an aspect of coral reef restoration (Table 1).
The two-category string approach used to search for policy documents.
Multiple non-systematic searches were carried out, with each one combining at least one term describing a legal framework (left-hand column) and one term describing an aspect of coral reef restoration (right-hand column).
Legal framework search term	Coral reef restoration search term Undang-undang (Law)	Terumbu karang (coral reef) Peraturan Pemerintah (Government Regulation)	Pesisir (coastal) Peraturan Presiden (Presidential Regulation)	Pulau-pulau kecil (small islands) Peraturan Menteri (Ministerial Regulation)	Rehabilitasi (rehabilitation) Keputusan Menteri (Ministerial Decree)	Restorasi (restoration) Empty Cell	Pemulihan (recovery) Empty Cell	Transplantasi (transplantation) 2.2. Review of reef restoration records An extensive review was carried out of the academic and ‘grey’ literature describing coral reef restoration projects in Indonesia over the past three decades (1990–2020).
This multiple-source approach was critical to gain an accurate understanding of the true extent of reef restoration activities in Indonesia, given that the majority of projects have been reported outside of the scientific literature.
Searches were carried out in both Bahasa Indonesia and English, using combinations of the keywords ‘karang’ (coral), ‘terumbu karang’ (coral reef), ‘terumbu karang buatan’ (artificial coral reef), ‘terumbu buatan’ (artificial reef), ‘transplantasi’ (transplantation), ‘rehabilitasi’ (rehabilitation), ‘restorasi’ (restoration), ‘pemulihan’ (recovery) and ‘laju pertumbuhan karang’ (coral growth rate).
Records from these searches were compared with English-language records of Indonesian reef restoration summarised in a recent global review of coral reef restoration [9].
Following this comparison, all records from both reviews were combined into the database associated with this study.
When entering the data, it was necessary to distinguish between projects and records, as some projects from a single source reported multiple locations and/or methods and were split over multiple rows in the database.
Therefore, there are a greater number of records than projects in the database.
Further, not all entries are complete, as sources did not always report information about every aspect recorded in the database.
Percentages belonging to a specific group or category (i.e. restoration method, materials used etc.) were therefore calculated as  , where y = the total number of records in the category, and x = total numbers of records that contained information about that category.
Thus the denominator can be < the total number of individual projects in the database when information is missing from that source, but also > the total number of individual projects in the database when a project contains multiple records.
2.3. Terminology Readers should note that the terminology describing restoration methods in Indonesia, and therefore in this study, differs slightly from that generally adopted to describe coral reef restoration methods elsewhere (i.e. compared to [9], [12]).
The term ‘transplantation’ is used here to describe any method that involves coral fragments, whether these are directly transplanted onto a substrate (elsewhere: ‘direct transplantation’), or via an intermediate coral nursery (elsewhere: ‘coral gardening’, or ‘asexual propagation’).
The term ‘transplantation rack’ refers here to a specific type of coral nursery that is used commonly in Indonesia (elsewhere: ‘table nursery’).
Finally, reef restoration is generally referred to as ‘reef rehabilitation’ in the majority of Indonesian legal documents and references; this term was included alongside restoration for all aspects of this review.
Results and discussion 3.1. Indonesian laws and regulations on coral reef restoration Seventeen policies and regulations were identified that pertain to coral reef restoration in Indonesia (Table 2).
These regulations comprise four national laws, three government regulations, two presidential regulations and eight ministerial regulations.
Specific topics mentioned by laws and regulations that govern coral reef restoration in Indonesia.
This table includes laws (items 1–4), government regulations (items 5–7), presidential regulations (items 8–9) and ministerial regulations from the Ministries of Environment (MoE), Forestry (MoF), and Marine Affairs and Fisheries (MMAF) (items 10–17).
Ticks indicate that laws mention the topic denoted by each column.
Shaded items (8, 11, 12, 15 and 17) are those that contain the most comprehensive rules and guidelines for coral reef restoration in Indonesia.
* * denotes the guideline that describes transplantation (i.e. cutting a piece of live coral for planting/attaching it to an artificial substrate or natural coral rock; Article 26 verse 1d), where it is described as a method for breeding protected and non-protected fish species.
Image 1 All of Indonesia’s regulations concerning coral reef restoration encourage wide community participation, with ownership and responsibility shared between government (both central and local) and local communities who live near and benefit from reefs.
For example, Law No. 27/2007 (amended by Law No. 1/2014) stipulates that restoration practices can be conducted by ‘Government and/or Regional Government and/or each person which directly or not directly obtains the benefit from coastal areas and small islands’ [Article 33.1].
This sentiment of community-driven management of restoration is echoed in Presidential Regulation No. 121/2012 (‘Rehabilitation can be conducted through cooperation between government, regional government, person or community’ [Article 12.1] and ‘Community or persons can participate in the implementation and maintenance of rehabilitation voluntarily’ [Article 15.1]), and also in the recent MMAF Ministerial Regulation No. 26/2021 (‘Each person can participate in the rehabilitation of fisheries resources and their environment’ [Article 67.1]).
Indonesia’s system for gaining official permission to conduct reef restoration is also reflective of this community-driven approach.
While many other countries with a large restoration footprint (like Australia and the USA) rely on centrally-governed permits that are administered at a national level (e.g. Australia: https://www.gbrmpa.gov.au/access-and-use/permits), Indonesia’s regulations are governed regionally.
For example, Presidential Regulation No. 121/2012 states that proposals for restoration must be ‘consulted with the Regional Working Unit in charge of the marine and fisheries affairs at the rehabilitation location’ [Article 9.2], rather than going through a nationally centralised governing unit.
MMAF Ministerial Regulation No. 26/2021 also reflects this regional governance structure, dictating that plans for restoration ‘must be delivered and consulted with Government, Governor or Regent/Major at the rehabilitation location’ [Article 48.4].
The requirement to obtain permits for marine activities is not new in Indonesia - Law No. 32/2014 states that ‘Each person undertaking marine spatial use permanently in the waters and jurisdiction areas are obliged to own a location permit.’ [Article 47.1].
However, the most recent ministerial regulations released in 2021 have emphasised the need for permits - MMAF Ministerial Regulation No. 28/2021 repeats this sentiment that ‘Each person conducting marine spatial use activity on the coastal waters, waters area, and/or jurisdiction area permanently on some parts of marine space is obliged to have KKPRL [permit].’ [Article 113.1].
This renewed emphasis on permit requirements may be in response to a rapidly growing number of new restoration projects around the country in recent years (see 3.2 Summary of reef restoration projects in Indonesian waters (1990–2020), 3.3 Temporal trends in reef restoration practice within Indonesia).
In addition to having a regionally structured permitting system, Indonesia’s legislation specifically requires that local communities and stakeholders should be directly involved in both the planning and implementation of restoration activities.
MMAF Ministerial Regulation No. 26/2021 states that restoration plans ‘must be consulted with related stakeholders around the rehabilitation location in order to receive inputs and responses’ [Article 48.3], in a system that echoes the broader rules laid out by the Ministry of Forestry (MoF) for all categories of ecosystem restoration (‘Implementation of ecosystem recovery is conducted by the management unit and/or can be conducted by permit holder after obtaining a permit from the Minister by involving the local community.’, MoF Ministerial Regulation No. 48/2014, Article 15.1).
As such, Indonesia’s legislation around restoration decentralises the governing responsibility to regional authorities rather than a national centre, and encourages the participation of a diverse range of local communities and stakeholders.
Indonesia’s regulatory structure also creates space for a diverse range of methods and approaches to reef restoration.
It is specified at a broad level that all projects should aim to protect and enrich natural ecosystems and resources.
For example, Law No. 27/2007 (amended by Law No. 1/2014) states that restoration should be carried out in ways that ‘pay attention to the balance of the ecosystem and/or local biodiversity’ [Article 32.1] and are ‘environmentally sound’ [Article 32.2d].
However, within this framework, the regulations do not specifically regulate restoration methods or specify measurable target outcomes.
A recent MMAF Ministerial Decree (General Director of Marine Spatial Management Decree No. 10/2021) provides guidelines for a range of restoration activities, but there are no permits or legal approval that are conditional on these guidelines.
As such, Indonesia’s regulatory framework is likely to lead to a high degree and diversity of participation in restoration, but a lack of a synchronized approach or common methods.
Further, an emphasis on deployment without a requirement for clearly specified objectives and measurable targets increases the risk of ill-advised restoration projects that are likely to fail to deliver genuine conservation benefits.
3.2. Summary of reef restoration projects in Indonesian waters (1990–2020) We documented 533 restoration projects spanning 29 of Indonesia’s 34 provinces (Fig.
These projects were recorded as 600 separate records in the database (Table S1, Supplementary Material).
The primary source of records was online news sites (222, 42%), followed by official organisation websites (106, 20%), peer reviewed literature i.e. local and international journals (71, 13%) and reports (54, 10%, Fig.
This wide range of sources illustrates the complexity of summarising restoration activities across the country, and is driven in large part by the diversity of participation in restoration.
1 Download: Download high-res image (178KB) Download: Download full-size image Fig.
Indonesia’s coral reef restoration projects (1990–2020), aggregated by province.
Circles are positioned at the geometric centre of each province; their size is proportional to the number of restoration projects in that province.
There are a total of 533 projects in the database.
To explore this database further, see the interactive visualisation here.
2 Download: Download high-res image (140KB) Download: Download full-size image Fig.
The a) information source and b) main organiser of each of the 533 Indonesian coral reef restoration projects in the database.
A range of public and private organisations have established Indonesia’s reef restoration projects (Fig.
One third of records in the database were organised by the Indonesian government (205, 38%), with the next most common organisers being in the private sector (79, 15%), university (75, 14%) and NGOs (68, 13%).
This diversity in practitioners mirrors the policy landscape in Indonesia; national laws and regulations promote inclusivity and heterogeneity in participation (Section 3.1; Table 2), and so it is unsurprising that a wide range of practitioners are actively involved in establishing a high number of restoration programmes.
Intersectional collaboration is also a common feature of Indonesia’s restoration landscape; many of the projects were led by one organisation, but included involvement of partner organisations in different sectors.
Collaborative approaches of this nature have the potential to overcome the limitations of any single organisational structure and lead to better restoration practice [13].
3.3. Temporal trends in reef restoration practice within Indonesia The number of coral reef restoration projects in Indonesia has increased dramatically in recent years (Fig.
Over two thirds of restoration projects in this database were established in the past ten years (388 projects established since 2010, 73%), with over half established in the past five years (294 records since 2015).
Strikingly, this recent increase has continued even despite the COVID-19 global pandemic, with the year 2020 featuring more new records of restoration projects than any previous year (Fig.
These new projects in 2020 were largely attributed to the ‘Indonesia Coral Reef Garden’ programme, organised by the Coordinating Ministry for Maritime and Investment Affairs as part of an economic recovery strategy for coastal communities impacted by unemployment due to COVID-19 (https://maritim.go.id/mewujudkan-indonesia-coral-reef-garden/).
In total, this programme is estimated to have employed 10,000 people in planting nearly 96,000 units of artificial reefs and transplantation racks/coral nurseries covering 74.3 Ha in five areas in Bali between October 2020 and January 2021 [14].
This large programme is one example of a general trend demonstrating that the operational scale of restoration activities across Indonesia has increased dramatically in recent years.
Before 2010, only two projects had outplanted more than 10,000 coral fragments; by contrast, in the subsequent decade (2010–2020) this milestone was achieved by nine further projects (Fig.
While these numbers are impressive, it is important to remember that a high number of outplanted fragments does not necessarily indicate a successful project.
Rather, the ultimate goal of restoration projects should be the long-term survival and proliferation of outplanted corals into a self-sustaining functioning ecosystem (see Section 3.4 for more details on monitoring).
3 Download: Download high-res image (317KB) Download: Download full-size image Fig.
Temporal trends in Indonesia’s coral reef restoration projects.
Shown are trends through time in the establishment of restoration projects, split by: a) method of restoration; b) materials used; and c) number of coral fragments installed.
To explore the database further, see the interactive visualisation here.
There are a diverse range of methods and materials used in Indonesian reef restoration projects (Fig.
3), which have also changed markedly through time.
Across all time periods, the most favoured materials used to make restoration structures are concrete (173, 46%), and steel (91, 24%) (Fig.
However, the diversity of materials used has increased in recent years; projects established in the 1990 s predominantly used concrete and tyres, compared to a far more diverse array of approaches used in recent years, that includes ceramic structures, steel frames, direct transplantation and biorock.
Whilst concrete has remained the dominant material throughout all three of the decades studied, other materials have seen changes in their popularity.
For example, the use of tyres was popular throughout the 1990 s, representing 50% of projects in that decade, including some years (1996–1997) where it was the only material used.
However, the use of tyres has gradually declined such that no such projects have been recorded since 2009.
The use of steel structures has dramatically increased in recent years, from four records in the 2000 s to 86 in the last decade.
Many of these structures use a hexagonal shape, mimicking the success of the ‘Mars Assisted Reef Restoration System (MARRS)’ in southern Sulawesi [15].
These structures were first used by Mars in 2013 and they now represent 18% of project records over the last three years (33 projects between 2018 and 2020).
As such, there are several lines of evidence that different methods and materials for restoration are spread throughout the country, with certain techniques becoming more and less popular over time.
These changing trends may be a result of different projects inspiring and imitating each other, or may be due to fluctuations in the availability and affordability of certain materials above others.
3.4. Post-installation monitoring Amongst reef restoration efforts worldwide, there remains a need to align and standardise metrics for ecological monitoring [16].
This is particularly important for evaluating the success of different approaches to restoration and to guide management decisions in different contexts.
The diversity of restoration approaches in Indonesia means that ecological monitoring is of particular importance in this region; however, only 16% (85) of the reef restoration 533 projects incorporated a post-installation monitoring programme.
These 85 projects were recorded as 101 separate records in the database (Table S2, Supplementary Material).
All of the projects that mentioned ecological monitoring were published in the academic literature (i.e. journals, theses, proceedings and reports) or official project websites, with no online news reports (the dominant source of reef restoration records) mentioning ecological monitoring.
There may be a reporting bias present in these calculations (i.e. news reports may be more likely to report on project establishment rather than project monitoring).
However, it remains clear that ecological monitoring is far from ubiquitous in Indonesian reef restoration practice.
While 85 records indicated that they had conducted monitoring, the vast majority lacked sufficient detail to reliably extract information about focal taxa and/or to discuss outcomes of the restoration.
As such, in this review we detail only the proportion of projects that conducted certain types of monitoring, rather than the results of that monitoring.
Those projects that did include ecological monitoring featured monitoring schedules that varied in duration from one month to 16 years after the installation of artificial reefs/coral nursery.
Most of these monitoring studies reported only a single visit to the restoration sites (47 of 85 projects, 55%), while remaining projects visited sites between 2 and 16 times over the study period.
A majority of monitoring studies (80, 94%) had monitored some aspect of the coral community, with the primary focus being on the survival and/or skeletal extension rate of the coral transplants.
A number of studies (39, 46%) reported monitoring the fish community on restoration sites, most often expressed as raw abundances or as density measures; while 26% (22) monitored both reef benthic and fish populations.
Only one study examined in detail the physical condition of the artificial reefs [17], reporting that between one and five years post-installation the concrete structures in several restoration sites have been completely buried by rubble or destroyed due to poor setting or placement during the installation process.
This diversity of restoration approaches, combined with a lack of ecological monitoring, combines to limit the potential for evaluating success in Indonesia’s reef restoration efforts.
Whilst many different methods and materials are used, very few approaches seem to have implemented monitoring programmes to understand how coral, fish and invertebrate populations are responding to restoration interventions.
Some projects do offer encouraging examples of successful monitoring; for example, there are well-documented increases in coral cover on rock piles in Komodo National Park [8] and on Reef Stars in South Sulawesi [15] - but these projects are the exception rather than the norm (Fig.
For future reef restoration initiatives to learn more effectively from each other and share knowledge of best practice, a common approach to monitoring and data sharing is required.
To achieve this, reef restoration budgets need to include costs for ecosystem monitoring and data sharing protocols as essential items to evaluate project outcomes.
These budgets must also be structured to provide for future monitoring events, in order to allow long-term evaluation of restoration success for the years following restoration interventions.
This would facilitate understanding of which restoration practices were most effective for meeting different targets in different socioeconomic and ecological contexts - in turn allowing the formulation of more efficient restoration strategies across the country.
4 Download: Download high-res image (1006KB) Download: Download full-size image Fig.
Examples of coral reef restoration techniques used in Indonesia.
Shown are A) Rock piles at Komodo National Park, East Nusa Tenggara [8], B) Mars Reef Stars at South Sulawesi [15], C) EcoReefs at Bunaken National Park, North Sulawesi [20] and D) Reef Balls at Sumbawa, West Nusa Tenggara [21].
Each technique is shown at the point of installation and after several years of successful coral growth.
Note that these pictures represent ‘best-case’ outcomes, and the authors do not suggest that all projects using specific techniques have had the same success.
Photo credits: Helen E.
Fox (A), The Ocean Agency (B), Mark V.
Erdmann and Tries B.
Razak (C) and PT.
Amman Mineral Nusa Tenggara (D).
There are several examples of monitoring schemes and tools which might help to achieve more holistic monitoring of reef restoration programmes in Indonesia.
For example, the Global Coral Reef Monitoring Network (GCRMN) guides and mobilises monitoring of reef health and bleaching status around the region [18]; this model might be adapted to evaluate the health of reef restoration projects around Indonesia.
Additionally, several organisations have published guidelines for designing and implementing monitoring protocols for restoration programmes; for example, the NOAA manager’s guide for reef restoration includes guidelines and ideas for monitoring strategies specific to restoration projects [19].
The high number and diversity of Indonesia’s restoration projects demonstrate that there is great capacity to carry out restoration work; now developing a similar capacity for monitoring will allow these interventions to be more evidence-led and effective.
3.5. International communication The vast majority of records in this database were written in Bahasa Indonesia (450 of 533, 84%) and/or published in online Indonesian media outlets (222, 42%).
These communication methods are excellent for reaching audiences within Indonesia - and much of the within-country knowledge exchange that has occurred over the past three decades is likely to have been influenced by these media reports.
However, these sources of information are largely inaccessible to people and organisations outside of Indonesia’s borders, reducing the potential for knowledge exchange with other countries.
A recently compiled global database of restoration projects around the world [9] (www.icriforum.org/restoration/coral-restoration-database) captured only 5% of this study’s Indonesian records (27 of 533), probably because it focused only on English-language sources.
This highlights the extent to which lessons learned in Indonesian restoration projects are currently difficult to translate around the rest of the world.
Indonesia is widely recognised as being the global epicentre of coral reef diversity [1], and the 533 restoration projects documented in this paper now also suggest that the country has the necessary experience to be a world leader in restoration capacity.
If Indonesia’s abundance of experience in a diverse array of restoration projects could be more effectively shared around the world, this might foster wider collaboration and capacity building, ultimately advancing global understanding and competence in reef restoration practice.
Recent initiatives within Indonesia have started to make encouraging progress in expanding knowledge exchange with international partners.
For example, the Coral Triangle Center (CTC) have a training centre in Bali from which they can deliver training and capacity building for partners around South-East Asia (www.coraltrianglecenter.org), Department of Marine Science and Technology at IPB University have recently launched the School of Coral Reef Restoration (SCORES) a working group and knowledge-sharing platform for reef restoration practitioners in Indonesia and around the world (https://fpik.ipb.ac.id/), and Mars Sustainable Solutions provides restoration training to practitioners around the world based on successful methods developed within Indonesia (www.buildingcoral.com).
Further progress on international collaborations such as these will ensure that the wealth of knowledge and experience accrued within Indonesia can be valuably disseminated amongst restoration practitioners around the world.
3.6. Future directions Over the past three decades, Indonesia has accumulated a wealth of practical knowledge regarding reef restoration.
The sheer number of projects and outplanted coral fragments outnumber any other country covered in the global restoration review [9].
The extent and diversity of these projects clearly demonstrate Indonesia’s potential as a global leader in coral reef restoration.
However, Indonesian reef restoration shares many of the same growing pains that have been experienced by coral reef restoration globally, and coastal restoration in general [22].
A large proportion of projects are categorised as artificial reefs (397, 66%), but do not report that any coral fragments have been transplanted onto the reef, or that the reef is being maintained in any way.
In the best-case scenario, these artificial reefs can act as fish-attracting devices by increasing structural complexity in the short-term [23], and act as settlement substrates for recruiting corals in the long-term [24].
However, when placed in sub-optimal locations (i.e. where no coral reef previously existed, or natural recruitment is low) these sites run the risk of being nothing more than underwater refuse heaps.
Consistent monitoring and appraisal must be carried out to ensure that artificial reefs constructed in the name of coral restoration are functioning effectively, rather than as underwater structures that play no active role in regenerating coral populations.
Further, there appears to be an over-representation of records in the dataset that are categorised as coral nurseries (19% overall), while studies describing outplanting are much more scarce (5%) suggesting that these nursery racks are not an intermediate step towards outplanting corals, but rather a permanent structure.
If Indonesia is to move towards a coral restoration programme that achieves measurable, ecologically meaningful outcomes on coral reefs at a nation-wide scale, it is imperative that objectives focus on holistic reef recovery rather than just numbers of corals grown in temporary or artificial nurseries.
Ecological metrics must be incorporated into each step of the lifecycle of restoration projects.
Several recent publications can serve as guides to help achieve these goals: for example, by outlining high-level steps to improve coral restoration in general [16]; guide managers through the steps of planning restoration projects [19]; providing suggestions for monitoring [25]; and highlighting the importance of including social metrics in the planning and evaluation of restoration success [13], [26].
The barriers to knowledge sharing and the lack of appropriate objectives and monitoring described in this review have the potential to prevent Indonesia from meeting its potential as a global leader in coral reef restoration.
To address these issues, future projects should include: 1) explicit objectives, 2) long-term monitoring of ecological outcomes, and 3) improved knowledge exchange with the international scientific and restoration community.
Conclusions Indonesia’s coral reefs are amongst the most species-rich in the world, but also face exceedingly high levels of local anthropogenic pressure.
When combined with threat mitigation (e.g. improved water quality, cessation of blast fishing, climate change mitigation), reef restoration is likely to play a valuable role in the management of these exceptionally diverse and threatened ecosystems.
Indonesia’s policy framework encourages an unusually high diversity of participation in restoration activities, with low levels of centralised regulation compared to other countries.
This has led to diverse involvement in a high number of restoration projects across the country, organised by a multi-sector group of practitioners using a wide range of methods and materials.
However, significant challenges remain for Indonesia to meet its potential as a world leader in coral restoration.
With greater efficacy in meeting target-driven outcomes, consistency in ecological monitoring, and intentionality in global knowledge exchange, Indonesia’s restoration projects could become a transformative resource for the region and an example for the world to follow.
Abstract The concept of urban forestry is addressed from a discursive perspective, with focus on identifying and describing various scientific discourses, their strength and development over time and on different continents.
This work can help obtain a deeper understanding of the scientific discourses in terms of identifying research trends and reasons behind these trends, as a possible way forward for research.
Scientific publications (N = 519) issued during the period 1988–2014 (and as listed in the SCOPUS database) were analysed with the aims to 1) systematically identify and describe scientific urban forestry discourses, 2) discuss implications of these findings for scientific practice, and 3) propose ways forward.
Six discourses of various strength and geographical distribution were identified.
Scientific production was found to be dominated by North American and European authors with modest contributions from authors from other continents.
Scientific discourses proved mostly expert driven and reflecting the positivist scientific paradigm.
Prevailingly managerial orientation and absence of qualitative approaches indicate a lack of deeper understanding of human-environment relations.
Studies related to active participation of citizens and partnerships in urban forestry have been missing.
More emphasis should be placed on the testing of existing, and developing new methods and modalities of public participation, and on the value of civic involvement for the decision making.
Moreover, a more solid evidence base is needed for benefits from urban forests, while economic aspects of biodiversity and other ecosystem services are still insufficiently explored.
Study findings also call for more research on urban forest governance and relation between urban forest benefits and existing policies (e.g. climate change adaptation, energy policy or health).
Previous article in issue Next article in issue Keywords Discourse analysisResearch reviewSCOPUSUrban forest researchUrban green space Introduction Broad consensus exists on the multiple benefits urban forests provide accompanied with growing body of scientific evidence (e.g., Roy et al., 2012).
Yet no consensus exists on the precise meaning of the terms ‘urban forests’ and ‘urban forestry’ (UF) (Randrup et al., 2005).
The most quoted definitions of UF reflects high expectations for the field, encompassing an inclusive perspective of the urban forest as representing various types of green space, long term planning, provision of multiple benefits, dialogue between various disciplines and creation of partnerships among stakeholders (Randrup et al., 2005).
However, the existence of various meanings and practices of UF implies existence of various discourses in the field of UF.
The last two decades have shown increasing interest in the role of discourses and many studies show influence of discourses on environmental and forest-related policy making and politics (Hajer and Versteeg, 2005, Arts and Buizer, 2009, Arts et al., 2010, Lawrence et al., 2013).
A recent review of forest-related discourse studies showed that political science approaches to discourse analysis (DA) were the most popular (Leipold, 2014).
Nevertheless, DA of the UF concept has not been systematically done so far.
There are many conceptions of what discourse is, and there are many approaches to DA (Arts and Buizer, 2009).
Discourse is embedded in language and refers to meaning shared with others (Hajer and Versteeg, 2005, Dryzek, 2005).
Discourse is described as: “An ensemble of ideas, concepts, and categorisations that are produced, reproduced, and transformed in a particular set of practices and through which meaning is given to physical and social realities.” (Hajer, 1995, p.
This definition also reveals some of the discourse building blocks – ideas, concepts and categorisations that are subject to DA together with storylines, assumptions, symbols or metaphors.
Discourses are dynamic.
They interact, overlap, compete with each other and change over time, are not necessarily homogeneous, but show great durability (Arts et al., 2010).
DA is useful for identifying how a certain problem is structured, what solutions are offered and by whom, and in what historical, cultural or political context (Hajer and Versteeg, 2005).
Starting with the assumption that various discourses on UF exist, and focusing on discourses as featuring in the scientific literature, the aims of the paper are to 1) systematically identify and describe scientific UF discourses, 2) discuss implications of these findings for scientific practice, and 3) propose ways forward for research.
Scientific discourses were taken into account due to availability of scientific publications in databases in comparison to looking into urban forestry practices at large that are locally specific and not collected in databases.
Methods Description of the sample Scientific papers were retrieved on 28 June 2012 and again on 12 December 2014 (in order to update the search with recent studies) through the SCOPUS database by using the key word “urban forest*” in the title, abstract or key words in a predefined set of journals deemed the most relevant for UF, namely Arboriculture and Urban Forestry (until 2006 the Journal of Arboriculture - JoA/AUF), Urban Forestry & Urban Greening (UFUG), Landscape and Urban Planning (LANDUP) and Forest Policy and Economics (FPE).
JoA/AUF and UFUG specifically include topics related to “trees in the urban environment” and “urban and peri-urban woody and non-woody vegetation” respectively, in their aims and scope.
The rationale behind pre-selecting FPE and LANDUP was that the authors were aware that several influential articles on urban forestry had been published here, with the former linking urban forestry primarily to forest policy and economics, while the latter provides a context of landscape, urban ecology and urban planning.
The SCOPUS search yielded 519 hits for the period 1988–2014 and annual distribution shows constant gradual increase in number of publications over time (Fig.
Download: Download full-size image Fig.
Distribution of papers based on the SCOPUS search by the key word “urban forest*” in the period 1988–2014.
The timeframe of the search was not predefined.
It should be noted that some years of JoA are not covered in SCOPUS; for these years papers were searched for by using the same key words and downloaded directly from the journal's webpage.
SCOPUS was selected instead of e.g., Web of Science (WoS) since specific, highly relevant journals to the field of urban forestry (JoA/AUF and until 2009 also Urban Forestry & Urban Greening) were not listed in WoS.
The other included journals appear in both SCOPUS and WoS.
The authors are aware that not all papers on urban forests/forestry were included in this study, but consider that included papers represent a sample of the whole population of scientific articles related to this topic.
Almost half of the papers were published in the JoA/AUF (Fig.
This is not surprising taking into consideration the North-American origins of the urban forestry concept and the fact that FPE and UFUG were established only in 2000 respectively 2002; which coincides with the increase in overall number of papers (Fig.
Download: Download full-size image Fig.
Distribution of papers per journal in the period 1988–2014 (N = 519) (FPE = Forest Policy and Economics, JoA/AUF = Journal of Arboriculture/Arboriculture and Urban Forestry, LANDUP = Landscape and Urban Planning, UFUG = Urban Forestry & Urban Greening).
Download: Download full-size image Fig.
Distribution of papers per journal and year in the period 1988–2014 (N = 519) (FPE = Forest Policy and Economics, JoA/AUF = Journal of Arboriculture/Arboriculture and Urban Forestry, LANDUP = Landscape and Urban Planning, UFUG = Urban Forestry & Urban Greening).
The majority of the papers were written by North-American authors (almost all USA based), when affiliation of the first author was taken into account, followed by European authors, especially from the year 2000 onwards, while an increasing scientific production of Asian authors was noted recently (Fig.
Download: Download full-size image Fig.
Distribution of papers per continent and year in the period 1988–2014 (N = 519) (A & NZ = Australia and New Zealand).
First author affiliations comprised 39 countries, with the USA and Canada representing more than 60% of all papers.
In Europe, the Nordic countries and the UK represented almost two thirds of the papers.
Elsewhere, Japan, China and Australia were best represented (Fig.
In 18 countries only one or two papers were identified in the given period.
Download: Download full-size image Fig.
Top 20 countries based on the number of publications in the period 1988–2014.
Data analysis Two rules were established for analysis of retrieved papers.
First, full papers were used instead of only abstracts.
Secondly, a ‘one paper one discourse’ rule was adopted, implying that one paper could be allocated to one discourse only, according to the aim to identify ideal-typical discourses, quantify their strength based on the number of publications attached to certain discourse with taking into account their geographical distribution.
This is corroborated by the well-documented similarities and differences of UF in North America and Europe (Konijnendijk et al., 2006).
Each discourse was described based on several elements: rationale of the discourse, prevailing topics, ideas, concepts, storylines or metaphors, key challenges, solutions offered, whether the discourse is contested and its timeframe.
In the discussion, the relevance of findings to urban forestry science and practice and their development are debated.
Results Scientific UF discourses described Six scientific UF discourses of varying strength and geographical distribution were identified (Table 1).
Scientific UF discourses and number of papers associated with each discourse and per continent in the period 1988–2014.
DISCOURSES	E	NA	OTHER	TOTAL Empty Cell	Empty Cell	Empty Cell	AS	A & NZ	LA	AF	Total	Empty Cell Managerial (total)	39	190	10	14	6	2	32	261  Trees	10	100	4	6	1	1	12	122  Forest (woodland)	15	6	3		1	1	5	26  The “Urban Forest”	14	84	3	8	4		15	113 Civic involvement	43	47	5	2		1	8	98 Ecosystem services	10	54	11	2		1	14	78 Biodiversity	20	23	15	6	1	1	23	66 Urban planning	4	1	3	1			4	9 Green infrastructure	2	2	1	1	1		3	7  TOTAL	118	317	45	26	8	5	84	519 E = Europe, NA = North America, AS = Asia, A & NZ = Australia and New Zealand, LA = Latin America, AF = Africa.
The managerial discourse Main rationale of the managerial discourse is achieving healthy, resilient and safe urban forests and trees by means of sound urban forest management.
The discourse included wide array of topics, such as forest and natural resources assessment (tree inventory) (e.g. Pauleit and Duhme, 2000, Walton et al., 2008, Sreetheran et al., 2011), woodland management (Rydberg and Falck, 2000, Nakamura et al., 2005, Gundersen et al., 2006, Nielsen and Jensen, 2007); tree risk assessment and risk management (Smiley and Fraedrich, 1992, Martinez-Trinidad et al., 2010), as well as legal-institutional aspects (Anderson, 1988, Conway and Urbani, 2007), education and research in the field of UF and arboriculture (Wiseman et al., 2011), rules and regulations addressing forest and tree management, and maintenance including effectiveness and efficiency of current approaches and policies (O’Brian and Joehlin, 1992, Ries et al., 2007) (Table 2).
The concept of sustainable forest management is important in UF and some authors offered criteria for assessment of urban forest sustainability (e.g. Clark and Matheny, 1998).
Within the managerial discourse three strands were identified based on the subject of managerial practice, i.e. trees, woodland or the totality of tree and/or woody vegetation (the “urban forest”; Table 2).
In comparison to Europe North American experts seem to place more emphasis on trees and the ‘urban forest’ than on woodland (e.g. Dwyer et al., 2003).
Summary of identified scientific discourses on UF.
Empty Cell	M	CI	ES	BIO	GI	UP Rationale	- Healthy, resilient and safe urban forests and trees	- Making urban areas pleasant - Active civic involvement	- Provision of ES from urban forests - Justification of costs - Gaining support	- Harbouring biodiversity in urban areas	- Optimal distribution of green space - Cost-effective delivery of multiple benefits	- Sustainable urban areas  Topics	- Tree selection - Tree health and risk assessment - Tree growth - Tree inventory - Woodland management - Expert education - Rules and regulations	- Environmental psychology - Public participation in decision making - Social inclusiveness	- Quantification of benefits - Valuation of benefits	- Negative effect of urbanisation on biodiversity	- Planning aspects - Forest and landscape ecology - Policy and institutional aspects	- Planning aspects  Idea, concept, storyline, metaphor	- Urban forests = ecosystems - SFM - Effectiveness and efficiency	- Quality of life - Attitudes - Values - Behaviour - Preferences - Public participation - Social inclusiveness	- Urban forest benefits surpass costs - Urban trees = carbon sinks - Growing trees helps mitigate climate change	- Urban forests as places of biodiversity conservation - Urban forests = ecosystems - The network metaphor - Connectivity (patches and corridors, green systems)	- Optimal distribution of benefits - The network metaphor - Connectivity (hubs and corridors, green systems) - Effectiveness and efficiency	- Green space is necessary for urban sustainability  Key challenge	- Optimal forest structure - Pest control	- Delivering quality green space - Fulfilling people's needs	- Quantification of benefits - Valuation of benefits	- Preserving biodiversity in urban areas	- Optimal distribution of benefits	- Incorporating green elements into existing urban fabric - Securing green space in urban development  Solution	- Modelling (e.g. i-Tree) - Quantitative methods prevail - Use of technology - Experts	- Opinion eliciting methods - Quantitative methods prevail - Experts mostly	- Economic valuations - Use of models (e.g. i-Tree) - Quantitative methods - Experts	- Landscape and urban forest ecology - Quantitative methods - Indicators and landscape metrics - Experts only	- Ecological and green infrastructure networks - Integrative approach to spatial planning - Cost- benefit analysis - Experts (with or without public)	- Holistic approach to landscape and urban planning  Timeframe	- 1988- onwards (USA), in Europe from 2000	- Intensified from 2000	- 1990 onwards, since 2000 in Europe	- Intensified from 2000	- Started in 2010, emerging	- Started in 2000, incidental  Contested	- Tree, woodland and the “urban forest” strand					 BIO = the biodiversity discourse; CI = the civic involvement discourse; ES = the ecosystem services discourse; GI = the green infrastructure discourse; M = the managerial discourse; UP = the urban planning discourse.
In the woodland strand and the holistic conceptualisation of UF (the “urban forest”), often an ecosystems perspective has been taken.
This embodies an ecological and systems logic that is different than when focus is on single tree, e.g. encompassing interconnectedness and interdependency of living organisms and their environment, and complexity and dynamics of ecosystem processes.
The perspective should be handled with care since human activity may have a serious impact on the future of the specific ecosystem and humans themselves.
Furthermore, the institutional setting for UF has been discussed in terms of effect of strategies (e.g. tree ordinances, urban and community tree programmes) for management and protection of trees (e.g. Conway and Urbani, 2007, Muller and Bornstein, 2010).
For enhancing urban forest resiliency and functionality, healthy trees and pest control have been considered as key challenges for urban forest managers.
This calls e.g., for focus on selection of species appropriate for specific climate type, distribution of age classes according to specific management regimes, all with the goal of achieving and if possible maintaining forest resiliency – i.e. the capacity of the forest ecosystem to defend itself from disturbances (e.g. Holling, 2001).
To support this work, various assessment and modelling methods and tools (for example i-Tree) are used to check and monitor whether current urban forest corresponds with set objectives and expectations regarding its quantity, quality and structure.
Among these tools, field measurements (e.g. tree and forest inventory, measuring trees on sample plots) have featured most prominently, either as a stand-alone method (e.g. Stoffberg et al., 2008, Staudhammer et al., 2011), or in combination with remote sensing (Thaiutsa et al., 2008).
Survey questionnaires (Kuhns et al., 2004, Sydnor et al., 2010, Zhang and Zheng, 2012), experiments (Struve et al., 2009, Grabosky and Gucunski, 2011) and remote sensing (Morgenroth and Armstrong, 2012) have been employed less frequent than field measurements (Table 2).
Methods used reflect positivist scientific epistemology and corresponding quantitative methods.
Approaches presented in the papers are expert-based, involving foresters, urban foresters and arborists, while non-experts (lay people) are widely excluded.
The civic involvement (CI) discourse The main rationale of this discourse is making urban areas more pleasant for inhabitants (Table 2), implying that these areas should suit people's needs.
Therefore, the main problem to be addressed is how to deliver quality green space that suits the needs and preferences of urban population and thereby improves their quality of life and sense of wellbeing possible through active involvement.
Citizens have been asked about their preferences and needs and thus put in the role of consumers who choose what they like, while experts are those who have been eliciting these preferences from their ‘customers’ in order to deliver better public service and/or gain public support for their activities.
Concepts included in this discourse have been those depicting human–nature interactions (Table 2).
Publications within this discourse have proliferated both in North America and Europe from 2000 onwards, and publications of authors from other continents only recently started to appear (Garthright et al., 2008, Kirckpatrick et al., 2012).
Environmental psychology studies have dominated the discourse and included topics of people's attitudes and values towards trees and woodland (Crow et al., 2006, Heimlich et al., 2008), preferences for urban forest structure (e.g. Jorgensen et al., 2007) and human behaviour in terms of recreational use of urban forests (Arnberger and Haider, 2005, Sanesi and Chiarello, 2006, Gentin, 2011).
The second important topic has addressed citizen participation in decision making (McPherson and Johnson, 1988, Janse and Konijnendijk, 2007, Buizer and Van Herzele, 2012) or by volunteering for hands-on activities, such as tree planting or pest monitoring (Bloniarz and Ryan, 1996, Still and Gerhold, 1997, Greene et al., 2011).
However, differences were noted in scientific focus between North American and European studies.
The former have paid more attention to topics of participation and motivation of volunteers in urban and community forestry programmes (e.g. Daniels et al., 2014), while the latter have shown greater interest in restorative effects of forests and green space (Hansmann et al., 2007, Roe and Aspinall, 2011).
The concept of social inclusiveness (social integration) has obtained more interest from European authors, especially in terms of social integration of marginal groups (Jay and Schraml, 2009, Seeland et al., 2009), although notably some authors have used the term ‘social inclusiveness’ to discuss involvement of citizens in public participation process (e.g. Van Herzele et al., 2005 or Sipilä and Tarväinen, 2005).
Public participation studies have addressed the topics of who was involved (Sipilä and Tarväinen, 2005), what was the method of participation (Sipilä and Tarväinen, 2005, Lakicevic et al., 2014), whether it was successful (Buizer and Van Herzele, 2012), as well as how likely is that citizens would get involved (Straka et al., 2005, Fleming et al., 2006, Greene et al., 2011).
The most commonly used research method has been the questionnaire survey with (Arnberger and Haider, 2005, Moskell and Allread, 2013) or without visual stimuli conducted either by mail (Still and Gerhold, 1997, Coles and Bussey, 2000, Elmendorf et al., 2005, Ellis et al., 2006), telephone (Lohr et al., 2004, Sanesi and Chiarello, 2006), or on site (Hansmann et al., 2007, Arnberger et al., 2010).
Less common has been use of qualitative interviews (Jay and Schraml, 2009, Mellqvist et al., 2013), while use of experiments has been very uncommon (Roe and Aspinall, 2011).
Only two studies have included qualitative method of walking interviews (Jorgensen and Anthopoulou, 2007, Skår, 2010).
Use of positivistic epistemology and accompanying quantitative methods has dominated the discourse on CI.
Therefore, some authors have advocated for the use of qualitative approaches for better understanding of human-urban forest interactions (McLean et al., 2007, Gundersen and Frivold, 2008).
The ecosystem services (ES) discourse The primary storyline of this discourse sees urban forests as providing multiple ecosystem services (ES).
Provision of the benefits associated with these services is associated with costs.
However, it is claimed that benefits from urban forests surpass the cost of their maintenance.
The main rationale has been to justify the costs of service provision and gain public support transformed into funding, especially when taking into consideration trend of decreased public funding for urban forest (Krott, 2004).
In order to gain public support, evidence that urban forests do provide these services and to what extent is needed.
The key challenge is quantification and valuation of benefits, especially since many benefits are public goods (Table 2).
Use of models for quantification of benefits such as the i-Tree tool (i-Tree Streets, User's manual v.
5.0) and methods of non-market valuation such as contingent valuation (Tyrväinen and Väänänen, 1998, Notaro and De Salvo, 2010, Majumdar et al., 2011, Li and Meng, 2012) or hedonic pricing (Tyrväinen, 1997, Anthon et al., 2005, Kong et al., 2007) have been offered as solutions.
Interest in quantification of urban forest benefits started in North America in early 1990s (Rowntree and Nowak, 1991, Dwyer et al., 1992).
This expert-driven discourse has been much stronger in North America than in Europe, although European publications have increased from the year 2000 onwards.
Some services have been given more interest than others, e.g. carbon sequestration (Rowntree and Nowak, 1991, McPherson, 1998, Nowak et al., 2002, Awal et al., 2010, Stoffberg et al., 2010, Strohbach and Haase, 2012, Zheng et al., 2013), air pollutant uptake (Yang et al., 2005, Nowak et al., 2006, Cavanagh et al., 2009, Wang and Lin, 2012), the effect of urban forests and trees on property values (Tyrväinen, 1997, Anthon et al., 2005, Kong et al., 2007, Donovan and Butry, 2011, Saphores and Li, 2012), and energy savings (Simpson, 1998, Jensen et al., 2003, McPherson and Simpson, 2002).
Other services have been addressed to a lesser extent, such as valuation of aesthetic benefits (Price, 2003, Notaro and De Salvo, 2010), stormwater attenuation benefits (Kirnbauer et al., 2013), rainfall interception by urban forest (Xiao et al., 1998), oxygen production by urban trees (Nowak et al., 2007), mitigation of the urban heat island effect (indirectly related to how to limit stress during summer heat waves) (Hardin and Jensen, 2007), and assessment of visibility of urban forests in cities (Yang et al., 2009).
While some studies have dealt with only one ecosystem service, others have taken a more integrative approach and tried to provide valuation of multiple services.
Quantification and provision of ecosystem services by experts is strongly connected with the concepts of effectiveness and efficiency as reflected in studies using cost-benefit analysis by introducing concepts such as benefit and cost ratios, or net benefits (e.g. McPherson and Simpson, 2002).
The biodiversity discourse This discourse's storyline says that even urban areas can harbour biodiversity and contribute to biodiversity conservation (Alvey, 2006).
This discourse was identified both in Europe and North America, as well as in other continents, albeit to a lesser extent (Table 5) with the majority of the studies published from 2000 onwards (Table 2).
Key challenge for urban forest biodiversity is the effect of urbanisation on urban forests.
Many studies report negative effects of urbanisation on urban forests causing habitat fragmentation, biodiversity loss, and change in species composition or urban forest structure (Kromroy et al., 2007, Sanesi et al., 2009, Hutyra et al., 2011).
Attention has been given also to importance of forest edge structure (e.g. De Chant et al., 2010), forest regeneration in the context of anthropogenic or non-anthropogenic influences (e.g. Lehvävirta et al., 2004) and connectivity between forest patches (e.g. Pirnat, 2000).
Urban forests have to compete with other land uses, especially within an urban development context.
Here the concept of connectivity between habitats comes in, since it allows for creation of green systems or green networks for biodiversity conservation among other services.
Another important concept is that of ‘forest patch’.
Patch size and distance between patches are important for biodiversity conservation and can be indicators of the negative impact of urbanisation on urban forests (Pirnat, 2000).
People are part of an urban system, though having mostly a negative role through for instance urban sprawl (Schmitt and Suffling, 2006), residential encroachment (McWilliam et al., 2010) or trampling (Lehvävirta et al., 2004), act as stressors and cause disturbance in urban forest ecosystems.
This can be reflected in increased presence of alien species or problems with regeneration.
Studies in urban forest ecology and landscape ecology provide evidence that urban forests can harbour substantial biodiversity, allowing for monitoring of land use and biodiversity change due to urbanisation, and therefore, provide input for sustainable urban forest management and guidelines on how to protect biodiversity in urban forests.
Methods used have been exclusively quantitative and include field measurements on randomly selected sample plots, sometimes by using transect method along urban-rural gradient (Sudha and Ravindranath, 2000, Zerbe et al., 2003, Sandström et al., 2006, Warren et al., 2011), spatial analysis by using GIS (Pirnat, 2000, Song et al., 2005, Kromroy et al., 2007), remote sensing (Dumas et al., 2008, De Chant et al., 2010, Kuruneri-Chitepo and Shackleton, 2011) and experiments (Horák, 2011).
Positivistic scientific claims are dominant and solutions are provided by experts only.
Biodiversity and landscape change are quantified by using biodiversity indices (e.g. Shannon-Wiener index), landscape metrics or biodiversity indicators (usually abundance and richness of avian or insect species).
The urban planning (UP) discourse This discourse is to a large extent fragmented with only few papers attached to it from the year 2000 onwards (Table 5), making a detailed account on this discourse difficult.
The rationale of the UP discourse is achieving sustainable cities and green elements are considered as part of the urban fabric (Table 2).
UP should protect existing green space and incorporate new green space in order to produce sustainable cities.
It takes an integral approach to UP and strategic planning for urban forests and green space.
The green infrastructure (GI) discourse This discourse is linked to the urban planning discourse above, but also has specific characteristics that make it into a discourse of its own.
Discussing UF in the context of GI is an emerging discourse (Table 2) and in all papers the term ‘green infrastructure’ has been used explicitly.
The term GI appeared in the USA in mid-1990s, but it certainly does not represent an entirely new idea (Benedict and McMahon, 2001).
Main rationale is optimal distribution of UF and green space, physical and functional connectivity for effective and efficient provision of ES (e.g. Ahern, 2007).
Topics of papers have been various and included planning, ecological, recreational and institutional aspects of GI (Frischenbruder and Pellegrino, 2006, Qureshi et al., 2010, Tzoulas and James, 2010, McLain et al., 2012, Young and McPherson, 2013).
Few studies have addressed recreational use of urban green space networks (Tzoulas and James, 2010).
However, papers have mostly addressed the green elements of GI (see Frischenbruder and Pellegrino, 2006 for an exception).
The network metaphor is part of this discourse and relates to network resembling structure of interconnected green space, whereas the concept of connectivity, both physical and functional, plays an important role (Table 2).
Since only a few papers have been associated with this discourse it is hard to make an elaborate account on this discourse based only on these papers.
Discussion The managerial discourse was identified as the dominant one during the entire period.
Other discourses have coexisted and are not mutually exclusive, to some extent overlapping during the time period studied.
In general, scientific UF discourses have been dominated by North American authors, while larger amounts of European publications have emerged primarily from 2000 onwards.
Overlapping in content has also occurred between the ES, biodiversity and GI discourses.
A major difference between the ES and the biodiversity discourse lies in quantification and valuation of ES, which is inherent to the ES discourse.
On the other hand, biodiversity quantification in terms of using biodiversity indices is also a topic of the biodiversity discourse, but is not connected with monetary valuation.
In this sense the ES discourse is closer to the GI, while approaches developed in ES research can help operationalising multifunctionality as an important principle in GI planning (Hansen and Pauleit, 2014).
The biodiversity discourse and the GI discourse share the concept of connectivity depicted by the network metaphor and hence stressing the importance of interconnectedness, in physical and functional sense, among the parts of the network for biodiversity conservation (e.g. making links between urban and rural areas) and effective and efficient provision of ES.
Still, the biodiversity discourse puts emphasis on biodiversity conservation, while in the GI discourse the goal is delivering multiple services similar to ES discourse.
Furthermore, in comparison to the biodiversity and the ES discourse, the GI discourse has a much stronger social component (e.g. recreational services), especially in Europe.
In general the emphasis on services was dominant, with almost no studies on disservices (see Dwyer et al., 1992, Rusterholz et al., 2009 for exception).
The dominant focus on trees and the “urban forest” in North America and on woodlands in Europe can be explained by historical differences between UF in North America and Europe (Konijnendijk et al., 2006) and provides an example that homogeneity of discourse is not a rule.
The weak presence of the UP discourse could be explained by the selection of journals and selection of the key word.
It is likely that architects and planners traditionally dealing with UP are not publishing in these journals.
The validity of this claim was checked and confirmed by combining the key word “urban forest*” with the key word “urban planning” but looking outside preselected journals.
The concept of sustainable forest management binds the managerial with the CI, ES and biodiversity discourse, since it strives for balance between ecological, economic and socio-cultural aspects of UF.
All these aspects are important for the GI as well, with the distinction in terms of putting an emphasis on optimal distribution of green space elements, whereas spatial planning plays a huge role.
The authors acknowledge that biodiversity is closely linked to ecosystem services, although it rather provides a foundation for services than being a service itself (c.f. EC, 2011).
In the current EU Biodiversity Strategy biodiversity is labelled as “our life insurance” (EC, 2011).
According to the resolution of the European Parliament from 2012 (EP, 2012) the loss of biodiversity causes annual global GDP loss of 3%, while “the benefits of the Natura 2000 network for protected areas only is estimated to 200–300 billion EUR with a total of about 4.5 to 8 million full-time equivalent jobs being supported directly from visitor expenditure in and around these sites”.
However, the economics of biodiversity conservation in urban areas were not addressed in the papers in the given period, despite the growing body of evidence showing that urban areas can significantly contribute to harbouring biodiversity (e.g. Pirnat, 2000, Alvey, 2006, Kantsa et al., 2013).
In spite of general societal trends towards civic involvement in governance of natural resources (e.g. FAO, 2011), studies related to active participation of citizens in decision making and hands-on activities, and collaborative processes/partnerships in urban forestry are largely lacking.
It would help policy and decision makers to see benefits from partnerships and to know what makes successful partnerships, especially in the context of GI.
The need for a diversity of public participation methods and involvement of a wider range of stakeholder groups was identified (Sipilä and Tarväinen, 2005).
Furthermore, testing of existing and development of new methods or modalities of public participation is needed.
For instance, it would be valuable to know whether current instruments and modalities of public participation allow true and just public involvement in decision making or their application only serves legitimisation of something already decided.
Even though positivist methodology and associated quantitative methods are valuable in some cases (e.g. quantification of ecosystem services or urban forest structure), prevalence of quantitative studies may indicate lack of deeper understanding of human–nature relationship that could be achieved by applying qualitative research approaches complementing quantitative approaches as advocated by McLean et al.
(2007) or Gundersen and Frivold (2008).
This could be related also to the fact that qualitative approaches are not always providing conclusions generalisable to the larger population.
Their application is time consuming and hence costly in comparison to their quantitative counterparts.
In the context of reducing public budget allocations for urban forestry (c.f. Krott, 2004) while trying to gain public and/or political support for urban forestry activities favouring quantifiable measures is than understandable to some extent.
This is also in line with the dominant influence of the neoliberal discourse on forestry and UF, especially in the USA (Humphreys, 2009, Perkins, 2011), in which the emphasis is on effectiveness and efficiency, while quantification and use of criteria and indicators help justifying costs for UF activities and gaining public support.
This could be the reason why benefits of urban forests for social integration were weakly addressed, with almost complete disinterest for spiritual meaning of trees for people.
Lately there has been an increasing interest in quantification of carbon sequestration by urban forests (e.g. Stoffberg et al., 2010, Strohbach and Haase, 2012) and some attempts are made to develop carbon-credit market based on urban forests, such as the state of California with its Climate Action Reserve's Urban Forest Protocol being a pioneer in carbon marketing (Climate Action Reserve, 2014).
In some cases carbon offsetting by urban woody vegetation may be high (e.g. Zhao et al., 2010).
However, potential for carbon offsetting by urban forests is still limited partly because of insufficient knowledge about the direct impact of urban forests on atmospheric carbon due to lack of comprehensive measurement programmes (Weissert et al., 2014), but also due to the fact that carbon emissions in cities are much higher than possibility for carbon sequestration by urban trees.
Non-market valuation of urban forest ecosystem services is not widespread.
This could be due to issues related to implementation of methods such as contingent valuation and hedonic pricing (e.g. Krajter Ostoić et al., 2013).
Both are time consuming and need large samples making them costly.
The other possible reason is that researchers might not be necessarily convinced in effectiveness of these methods in quantifying how much people value urban forests.
Lack of discussion on urban forest(ry)’s contribution to climate change adaptation in urban areas is surprising, especially in the context of recent emphasis on climate change adaptation and human health (c.f. EEA, 2012, EC, 2013b).
Quantification of reduction of urban heat island effect by urban forest has not been given much scientific interest in the given period (c.f. Hardin and Jensen, 2007 for exception), and in the limited available work results were not discussed in the context of climate change adaptation.
Adaptation of urban forest management to impacts of climate change has not been discussed either, especially when compared to number of publications related to adaptations in forest management (e.g. Blennow et al., 2012).
The need for transdisciplinary and participatory approaches to studying the effects of climate change on urban forests and people in urban areas as well as better understanding how GI is modulating urban heat island effect has been articulated by Niemelä (2014).
However, GI approach is acknowledged as a mean serving climate change adaptation (EC, 2013a, EC, 2013b).
Neither is there discussion related to how benefits from urban forests serve existing policies (e.g. energy policy, climate change adaptation, health).
In general there is a lack of research on urban forest governance (c.f. Lawrence et al., 2013).
While the urban forestry definition calls for interdisciplinary and cross-sectoral research (Randrup et al., 2005), this is not reflected in scientific practice.
Conclusions Discourse analysis showed the dominance of managerial discourse in the scientific literature in the given period, followed by the civic involvement, ES, biodiversity and GI discourse.
Even though overlapping to some extent, these discourses were not mutually exclusive.
Scientific production has been led by North American authors and followed by European authors, while the number of papers from other continents is still modest.
Dominance of quantitative methods associated with positivist epistemology indicates the need for deeper understanding of human–nature relationship and corresponds with the prevailing influence of neoliberal discourse in urban forestry.
More emphasis on social aspects of urban forestry including public participation in decision making is certainly expected in the future when having in mind constantly growing population in urban areas.
Despite the increasing interest in quantification of ES, especially carbon sequestration by urban trees, the body of evidence on the effects of urban forests on the quality of life in urban environments is still limited due to often fragmented studies and lack of comprehensive urban forest monitoring, while possible negative effects are almost completely ignored.
There is a surprising lack of discussion on climate change mitigation and adaptation both in terms of effect of climate change on urban forests and the mitigating effect of urban forests on climate change impacts on urban population.
The same is evident for contribution of urban forests and urban forestry to public policies, and the role of urban forests in green economy, green job creation and innovation potential.
Great importance of economic valuation of ES for advocating green agenda to policy makers, especially in NA and UK, is not reflected in scientific publications.
DA is possible limited due to selection of the keywords and journals.
The term urban forest may not be strongly rooted outside of English-speaking areas.
Secondly, the predefined set of journals taken into account possibly contributed to prevalence of North American authors.
Thirdly, language bias should be acknowledged since only publications in English were taken into account.
DA proved useful for exploring the discursive character of the UF concept based on scientific publications.
Scientific production related to the urban forests is not homogenous and highly dominated by North-American and European authors.
In the future the managerial discourse is expected to remain the strongest, while the GI discourse is expected to gain in influence.
Focus on ES as being inherent in the ES, biodiversity and GI discourse, especially in the context of biodiversity loss and climate change would not lose its grip.
In the end it can be concluded that more transdisciplinary and participatory research related to urban forests is needed to help in dealing with pressing societal issues such as climate change.
Existing urban forest literature is strongest in its quantification and qualification of the benefits and care of trees, and not in its ability to assess the results of lack of investment in trees.
This paper presents the results of a literature review on the “Costs of Not Maintaining Trees” commissioned by the ISA Science and Research Committee.
The authors summarized the literature from within the field of arboriculture/urban forestry to answer the questions: What are the costs of maintaining trees and the urban forest?
And, What are the costs of not maintaining trees?
Present here is a detailed summary of the literature on the costs of maintenance and lack of maintenance for types of tree care commonly included in municipal budgets (planting, pruning, removal, pest and disease management) and a brief review of costs associated with less-studied types of tree care (including tree risk management; watering; mulching; fertilizing and nutrient management; staking, cabling, and bracing; tree protection; and infrastructure repair).
The authors suggest that future literature should aim to examine the influence of maintenance regimes on costs and tree outcomes, including examining how the frequency, intensity, duration, and extent of tree maintenance activities is connected to the structure, function, and benefits of trees.
Key Words Cost of Not Maintaining TreesLiterature ReviewMaintenance CostsPruningPlantingRemovalMunicipal ForestryDeferred MaintenanceUrban ForestryUrban Tree Maintenance The benefits of trees are frequently monetized and valued.
Researchers and practitioners of urban forestry can put a value on the benefits of trees with reasonable ease, using the i-Tree software (or its precursors, STRATUM and UFORE, now the i-Tree Streets and Eco modules, respectively) and other direct or implied valuation methods [e.g., the Council of Tree and Landscape Appraisers (CTLA) valuation methods, replacement cost valuation, willingness-to-pay surveys, hedonic property value methods].
The value of these benefits is frequently then used to justify investments in trees (e.g., McPherson et al.
2005; Peper et al.
Ideally, an economic analysis of urban tree benefits accounts for costs associated with planting through removal to create net benefit models (i.e., through benefit-cost analysis).
Net benefits occur when benefits exceed the costs incurred to obtain these benefits.
The costs of urban tree maintenance and management are less understood.
In a systematic review of studies that examine the benefits and costs of urban trees, Roy et al.
(2012) found that only 15.6% (18) of 115 papers reviewed discussed the problems or costs of urban trees.
The most common type of problem discussed was environmental (e.g., the release of volatile organic compounds), while explicit costs (e.g., money paid for tree pruning services) are most frequently monetized only in terms of budget outlays or expenditures by municipal urban forestry programs (Roy et al.
Studies that examine the costs and benefits of the urban forest—in an attempt to calculate the net value of urban trees, for instance—frequently weigh municipal budgets (“costs”) against the ecosystem services (“benefits”) produced by public trees (e.g., McPherson et al.
2005; McPherson et al.
2006; Peper et al.
Tree maintenance funding at the municipal level is limited by the economic principle of scarce resources.
There are only so many resources (e.g., money, time) available to allocate.
Tree care budgets are frequently considered non-essential or less-essential city services when compared to police departments, fire departments, road projects, schools, and other public services.
Thus, tree maintenance can frequently find itself on the chopping block during budgets.
Sometimes, entire urban forestry programs are cut; for example, the entire urban forestry department of Gary, Indiana, U.S., was eliminated during the 2009 budget year as a result of the Great Recession (Krause et al.
And this was not a new problem: a 1983 survey of 329 municipalities reported that the most commonly cited limiting factor to tree care was lack of funding (Tate 1984a).
Practitioners of urban forestry need tools to help determine minimally sufficient levels of spending on the provision and maintenance of trees in cities in order to meet diverse urban forestry program goals.
With this in mind, the International Society of Arboriculture commissioned a literature review to examine “The Costs of Not Maintaining Trees.” This paper is the second of three resulting from this literature review, and addresses the literature from within the fields of arboriculture and urban forestry (including municipal, commercial, and utility forestry), on the topic of tree maintenance costs.
[The first paper was published in Arborist News in February 2015 (Hauer et al.
The final paper will summarize tools and strategies from other fields that may help inform how arboriculture/urban forestry researchers and practitioners view the costs of maintenance.]  LITERATURE REVIEW METHODS  Listen Researchers reviewed literature relevant to the costs of maintenance contained in the published records of the two main scholarly journals in the field of urban forestry—Journal of Arboriculture/Arboriculture & Urban Forestry (JOA/AUF; 1975 to June 2013) and Urban Forestry & Urban Greening (UFUG; 2002 to June 2013).
To supplement the systematic reviews of JOA/AUF and UFUG, researchers also performed keyword searches of scholarly databases to obtain literature from 1980 to June 2013 published in other major English-language journals related to arboriculture/urban forestry.
Databases queried during the literature search included: Google Scholar™, Web of Knowledge™, JSTOR®, SciVerse, and the University of Minnesota Urban Forestry Database.
Criteria for selecting articles for inclusion in the literature review included:  The article is within the discipline of urban forestry and includes discussion (qualitative) or measurement (quantitative) of a “cost” (monetary, opportunity, social, human, ecological, environmental, forgone benefit, etc.) or “benefit” (economic, social, human, ecological, environmental, etc.) resulting from some type of management of urban trees.
For articles not published in JOA/AUF or UFUG, the article was published between January 1980 and June 2013.
The article was published in English, or at least an abstract was available in English.
Relevant review articles were included, and the relevant original research articles discussed therein were also consulted.
Opinion pieces (or opinion pieces billed as review articles – mostly from older issues of JOA/AUF) without references were included in the review, but were given less emphasis in qualitative summaries of topic areas.
Books (textbooks, reference books, and popular books) and book chapters were excluded from the literature search, except where these provided sources of peer-reviewed articles.
Professional whitepapers and government reports (e.g., those from the U.S. Forest Service or other appropriate entity) were included in the literature search, as long as they were scholarly in nature.
Selected articles (or their abstracts, if full text was unavailable) were added to a collaborative citations folder using the Mendeley citation software (Mendeley Ltd, New York City, New York, U.S.).
Each article was read by at least one investigator and coded for the list of attributes in the Appendix using a Microsoft Excel® spreadsheet.
Dollar Values All dollar values presented in this text are in real values [current-day equivalent, expressed as 2013 dollars (U.S., Canadian, or Australian) or 2013 Euros], with nominal values (numeric dollars/Euros from the year the article was originally published) and year in parentheses (e.g., 1986$).
U.S. dollars were converted from nominal to real values using the U.S. Bureau of Labor Statistics Consumer Price Index inflation factors (BLS 2015).
Canadian dollars were converted from nominal to real values using the Bank of Canada Inflation Calculator (BOC 2015).
The single study from Australia that reported costs in local dollars ($AUD) was conducted in 2013 (Ryder and Moore 2013) and required no conversion from nominal to real values.
Euros were converted using European Union Consumer Price Index inflation factors for June 1 of beginning and end years (FXTOP 2015).
The Logic of Linking Maintenance to the Benefits and Costs of Trees It is useful to think about the logic of how maintenance is linked to the benefits and costs of trees (Figure 1) before summarizing the literature on the costs of maintaining and not maintaining trees.
Arborists and urban foresters intuitively know that the level of care or maintenance performed on a planted tree is linked to tree establishment, survival, growth, condition, and longevity (i.e., tree success).
Survival, growth, and condition are closely connected to one another and to the structure of a tree (e.g., tree size, leaf area) and of the urban forest (e.g., canopy cover, diversity, age distribution).
Tree structure, in turn, impacts the functions provided by the urban forest and ultimately the level of benefits generated by the tree.
Thus, less-than-optimal maintenance may lead to decreased benefits produced by the urban forest (Figure 2, dashed lines).
Theoretically, if one can determine how different levels of maintenance may differentially impact the level of benefits provided then he or she can determine the amount of benefits or value lost by reducing or eliminating maintenance.
The benefits lost are the “costs” of not maintaining trees.
Download figureOpen in new tabDownload powerpoint Figure 1.
Maintenance directly impacts tree structure, which in turn impacts the functions and benefits provided by the urban forest.
Download figureOpen in new tabDownload powerpoint Figure 2.
Hypothetical cost and benefit profiles over the life-time of an individual tree (street tree), with (solid lines) and without (dashed lines) adequate maintenance.
Benefits are maximized during the mature phase of a tree, and decline rapidly through senescence, while costs show an inverse pattern.
Compare the benefits and costs profiles over the course of a tree’s life cycle in this figure to the profiles over the tree size classes in Figure 5.
Note that the benefits and costs profiles for an individual tree will vary depending on the tree’s location, the party benefiting from and incurring costs of the tree, and other factors (weather, etc.).
Figure modified from Vogt et al.
Note that because this literature review is not a comprehensive review of the benefits of trees, researchers have only included information about tree benefits as it has been connected in the literature to tree maintenance activities, lack of maintenance activities, or maintenance costs.
The authors acknowledge that when trees are not planted or maintained properly and then die, benefits of all types these trees might have provided are lost—environmental, social, economic, or otherwise.
In the literature review that follows, researchers include mention of specific types of benefits only when research has explicitly and quantifiably linked those benefits or loss thereof to a particular maintenance activity.
Maintenance throughout a tree’s life Maintenance can be linked to tree success both at the beginning and end of its life span.
Early in a tree’s life, during the establishment and immature (i.e., juvenile) phases, maintenance must be adequate to ensure early survival and establishment in the urban landscape.
Presumably, any post-planting maintenance performed on a tree that improves its chances of survival to maturity or lengthens the time that tree spends in its mature phase (where benefits are produced in the greatest amount) increases the monetary value of that tree (Figure 2).
The cost of not maintaining trees early in life may translate to greater maintenance costs down the road; this is deferring maintenance (and its costs) to the future in order to save on maintenance costs today.
Later in a tree’s life, maintenance may aim to extend the tree’s life span or prevent tree failure.
In this way, late-stage maintenance can defer removal costs.
For instance, structural pruning or crown thinning may aim to improve tree stability and reduce canopy weight and thereby reduce the likelihood of tree failure (although the research supporting this connection is not well documented; Clark and Matheny 2010).
If maintenance does prolong a tree’s useful life (i.e., delays the onset of senescence and a tree’s removal), it increases the amount of benefits it produces over its life span.
Alternatively, removing the dangling limbs on an aging tree can prevent these limbs from failing (during a wind storm or otherwise) and damaging people or property, and thereby avoiding subsequent repair- or liability-related costs (e.g., Bakken 1995).
Tree pruning to remove high-risk limbs and removal of the entire tree can be considered a type of maintenance that purportedly can save money due to avoided litigation costs (depending on frequency, likelihood, and costs of litigation).
The stylized benefits and costs curves presented in Figure 2 are in reality influenced by tree location, weather, pests/diseases, and many other factors both controllable and not controllable by people.
Useful concepts from economics Translating tree maintenance into urban forest benefits can be informed by some key concepts from economics.
Accounting for the costs and benefits of any activity—from a factory producing widgets to the ecosystem services produced by the urban forest—involves principles of effectiveness and efficiency.
Efficiency is the optimal use of resources (inputs) to produce a given output, and can be qualitatively or quantitatively expressed, such as the number of dollars spent to prune trees per one-diameter-inch of trunk size.
Effectiveness is less measurable, aiming considering whether what is done actually works and achieves an objective or outcome.
Evaluation of efficient and effective use of resources also considers the element of time (when the maintenance occurred during a tree’s life cycle), the changing value of money (e.g., due to inflation; see also the “dollar values” in METHODS), as well as risk and uncertainty in the use of resources (not to mention human willingness to accept risk and uncertainty).
Researchers consider these concepts implicitly in the discussion of the literature that follows.
RESULTS & DISCUSSION  Listen Summary of Publications Reviewed Over 300 articles were compiled, of which 163 were deemed useful for the literature review and included in the annotated bibliography and summaries here.
In this section, researchers briefly summarize the themes from these articles, placing greatest emphasis on those that were found most helpful in elucidating the costs of not maintaining trees.
The cumulative number of articles published on the costs of maintenance from the two flagship journals in the field (JOA/AUF and UFUG) by year of publication is shown in Figure 3; the rate of publication of relevant articles is relatively constant over the last four decades.
Other journals from which more than one article were reviewed include the Journal of Environmental Horticulture, Landscape & Urban Planning, and Arboricultural Journal.
Most articles discussed one or two types of maintenance, although some articles did discuss maintenance tasks in the aggregate or did not specify types of maintenance (Figure 4).
Many articles reviewed did not examine costs in explicitly economic terms (59 articles) or only discussed inferred economic costs (34 articles).
These inferred economic costs include articles that primarily focus on labor productivity or time-per-task (e.g., Pierce 1980), as this could be easily turned into monetary costs if the cost of labor were specified.
Download figureOpen in new tabDownload powerpoint Figure 3.
Sources of articles from within the field of arboriculture/urban forestry (inset pie chart) and the number of articles published per year (solid line) and cumulatively (dashed line) in the two flagship journals in the field, Arboriculture & Urban Forestry and Urban Forestry & Urban Greening related to the costs of tree maintenance.
Download figureOpen in new tabDownload powerpoint Figure 4.
Number of articles examining each type of maintenance.
Articles examining more than two distinct types of maintenance or in which maintenance activities were not disaggregated are designated Multiple/Many.
Maintenance activities included in Other: staking, wrapping trees against salt or frost damage, inventorying, and forest (stand) management practices.
What Are the Costs of Trees?
In order to evaluate the costs of not maintaining trees, one needs to consider the benefits and costs incurred over the lifetime of a tree under different maintenance scenarios.
Costs include the direct costs of provision and maintenance of urban trees, direct costs incurred as a result of infrastructure interference, costs inferred from environmental externalities, and opportunity costs (Table 1).
The first three of these are summarized briefly hereafter; the latter is not discussed in the current urban forestry and arboriculture literature.
Note that the costs of trees are the same neither for all types of trees (e.g., different species) nor for all types of planting situations (e.g., street versus park trees).
View inlineView popup Table 1.
Types of costs in urban forests.
Direct costs associated with provisioning the urban forest Maintenance-related costs begin at the time of planting (also called installation costs) and continue throughout a tree’s useful life through the time of removal.
Maintenance costs vary throughout a tree’s lifetime and by species and location (Schwarz and Wagar 1987; McPherson 2003; Leal et al.
Planting and establishment costs can include the cost of purchasing the tree, any costs associated with reworking infrastructure around the tree (e.g., removing sidewalk or paving stones, modifying or amending soil in the planting space), the cost of labor to install the tree, and any subsequent at-planting maintenance, such as staking, pruning, mulching, or watering.
Tree maintenance activities such as pruning, mulching, watering, and pest and disease management also occur throughout the lifetime of the tree and have costs during this time as well.
Finally, during senescence, tree maintenance costs related to the removal of dead branches to reduce liability and risk and eventually removal of the entire tree could be substantial.
This pattern of maintenance is what drives the theoretical costs throughout a tree’s life cycle that are seen in Figure 2, and different levels of maintenance at different points in time may affect subsequent maintenance needs.
Costs associated with tree interference with infrastructure Costs that result from infrastructure interference, damage, and repair are usually incurred when an improperly selected tree is used, the tree is not planted correctly, or is planted in an inappropriate location.
Vegetation improperly located may block road signs, leading to vehicle accidents, or block business signs, decreasing visibility of a store.
Sidewalk or street repairs are commonly observed for trees that are planted in too small of planting areas and thus their root systems damage the pavement (see section “Infrastructure repair”).
Additionally, costs can be incurred due to lack of service resulting from tree-initiated power outages (e.g., a tree falling on a power line).
Fire may result from tree contacts with electrical lines.
Tree-caused power outages result in the costs of repairing the line and restoring service as well as cause lost electricity revenue during the outage (see section “Utility pruning costs”).
Tree or branch failures also have costs in terms of roads blocked either due to the failed tree itself or to the tree crew cleaning-up the failed tree or branch (Randrup et al.
Negative externalities as costs Externalities are outcomes (benefits or costs) of a good or service that are not accounted for in the market price of that good or service.
Most of the benefits of urban trees (e.g., stormwater management, aesthetic beauty) can be considered positive externalities.
However, there are also negative externalities of trees.
Costs related to the negative environmental externalities (occasionally called “ecosystem disservices,” per Escobedo et al.
2011) of trees include net emission of biogenic volatile organic compounds (BVOCs) during the life of some tree species, leachate from foliar nutrients into surface water, as well as release of carbon dioxide and other greenhouse gases (e.g., methane) during decomposition at the end of a tree’s life.
Environmental costs can be related to the maintenance regime used by urban foresters taking care of an urban tree population.
For instance, tree maintenance requiring the use of equipment (e.g., a front end loader, chip truck, aerial lift truck, wood chipper, or a chain saw) that burn fossil fuels releases of carbon dioxide into the atmosphere [see, for instance, Nowak et al.
(2002), described in next section].
Life cycle assessment of costs Life cycle assessment is one means of assessing the externality-related costs of urban trees that takes into account the entire life cycle of a tree from production (i.e., nursery) to removal and disposal.
One common cost examined via life cycle assessment is greenhouse gas or carbon emissions resulting from urban forest activities.
For instance, Nowak et al.
(2002) examine the impact of minimal (low-carbon), “conservative” (i.e., deferred), and “intensive” maintenance scenarios on the life cycle net carbon balance of planted urban trees: Minimal (low-carbon) maintenance involved no return visits after tree planting, while conservative and intensive maintenance scenarios involved pruning visits with chain saws, an aerial-lift truck, and a wood chipper every 15 and 7 years, respectively.
Their analysis revealed that conservative and intensive maintenance had a negative impact on a tree’s carbon budget, resulting in a decrease in the length of time between tree planting and the last positive point at which carbon sequestration no longer exceeded carbon emission (Nowak et al.
Kendall and McPherson (2012) present a life cycle assessment that measures the greenhouse gas emissions of tree production.
In the assessment, they consider all sources of emissions, including those associated with maintenance activities at the nursery, such as materials needed for staking, or nutrients used to amend soil (Kendall and McPherson 2012).
In a similar analysis, McHale et al.
(2007) investigate the carbon footprint of tree planting initiatives in the context of carbon credit markets.
This article summarizes application of a set of guidelines for calculating carbon emissions and reductions associated with urban tree plantings to Colorado, U.S. cities to assess the cost effectiveness of tree planting in the carbon trading market (McHale et al.
Maintenance is considered in two parts of their analysis: 1) in terms of emissions generated by “tree care activities” and 2) in total monetary costs of planting and maintenance over a 40-year time frame (“how often the trees are watered, pruned, or fertilized, and whether or not volunteers are involved in these processes”) (McHale et al.
However, as maintenance rates were fixed and were not examined as part of the analysis performed with either Kendall and McPherson (2012) or McHale et al.
(2007), researchers cannot compare estimates of emissions costs between maintenance scenarios.
Other authors have examined the costs of urban greenspace more generally using a life cycle approach (e.g., Jo and McPherson 1995; Jo 2002; Strohbach et al.
Costs not considered in current literature Some costs of urban trees are largely ignored in the current literature.
Commonly omitted costs include those incurred for leaf collection and the release of biogenic volatile organic compounds into the atmosphere.
Where BVOC release is included as a “cost,” it is usually included in the estimation of air pollution or emissions reductions rather than itemized as its own cost (e.g., McPherson et al.
Pollen release from trees may exacerbate costs of allergies and medical treatments.
A final important omitted cost is the opportunity cost of alternative land uses for the tree planting location.
When trees are planted in the public right-of-way, the space cannot be used for other things, such as an outdoor café, a bike lane, parking, or additional lanes of traffic (Loukaitou-Sideris 2011).
Assessing the costs of not maintaining trees Ryan (1985) was one of the only authors to explicitly mention the costs of not maintaining trees in light of municipal tree budgets: “… trees that are not maintained at regular intervals soon become hazards due to deadwood and windthrow.
This cannot only upset your budget but may also cause considerable loss of life and property” (p.
In the paper, Ryan presented a dialectic for construction of a municipal tree maintenance budget and claims that both the “Estimated Cost of NOT Doing Tree Work” (emphasis original) and the “Estimated Savings by Doing Work” are important parts of justifying budgets (Ryan 1985).
However, this article provides no specific suggestions for how to estimate these costs.
Ryan (1985) argued that urban trees should be considered part of urban infrastructure (as what is, in modern terms, “green,” or living, infrastructure, to contrast with grey infrastructure, such as roads and sewer systems), and uses this idea to describe how the benefits of trees can be used to help justify costs of city tree budgets.
In a related article published in the Journal of Arboriculture, Schwarz and Wagar (1987) asked, “how much should you spend now [on street tree maintenance] to save later?” These authors presented three accounting frameworks that can be used to determine when preventative maintenance can result in decreased overall tree maintenance costs (Schwarz and Wagar 1987).
However, the methods presented (discounted present value of future benefits, internal rate of return, and service-life extension value or useful-life value) require that maintenance needs in the future be estimated (Schwarz and Wagar 1987), and the article did not provide guidance on how exactly to predict maintenance needs or estimate what they might cost; the authors also choose a discount rate that has large impacts on the conclusions of the study.
Maintenance Commonly Included in Municipal Budgets Costs of trees are frequently expressed in terms of expenditures by the parties who commonly pay for the care of trees.
(2007) estimated that the private arboriculture industry (excluding municipalities, nonprofits, or other non-commercial firms, and excluding utility arboriculture) collected nearly USD $9 billion in gross receipts in 2002 (although this analysis is unable to disaggregate this figure into types of tree care or maintenance).
Municipality expenditures on maintenance are more easily disaggregated by type: the most well-established types of tree maintenance activities—planting, pruning, removal, infrastructure repair, and pest/disease management—frequently appear as line items in city budgets (Kielbaso et al.
1982; Kielbaso 1990; Tschantz and Sacamano 1994; Kenney and Idziak 2000), while items like watering and mulching appear far less frequently (e.g., Thompson et al.
Municipal costs are also commonly reported in benefit-cost analyses (studies that compare the costs and benefits of urban forests (e.g., McPherson et al.
1997; McPherson et al.
1999; Maco and McPherson 2003; McPherson 2003; McPherson et al.
2005; Millward and Sabir 2010; Roy et al.
For example, McPherson (2003) reported on the size-specific maintenance costs for planting, pruning, removal, root-related infrastructure repair, pest management, and liability associated with 10 species of street trees in Modesto, California, U.S. (results reproduced in Figure 5).
Download figureOpen in new tabDownload powerpoint Figure 5.
Tree value increases as the size of trees increase (top).
The cost of tree maintenance varies by life stage of tree and maintenance requirement (bottom).
Figure reprinted from McPherson (2003).
Surveys of municipalities in the United States (400 municipalities: Kielbaso et al.
1982; 1,534 municipalities: Kielbaso 1990; 419 municipalities: Tschantz and Sacamano 1994), in Canada (92 municipalities: Kenney and Idziak 2000), and in Santiago, Chile (Escobedo et al.
2006) have reported on the total tree-related expenditures of municipal governments.
In the United States, tree expenses were distributed among street trees (61%) and park trees (24%; Kielbaso et al.
1982), and as a whole accounted for less than one-half of one percent of total city budgets (Kielbaso 1990).
Average annual per-capita municipal tree expenditures in the United State were $7.70 in 1974 ($1.63 in 1974$; Kielbaso 1990), $6.19 in 1980 ($2.19 in 1980$; Kielbaso et al.
1982), and $5.53 in 1986 ($2.60 in 1986$; Kielbaso 1990).
Annual per-tree expenditures were $30.48 in 1980$ ($10.78 in 1980$; Kielbaso et al.
1982) and $22.57 ($10.62 in 1986$; Kielbaso 1990).
Kenney and Idziak (2000) conducted a survey of Canadian municipalities between 1996 and 1998 and reported that average expenditures on tree maintenance were CAD $3.00 per capita and CAD $23.55 per tree annually ($2.20 and $17.29, respectively, in 1997$).
(2006) report results of expenditures by Santiago’s regional government on “green area management,” finding that municipality-level spending varied from $27,366 to $1,628,304 ($16,000 to $952,000 in 1991$) per year, while per-tree maintenance costs ranged from $0.17 to $6.84 ($0.10 to $4.00 in 1991$).
Pruning Of all urban forest maintenance activities, pruning is the most studied in terms of economics.
Pruning is performed throughout the lifetime of a tree for various reasons, including: improving growth form (Evans and Klett 1985; Ryder and Moore 2013); alleviating structural problems, such as removal of deadwood (Hensley 1979); crown raising (Clark and Matheny 2010); and managing pests or diseases (e.g., Dutch elm disease: Himelick and Ceplecha 1976; Gregory and Allison 1979; Sherald and Gregory 1980; Baker and French 1985; see section “Pest and disease management”).
Pruning costs are related to the type (and goals) of pruning performed (Ryder and Moore 2013).
Municipal pruning costs Tree pruning costs are typically the most expensive maintenance item in municipal tree programs (Kielbaso et al.
1982; Kielbaso 1990; Tschantz and Sacamano 1994).
Surveys in 1980 and 1986 reported that pruning accounted for 28% and 30%, respectively, of the municipal tree care budgets of U.S. cities (Kielbaso et al.
1982; Kielbaso 1990).
Tschantz and Sacamano (1994) reported that tree pruning accounted for an average of 36.9% of tree care operations costs and mean pruning expenses were $130.04 per tree ($82.73 in 1994$).
In a benefit-cost analysis for 10 street tree species in Modesto, California, U.S. McPherson (2003) reported that pruning was the greatest category of maintenance costs for all species, ranging from $91 ($63 in 1997$) per tree pruned for London planetree (Platanus acerifolia) to $328 ($226 in 1997$) per tree for Modesto ash (Fraxinus velutina ‘Modesto’).
Privatizing tree care operation is often suggested as a method to reduce costs through potential efficiencies (e.g., shared equipment and labor costs across multiple jurisdictions) that the private market place may bring into the public sector (Diller 1975; Tate 1986; Tate 1987; Tate 1993).
The data to support this was not found in peer-reviewed papers.
New York City, New York, U.S., found contracting to improve flexibility and efficiency of tree care operations (Lough 1991).
Similarly in Los Angeles, California, U.S., contracting tree-trimming services in combination with in-house staff was found to facilitate shifting from a 16.5- to 6-year tree pruning cycle (Kennedy 1990).
As reported in a local newspaper at the time, the City of Saint Paul, Minnesota, U.S., put the tree pruning operations out for bid and found the city workforce submitting the lowest bid of $35.64 per tree ($25.49 in 1999$) in comparison to private firm bids ranging from $53–$144 per tree ($38–$103 in 1999$) (Duchschere 1999).
A key to successful incorporation of private contractors is developing definitive specifications that are inspected for compliance and enforced by city staff; Henning (1990) and Klonowski (1991) provided mechanisms to evaluate contractor performance.
Worker efficiency studies Even though tree pruning typically receives the greatest budget allocation of all municipal tree maintenance activities, it is still often underfunded in comparison to needs (Sievert 1988).
For this reason, efficient allocation of resources for pruning is important.
Tracking worker activities, productivity, and performance over time (per O’Brien and Joehlin 1992) could help develop models of species- and size-specific required pruning time and estimate pruning time for future work while allocating maintenance resources appropriately (O’Brien et al.
The size of the tree was found to be positively correlated to the time required to prune, for disposal, and the amount of woody debris collected during pruning operations (O’Brien et al.
1992; Churack et al.
1994; Zillmer et al.
Thus, maintenance needs and costs of trees increase as the size of the tree increases (Miller et al.
2015; Nowak 1990).
From an early work in the 1960s, Wagner (1970) reported that a three-person crew was most efficient, requiring 54 work-minutes per trim in comparison to 59, 100, and 141 minutes for four-, five-, and six-person crews performing utility line pruning.
In comparison, Overbeek (1979) reported that the City of Grand Rapids, Michigan, U.S., found a four-person crew to be most efficient.
The challenge is to maximize worker productivity by developing standards for different operations and collecting data that can be used to make management decisions.
Pierce (1980) reported that crews in Omaha, Nebraska, U.S., spent 36% of work time on pruning activities (although no information is provided on the size of the urban forest maintained by tree crews).
(1994) authored the first study to describe through mathematical formulas the time requirements for pruning tree species in Milwaukee, Wisconsin, U.S. They found a strong positive relationship between pruning time required and tree diameter for four common species: green ash (Fraxinus pennsylvanica), honeylocust (Gleditsia tricanthos), littleleaf linden (Tilia cordata), and Norway maple (Acer platanoides) (Churack et al.
Waste wood stack time and waste wood yield were also quantified, as were trends similar to that as discovered with pruning time were discovered for the four species (Churack et al.
(2000) presented an updated productivity timing system for tree climbing training in Milwaukee, Wisconsin, U.S. The application of this technique in other regions would yield robust estimates of costs of pruning municipal tree populations, when combined with tree growth rates, tree population characteristics (e.g., tree size and tree species), and labor costs.
Utility pruning costs Pruning is performed extensively by utility companies and many articles discussing the economics of pruning are from a utility forestry perspective.
(1992) reported that pruning takes longer for trees under utility wires.
The cost of not pruning around utility wires or poles is clear: a lack of tree pruning can result in tree or branch failures or interference with utility lines (e.g., phone, electricity, cable, internet) during storm events, resulting in costly clean-up, repair, lost customer billing time, safety issues resulting in human injury or death, and more (Medicky 1976; Perry 1977; Dykes 1980; Ulrich 1983; Johnstone 1988; Kuntz et al.
2002; Guikema et al.
Utility pruning, therefore, is frequently examined in the context of “what can be purchased by budget expenditures for tree trimming in terms of reliability” (Perry 1977, p.
Concepts like the “minimum permissible clearance” distance between tree branches and utility infrastructure (Medicky 1976, p.
56), pole-miles of line maintained (Ulrich 1983), “optimal” maintenance scheduling algorithms (Kuntz et al.
2002), and other performance criteria [e.g., cost-effectiveness of pruning efforts (David 1979; Holewinski and Johnson 1983); time efficiency (Henning 1990)] infuse the utility pruning literature.
Ultimately, utility companies have a strong economic incentive (i.e., profit margin) for optimal allocation of resources toward pruning efforts.
Avoiding fines for electrical outages also factors into resource allocation.
Authors who have most comprehensively examined the costs of deferring utility pruning include Browning and Wiant (1997), Kuntz et al.
(2002), and Goodfellow and Kayihan (2013).
Browning and Wiant (1997) analyzed the time and costs of pruning utility trees in terms of time per tree as time varies by several factors, including time since last pruning, pre-work clearance distance, branch length, time of pruning, and tree diameter.
Results indicate that for each additional year maintenance is deferred past the optimum pruning cycle length, USD $1 saved now will have to be replaced by $1.47–$1.69 of spending four years in the future, and will yield approximately twice the amount of pruning waste for disposal (Browning and Wiant 1997).
(2002) presented a “quantitative approach to maintenance scheduling” aimed at reducing the cost of maintenance activities and increasing the reliability of utility service (p.
The authors used an optimization problem approach to minimize or maximize one of three objective functions with respect to maintenance crew availability: minimize total cost of reliability, minimize cost per a given reliability, or maximize reliability for a given cost (Kuntz et al.
The cost of reliability was estimated as customer willingness-to-pay to avoid a power outage; the cost of maintenance efforts was computed as cost per mile of line maintained (Kuntz et al.
Results indicated that computer-optimized maintenance schedules improved the interruption frequency index (a measure of utility system reliability where greater index values indicate better performance) by 4%–6.5% over a fixed-interval maintenance schedule (Kuntz et al.
Most recently, Goodfellow and Kayihan (2013) conducted a comprehensive review of the models used in scheduling utility pruning and identified five commonly used models: clearance, cost of deferral, reliability, annual increment, and regulatory mandate.
These authors then presented a probability-based “bow-tie analysis” model that weighs an acceptable level of risk against a desired level of performance in assessing causes and consequences of an incident (Goodfellow and Kayihan 2013).
In this light, preventative maintenance measures impact the likelihood of an incident occurring (i.e., tree failure and power system interruption), which mitigating maintenance efforts impact the relationship between the incidence and the consequence or result that occurs.
The authors identified a suite of variables that can be assessed in examining and weighing risk; see Goodman and Kayihan (2013) for the complete literature review and model.
Utility rights-of-way also employ chemical means of controlling growth and form of trees near utility wires.
Several authors in the late 1970s and early 1980s examined chemical growth control (Olenick 1977; Carvell 1975; Domir 1978; Domir and Roberts 1983).
Flurprimidol provided effective growth reduction; however, stem cracking, wood discoloration, and injection site weeping led to the discontinued use (Miller and Abbott 1990; Chaney 2005).
Paclobutrazol currently is used for tree growth reduction through a soil application (Bai et al.
Costs figures are not provided for any of these studies.
Interestingly, the cost of not properly maintaining or planting trees near houses and buildings also means that the energy savings that would result from a mature tree may be forgone (e.g., due to early removal); therefore, a utility company may have to install new electricity-generating infrastructure or increase capacity to cope with peak demand for electricity (rather than maintaining trees near buildings, which would offset peak demand (McPherson et al.
2006; Donovan and Butry 2009).
Trees planted and maintained on the west side of a house were found to provide annual cost savings of USD $15.50 (4% discount rate) over a 50-year period (Donovan and Butry 2009).
Pruning cycles Increasing the length of the pruning cycle, or the number of years between pruning events, is a way to reduce pruning costs up front.
In the short term, deferring the cost of pruning solves the immediate problem of a limited budget.
However, future costs will likely be greater from increased responses to citizen service requests, storm damage susceptibility, reduced condition class, tree risk from deadwood, rubbing branches leading to wounds, and more.
Structural defects (e.g., decay, poor branch attachments, deadwood, cracked branches) become more frequent as the numbers of years since last pruned increases (Miller and Sylvester 1981; Luley et al.
Reducing these factors along with structural pruning of trees from a young age are considered factors that make trees more resistant to failure during ice storms (Hauer et al.
1993, Sisinni et al.
(2002) compared service requests, priority maintenance work, and incidence of branch failures in street tree management areas that had been pruned or not pruned in the last five years.
They observed less priority maintenance work in recently pruned areas, but did not perform a complete economic analysis to compare cost savings resulting from less priority maintenance to the costs of frequent pruning (Luley et al.
The relationship between pruning frequency and tree failure may be less clear in rural areas than for street trees.
Kane (2008), however, found that campsite tree failure during a wind storm was unaffected by whether a tree had been recently pruned.
Ultimately, the length of pruning cycle impacts the condition class ratings of trees.
Miller and Sylvester (1981) developed a curvilinear model that related the condition of street trees to the number of years since last pruning in Milwaukee, Wisconsin, U.S. (Figure 6a).
The optimal pruning cycle was based on the value of the tree resource in relation to changes in pruning costs and condition class (Miller and Sylvester 1981).
Cost was generated as the reduction in tree value as condition class declined for each one-year increase in the pruning cycle length; marginal return, or marginal benefit, was generated based on the net decrease in pruning costs as the pruning cycle was increased in increments of one year (Miller and Sylvester 1981).
Comparison of savings in pruning costs versus reductions in tree population value suggested the optimal pruning cycle to be between four and five years (Figure 6b).
Download figureOpen in new tabDownload powerpoint Figure 6.
a) Relationship between pruning cycle length (number of years since last pruning) and CTLA condition class rating.
Asterisk (*) indicates regression is significant at the 0.05 level.
b) Marginal cost (loss of tree value) and marginal return (savings in pruning costs) for pruning cycle lengths.
Figure reprinted from Miller and Sylvester (1981).
Costs of not pruning The costs of not pruning trees have rarely been examined outside of the context of utility arboriculture or pruning cycles.
The only study this literature review found that explicitly examines this question is Ryder and Moore (2013, see sidebar The Costs of Not Pruning).
The Costs of Not Pruning Ryder and Moore (2013) have authored one of the few papers that explicitly examine the costs of not maintaining trees (i.e., deferring maintenance).
These authors asked: “If a tree is formatively pruned in the early stage of life, what will the cost-saving be if the same defects had not been rectified?” (p.
Seventy-eight percent of all planted trees in their sample showed structural defects that required formative pruning (Ryder and Moore 2013).
Formative pruning costs (all currency is in AUD$) averaged $2.79 per tree, while structural pruning for a mature tree averaged $44.59 (Ryder and Moore 2013).
The authors estimated that using inflation rates of 3%–5%, trees not formatively pruned today would cost $78 to $112 to structurally prune in 20 years (Ryder and Moore 2013).
Thus, the cost of not performing formative pruning on recently planted trees can be calculated as the difference between the costs of formative pruning plus normal structural pruning (~$48) and structural pruning for non-formatively pruned trees ($78–$112), or between $30 and $64.
Planting Kielbaso et al.
(1982) and Kielbaso (1990) attributed 14% of city forestry budgets expenditures to planting costs (the cost of the tree, labor, materials, water, mulch, and other things at time of planting).
Tschantz and Sacamano (1994) reported planting at 13.9%.
Time-of-planting costs can account for 80% or more of total maintenance-related costs during the life of a tree (McPherson et al.
(2002) reported results from a survey of cities in 17 European countries that revealed street tree planting and establishment costs range widely from EUR €250 to €1,875 (200–1,500 in 2002€).
McPherson (2003) reported that planting and establishment costs vary by species, and range from USD $0.01 annually per tree for hackberry (Celtis sinensis) ($0.01 annually in 1997$) to $3.16 annually per tree for ginkgo (Ginkgo biloba) ($2.18 annually in 1997$).
McPherson et al.
(1997) and others have argued that time-of-planting costs can be reduced significantly by properly matching the tree to the site, which calls to mind the urban forest management axiom: right tree, right time, right place.
Planting and establishment practices can influence subsequent maintenance needs and costs.
Harris (1985) argued that adequate root conditions for healthy establishment could make trees easier to maintain later in life.
Chapman (1981) specified that proper tree selection could reduce annual maintenance costs “by 20 to 50 percent” (p.
316), a significant potential savings where maintenance costs can range “from 20 to 50 percent of the planted price” (p.
313); however, Chapman provided no numerical data to support purported monetary savings.
McPherson (1992) stated that “funds spent initially to promote tree establishment, rapid growth and strong crown structure can reduce long-term tree care costs by prolonging the serviceable life of the tree” (McPherson 1992, p.
47); however, this article provided no long-term data to back this conclusion.
McPherson (1992) suggested a specific accounting approach for tree-planting projects, and demonstrates the utility of the approach using the city of Tucson, Arizona, U.S. The author found that costs of planting initially exceed the benefits of planted trees, but within five years of planting, benefits exceed costs at a rate of 3-to-1 or greater (McPherson 1992).
Costs of not planting The costs of not planting trees have been explicitly quantified in only a few studies.
McPherson (2001) quantified “benefits forgone” (e.g., air-conditioning savings, stormwater management) to express the difference between the current level of shading benefits provided by trees on parking lots in Sacramento, California, U.S., and the benefits to be expected if all parking lots conformed to the 50% shaded area required by ordinance.
This “benefits forgone” metric can be interpreted as the cost of not planting trees, equal to USD $1.9–3.4 million annually as calculated in this study ($1.4–2.5 million in 2000$; McPherson 2001).
However, McPherson (2001) notes that this figure is strictly benefits forgone, rather than net benefits forgone, and does not include the full costs associated with planting and maintaining the greater number of trees to provide benefits (e.g., repair to pavements due to tree damage).
Miller and Morano (1984) also provided data that enables calculating the costs of not planting trees (see sidebar The Costs of Not Planting).
Removal Tree removal is a tree maintenance activity necessitated by a variety of circumstances in urban areas: failure to establish in the landscape; old age; pest or disease attack; construction of roads or buildings; ice, wind, or other storm damage; risk that exceeds what managers are willing to accept; and more (Nowak 1990).
Tree removal is often the second-most costly expense for municipal tree program operations after pruning (Kielbaso et al.
1982; Kielbaso 1990; Tschantz and Sacamano 1994).
Kielbaso and colleagues reported that tree and stump removal accounted for 28% of the municipal tree budgets on average in 1980 (Kielbaso et al.
1982) and 1986 (Kielbaso 1990).
Tschantz and Sacamano (1994) reported an average of 20.1% of the tree care budget was allocated solely for tree and stump removal.
In a benefit-cost analysis by McPherson (2003), removal costs ranged from 26% of total tree costs for ginkgo (mostly due to high mortality rates during establishment) to 2% for Modesto ash and sweetgum trees.
The Costs of Not Planting In a 1984 article in Journal of Arboriculture, Miller and Morano presented a computerized urban forest management simulation or game designed to model changes in a street tree population over time as a result of maintenance activities.
The program, entitled URFOR/SIMULATION, used actual street tree data from a city in Wisconsin, U.S., and allowed a user to select management plans to set planting, pruning, and removal rates (Miller and Morano 1984).
The simulation ran on an annual basis for the number of years specified by the user, and the program output described the impact of management plans on the street tree population, calculated the value of the trees, and summarized management costs.
The simulation also included the ability to introduce any of six random events: wind storm, ice storm, new disease, drought, budget increases, and budget cuts.
Data from an example simulation presented in Miller and Morano (1984) illustrated the impact of planting on the net value of trees in the urban forest.
While a fully-stocked urban forest was initially the most costly management scenario, over the 40-year run of the simulation, it resulted in the greatest net benefits (see Figure 7).
The difference between the fully-stocked or repacement scenarios and the no-planting scenario can be interpreted as the costs (benefits forgone) of not planting trees.
The URFOR/SIMULATION program was a DOS-based program.
Lite v1.0 is an updated version that operated under Microsoft Windows 3.1 (Miller 1997).
The program has not been updated since 1996.
Figure Download figureOpen in new tabDownload powerpoint Figure 7.
Economics of removal decisions Two recent studies examine the economics of tree removal.
Scott and Betters (2000) presented a method for evaluating on an economic basis whether to remove and replace a tree, or retain and maintain a tree.
The authors advocated use of the individual tree appraisal methods (replacement) developed by the Council of Tree and Landscape Appraisers (CTLA) to calculate the replacement value of a single tree as a type of capital asset, taking into account species, location, and condition.
To extrapolate the benefits of a replacement tree (i.e., the value of a future tree), the authors used a discount rate of 2.5% per year.
In considering only whether to remove a tree (regardless of replacement), they proposed calculating the present net value of the existing tree as the difference between benefits now and benefits in the future, less the discounted stream of periodic maintenance costs incurred over the time period between the present and the time at which the tree would be removed.
In determining whether to remove and replace the tree, these authors added to the present net value of the existing tree the discounted “land expectation value,” or the value of a replacement tree with a given life expectancy assuming replacement recurs into the infinite future.
Scott and Betters (2000) presented an example of applying their methods to a single elm tree (Ulmus americana) on the Colorado State University campus.
Present net value of retaining the existing elm and engaging in maintenance (annual treatment) for a period of eight years was USD $95 ($70 in 2000$) (Scott and Betters 2000).
Replacing the existing tree immediately yielded present net benefits of $92 ($68 in 2000$), while retaining and maintaining the tree for eight years and then removing and replacing yields benefits of $413 ($305 in 2000$) (Scott and Betters 2000).
Thus, for this example, the greatest benefit was to retain and treat the elm tree for eight years and then replace the tree with a Dutch elm disease- (DED) resistant elm (Scott and Betters 2000).
In this example, the “cost” of removal and replacement was the lost stream of benefits resulting from premature removal of the tree.
Tinus and LaMana (2013) reframed tree removal costs by quantifying the economics of harvesting urban trees and recovering, as lumber and other wood products, the wood waste that would otherwise have been disposed of in a landfill.
Tinus and LaMana (2013) compared the value of recovered forest products and avoided landfill disposal costs to standard tree removal and disposal costs.
They found an average avoided disposal cost per job site of USD $877, compared to an average hauling cost of $842, yielding only a marginal difference of $35 to landowners (excluding additional milling costs and the value of secondary products (Tinus and LaMana 2013).
However, this analysis omitted the costs of hauling wood to a disposal site, although the cost of hauling wood to a milling site was included.
In addition to the studies cited here, several others have examined the economic costs of tree removal and replacement decisions in the context of diseased trees or those threatened by pests or disease (see section “Pest and disease management” for a more complete discussion of pest costs).
Non-economic costs of removal A non-economic (i.e., non-monetizable) cost of tree removal may be impacts on the remaining trees in the landscape.
An interesting study by Kane (2008) examined the impact of recent maintenance activities at a campsite, including pruning and removal of other trees, on the likelihood of the failure of trees at that site.
He found that removal of other trees at a campsite increased the likelihood of root-related tree failures due to increased root exposure and increased exposure to winds and decreased crown contact with neighboring trees (Kane 2008).
While this study did not explicitly examine costs, it can be inferred that an additional cost of tree removal, at a site where trees are in close proximity, increased risk of failure for the remaining trees at that site.
Unlike the tree pruning in which pruning cycles can be increased (time between pruning events lengthened) during periods of budget crisis, the removal of dead and high-risk trees should never be deferred unless property damage and personal injury can be avoided by closure of areas with high-risk trees (e.g., closing a park area to avoid human contact).
Of course, there are often costs to these alternative actions as well.
If tree removal is deferred and alternate precautionary steps are not taken, the costs can include injury liability and damages paid in court settlements (see section “Tree risk management”).
Infrastructure repair Infrastructure repair costs occur when trees interfere with other parts of the built environment in a way that damages the infrastructure, necessitating its repair.
Infrastructure damaged by trees most commonly includes curb and sidewalks (or other concrete surfaces, such as roads or parking lots), but also can include sewer lines and gutters.
Common repair activities for damage associated with trees includes removing and replacing concrete and root pruning.
A survey of 15 cities conducted between 1992 and 1994 by McPherson and Peper (1995) indicated that total concrete and sewer repair costs, for damage attributed to trees, was on average USD $7.11 per street tree annually ($4.28 in 1992$), or 25% of annual total tree program expenses.
Sidewalk and curb repair costs averaged $5.63 per tree ($3.39 in 1992$), while sewer repair costs averaged $2.76 per tree ($1.66 in 1992$) (McPherson and Peper 1995).
Many cities may require the local property owner to cover the cost of these repairs.
In a related later study, McPherson (2000) estimated that approximately $95.6 million ($70.7 million in 2000$) is spent annually in the state of California to repair damage resulting from conflicts between tree root systems and infrastructure.
(1993) found infrastructure repair activities near street trees led to 5.7% reduction in tree condition and a 4.1% increased mortality.
This resulted in a nearly USD $800,000 annual loss in urban forest value.
A program to reduce the effects of construction on street trees was developed and this reduced the impacts of construction on tree health and survival with no greater mortality and only 2.6% difference in tree condition (Koeser et al.
Infrastructure repair itself is a cost of improper tree location or species selection (i.e., neither the “right tree” nor the “right place”; Wagar and Barker 1983).
However, not repairing infrastructure damaged by trees can yield worse damage; Randrup et al.
(2001) noted that tree roots reportedly cause more than 50% of all sewer blockages.
In the case of total sewer collapse, repair costs can eclipse the costs of new construction, where the cost of proper root pruning and removal is only one-sixth of total replacement (Randrup et al.
Pest and disease management The clear management goal of maintenance practices related to pest and disease management—namely, control of the pest or disease—has yielded well-documented economics of pest/disease management.
Additionally, there is a clear counterfactual case for many types of pests/diseases; if lack of pest management actions results in pest infestation and eventually tree mortality, the cost of management actions can be directly compared to the value of trees lost (e.g., VanNatta et al.
The beginnings of pest economics: Dutch elm disease Several models exist to examine the costs and benefits of different pest management scenarios.
The economics of controlling Dutch elm disease (Ophiostoma novo-ulmi) was examined by many authors between the 1960s to mid-1980s.
An early example of a paper on the economics of pest management is a 1976 U.S. Forest Service report on the economics of Dutch elm disease control (Cannon and Worley 1976).
Cannon and Worley (1976) observed tree sanitation approaches to project tree mortality rates for “Best,” “Fair,” and “Poor” pest control scenarios.
They found removing diseased elms promptly through sanitation was the most cost-effective approach.
Intensive sanitation (three annual inspections) was 25% less costly than conventional sanitation (one annual inspection) with prevention of tree mortality and associated tree removal costs.
Himelick and Ceplacha (1976) reported the costs of treating trees infected with DED by pruning compared to the costs of removal and replacement: when less than 5% of the crown is showing DED symptoms, USD $1,216 ($297 in 1976$) can be saved by pruning ($233; $57 per tree in 1976$) instead of removing ($1,499; $354 in 1976$) DED-infected trees.
Kostichka and Cannon (1981) analyzed the costs of DED management for cities in Wisconsin, U.S., and attributed 79% of all costs to tree removal and disposal, 14% of costs to treatment (11% to fungicide injection and 3% to root-graft barriers), and 7% to inspection activities.
Sherwood and Betters (1981) performed a benefit-cost analysis of DED control scenarios with the goal of determining which scenario yields the highest return on investment (highest benefit-cost ratio).
They found that an “intensive consistent sanitation” management scenario consisting of two inspections per year, prompt removal of infected trees, and deadwood pruning of all trees yielded the highest benefit-cost ratio of the examined alternatives (Sherwood and Betters 1981).
These authors also provided a step-by-step method for assessing the benefits and costs of alternative DED management programs for a municipality considering undertaking DED control (Sherwood and Betters 1981).
Other authors over the years have examined the biological costs (e.g., mortality of trees, development of fungicide-resistant DED strains) of DED control and treatment efforts without matching economic data to treatment options (Wilson 1976; Campana 1977; Gregory and Allison 1979; Sherald and Gregory 1980).
Economics of other pests Studies examining the economics of pest management include Dreistadt and Dehlsten (1986; costs of aphid honeydew pest management), Jetter et al.
(1997; costs of ash whitefly biological control), Kovacs et al.
[2010; economic damage potential of the emerald ash borer (EAB), Agrilus planipennis], and VanNatta et al.
(2012; cost of EAB management).
Dreistadt and Dahlsten (1986) described a study undertaken to determine the costs of aphid honeydew pest management for tuliptrees (Liriodendron tulipifera) compared to removal and replacement of diseased trees.
Costs of pest management were estimated as direct costs by city arborists and parks supervisors and included structural and clearance trimming, removal and replacement of 1% of trees each year, and sidewalk repair and modifications necessitated by tuliptree trunk growth (Dreistadt and Dahlsten 1986).
Removal and replacement of 400 tuliptrees with London plane-trees (Platanus acerifolia) was only 63% of the cost of continued maintenance of the tuilptrees (USD $223,000 compared to $354,000 in 1984$; Dreistadt and Dahlsten 1986).
Costs excluded from this analysis include potential liability costs, temporarily lost aesthetic value, and other tree benefits.
(1997) performed a benefit-cost analysis of the use of a parasitic wasp (Encarsia inaron) to biologically control the ash whitefly (Siphoninus phillyreae), which attacks ash (Fraxinus spp.) and ornamental pear (Pyrus spp.) trees.
They compared the change in appraised value due to pest damage (benefits) to the costs incurred by the entities conducting the biological control (including personnel, travel expenses, and materials; Jetter et al.
Given total program costs of only USD $2.0 million ($1.2 million in 1992$), total net benefits of the program were almost $536 million wholesale ($323 million in 1992$) and $682 million retail ($411 million in 1992$) for street trees only (Jetter et al.
In other words, if biological control efforts had not occurred, over a half billion dollars in street tree appraisal value would have been lost.
Current pest threat: Emerald ash borer Kovacs et al.
(2010) examined the costs that will be incurred for municipalities as a result of emerald ash borer damage in municipalities in a 25-state region centered on Detroit, Michigan, U.S. (the epicenter of North America’s EAB infestation), between 2009 and 2019.
Using simulations of the spread of EAB and costs of various treatment options or removal and replacement for trees of different sizes, the authors estimated the costs of EAB management (Kovacs et al.
The analysis assumed that homeowners and tree managers act optimally and “[maximize] the present value of a stream of benefits and costs associated with each tree by choosing among four actions—1) do nothing, 2) remove, 3) remove and replace, or 4) treat with an insecticide that prevents injury from EAB” (Kovacs et al.
They concluded that EAB will cost U.S. communities an estimated $11.4 billion ($10.7 billion in 2010$) in discounted terms between 2009 and 2019 (Kovacs et al.
Note that the Kovacs et al.
(2010) scenario was an optimal one, assuming completely rational actors acting optimally in the face of EAB infestation, and does not allow for calculation of the costs of doing nothing.
(2012) provided more detailed EAB management scenarios based on the projected management costs and tree value.
They simulated the costs of four management scenarios for the ash tree population on the University of Wisconsin–Stevens Point campus: 1) doing nothing and removing ash trees as they die; 2) immediately removing all ash trees over a five-year period; 3) immediately removing and replacing ash trees with non-ash trees; and 4) minimizing mortality by treating all ash trees with approved insecticide treatments (VanNatta et al.
The costs of doing nothing to combat EAB (scenario 1) yielded an annual present value of benefits nearly equal to the costs of removing ash trees as they die (benefit-cost ratio of 1.02).
However, the net value of remaining trees after a 20-year period in the do-nothing scenario ranged from USD $868 (using i-Tree Streets to value the benefits of trees) to $44,913 (using CTLA appraisal methods to assess tree values; VanNatta et al.
This was compared to the best-case scenario (based on CTLA appraisal values) of treating all trees (scenario 4; yielding $84,610 net value remaining after 20 years; VanNatta et al.
The economic analyses of EAB detailed here have yielded tools available for managers facing decisions about managing EAB.
These tools include the EAB Calculator (Sadof et al.
2011; Purdue 2015) and the EAB PLANning Simulator (VanNatta et al.
2012; UWSP 2015), both of which allow urban forest managers to calculate costs of different control methods for emerald ash borer.
Integrated pest management Integrated pest management (IPM) and monitoring of pest and disease populations rose in prominence for urban areas in the late-1970s as a means of reducing the risk of economically damaging pest outbreaks in urban areas and the costs of controlling outbreaks.
IPM methods are not unique to urban forestry and arboriculture but originated in the field of agriculture to monitor and manage crop pests.
In 1978, Olkowski and Olkowski introduced the idea of an urban IPM to arborists as a means of more effectively dealing with the diversity of vegetation pests found in cities and to enable cost-effective dissemination of practices to homeowners.
These authors introduced the concept of injury level, or the level of pest infestation (in number of insects per unit of vegetation; e.g., leaf area) at which damage to the tree is unacceptable and treatment of the pest becomes desirable (Olkowski and Olkowski 1978).
Establishing injury levels for urban pests and trees helps minimize application of pesticides (i.e., costs of pesticide use) and make effective use of limited resources for treating pests in the urban forest (Olkowski and Olkowski 1978).
Ball and Marsan (1991) advocated for the establishment of an action threshold, as the level of pest infestation or incidence just below the injury level at which economic or aesthetic thresholds are reached, and at which treatment should begin.
In economic terms, the economic injury level occurs at the point at which the marginal benefits obtained when trees are treated for a pest (i.e., the increased benefits due to prolonged tree lifespan) equal the marginal costs of the treatment (i.e., the dollars and time spent treating trees).
An aesthetic action threshold is a management approach with treatment meant to avoid surpassing an unacceptable injury level, which is a point that vitality is reduced detrimentally.
Subsequent authors have encouraged proactive monitoring (including visual inspection of trees for damage and pest incidence, locating vulnerable populations of trees, trapping and baiting of pests, and monitoring of environmental conditions suitable for specific pests or for pest outbreaks; Raupp 1985; Ball 1987), preventative maintenance (to promote tree health; Nielsen 1986), and minimizing periods of tree stress to reduce susceptibility to pest or disease infestation (Moorman 1985).
(1987) provided a description of implementing an IPM program to control gypsy moth infestation (although results of the program are not provided).
However, beyond statements asserting that IPM and monitoring practices are economical, no authors advocating IPM provide explicit information about its costs or compare costs to traditional management of pest populations with pesticides.
Maintenance Not Commonly Quantified in Municipal Budgets Some types of tree maintenance are much less completely quantified and studied.
The costs associated with risk management, watering, mulching, soil and nutrient management, staking, tree support systems (e.g., cabling, bracing, and propping), and protection during construction are less explicit in literature from the field of arboriculture and urban forestry.
These tend to be tasks that do not earn line items in city budgets, and so do not appear as clearly quantified in records.
These types of maintenance may occur less systematically across a population of trees in the urban forest, and may be more likely borne by a nonprofit organization, neighborhood, or citizen in charge of tree care.
Tree risk management One of these less-studied costs of not maintaining trees is related to tree risk and liability management.
If a lack of maintenance results in a tree that fails and injures person or property, damages may be awarded to the injured party, payable by the individual liable for the tree (Ryan 1985; Anderson and Eaton 1986; Merullo and Valentine 1992).
Systematic inspection of trees for tree risks and documenting inspection efforts can help minimize the potential for liability suits that may happen due to tree-related damage, injury, or casualty (Anderson and Eaton 1986; Sharon 1987; Sreetheran et al.
The risks of harm posed by an assessed tree can be compared to the costs and benefits of removal or other risk-mitigating actions (Ryan 1985; Stewart et al.
Additionally, preemptively adopting practices to promote urban tree and forest health—including best management planting practices and regular maintenance, maintaining a mixture of age classes and species, and promptly removing declining trees—can also help minimize potential costs incurred due to tree failure (Anderson and Eaton 1986).
Several authors have discussed proper management of individual mature trees at risk of decline (Shigo 1975; Shigo 1982; Clark and Matheny 1991), or groups of mature trees in forest settings (Bakken 1995).
Yamamoto (1985) argued that programmed tree maintenance (whereby tree pruning is performed for a certain geography within the city every year) is defensible in negligence and liability claims of personal injury or property damage caused by street trees.
Insuring against these risks can also help minimize liability-related tree costs (Carpenter 1987).
Storm events are one particular source of concern in assessing risk in the urban forest; although a few authors surveyed damage caused to urban trees by storms (Gibbs and Greig 1990; Gibbs and Palmer 1994; Escobedo et al.
2009; Hauer et al.
(2009) and Hauer et al.
(2011) provided cost estimates for debris clean-up from storm damage.
An understanding is needed on how and if early maintenance leads to a costs savings from tree damage resulting from storms.
Watering Watering and irrigation of trees accounted for approximately 4.0% of municipal tree expenses (Kielbaso 1990).
Watering is widely acknowledged to be crucial to planted tree establishment and survival.
The biological costs of not watering are clear: trees that receive inadequate water exhibit decreased condition, and if moisture levels are low for a sufficiently lengthy period of time the tree may even die (Kozlowski and Pallardy 1997).
Many authors have examined the importance of watering for urban trees (e.g., Pellet et el.
1980; Kramer 1987; Costello et al.
2005; Costello 2013; Symes and Connellan 2013); however, few have examined the economics of watering.
Costs of not watering If watering leads to greater tree survival, there is a clear cost to not watering.
If the cost is less than the benefit, then the net benefit value added resulting from irrigation could then be calculated as the lifetime benefits produced by the additional trees that survive as a result of irrigation.
For instance, if irrigation results in 15 of 20 planted trees surviving over the 10 of 20 trees that survive without irrigation, the lifetime benefits of these five additional trees is the value added by irrigation.
The net benefit of irrigation is the total added benefits less the cost of irrigation.
Conversely, if forgoing irrigation results in a loss of five trees that otherwise would have survived, the costs of not irrigating are equal to the benefits forgone less the avoided costs of irrigation.
Gilman (2001) authored one of the few studies that collected data that enables measurement of the costs of not watering trees in terms of cost per live, established tree (see sidebar The Costs of Not Watering).
Outside of this study, to the knowledge of the authors, there are no other complete studies on the economic costs of not watering trees.
Mulching Mulching is a type of tree maintenance frequently employed at the time of planting.
Mulching decreases tree root competition with turf grass (Samyn and de Vos 2002), weeds or other vegetation (Watson 1988; Green and Watson 1989), can improve soil moisture content (Watson 1988), and may protect a tree from damage by lawnmowers or weed trimmers.
Mulching improves the health of a tree, increasing both above- and belowground growth, and trees mulched during establishment may require less maintenance later in life (Green and Watson 1989).
However, few articles have empirically demonstrated the long-term benefits of mulching trees.
Most studies have been conducted during the course of a single (e.g., Gilman and Grabosky 2004) or few growing seasons (e.g., Green and Watson 1989).
Furthermore, no studies have reported on the costs of mulching.
Municipal budgets almost never include mulching as a specific line item.
The Costs of Not Watering Gilman (2001) examined the impacts of watering throughout the first six months (the whole summer) after transplanting, compared to only watering for five weeks (no summer irrigation).
For four of six packaging and transplanting treatments, higher mortality rates of trees not irrigated following transplanting led to a greater cost due to replacing dead trees and thus a higher cost per-live tree (Table 1, based on data from Gilman 2001).
In only one case (root pruned ball-and-burlap trees) was there not a financial advantage of water.
However, in all cases the watered trees grew more.
Unfortunately, the research conducted by Gilman (2001) was one of the few papers to provide data that afford calculation of the cost per live tree of maintenance practices related to establishment.
View inlineView popup Table 2.
Cost savings (in 2013$) resulting from watering during establishment for six different planting packaging types.
(Based on data presented by Gilman 2001.
Original costs in Gilman (2001), from which these values were calculated, were assumed to be published in 2000$.] All currency is in USD$.
Soil and nutrient management Soils in urban environments may lack adequate nutrients for trees to grow (Scharenbroch and Catania 2012).
Fertilizing trees—either at the time of planting or later in their life—can help correct damage or poor conditions resulting from improper nutrient management (both deficiencies and excesses; e.g., Himelick and Himelick 1980; Smith 1988).
Fertilization to correct deficiencies and promote growth could also theoretically increase the number of established trees in the urban forest to a rate at which they reach an “environmentally functional size” and provide benefits (Harris et al.
If nutrient management would lead to survival or improved condition of the trees managed, the benefits forgone due to lack of nutrients that support reaching these objectives are the “costs” of this decision.
Examples to illustrate this have been documented by examining tree decline.
One particular type of nutrient management—nitrogen fertilization—has been examined by a few studies.
Nitrogen fertilization in general promotes tree growth (Scharenbroch and Lloyd 2004).
In an early example, Neely (1984) conducted a controlled experiment that found that application of nitrogen fertilizer (both in isolation or in combination with glyphosate herbicide) increased tree growth rate of black walnut (Juglans nigra), sycamore (Platanus occidentalis), Norway maple, and honeylocust, relative to untreated control trees.
However, Harris et al.
(2008) compiled five studies that tested the effects of several nitrogen fertilization rates on 10 tree species in both field- and container-growth settings, and found no impact of nitrogen fertilization on tree growth or establishment.
Gilman (2004) tested six types of soil backfill amendments but also found no benefits to growth or survival of any of these treatments during the first four months after transplanting.
Early maple decline studies Maple decline and methods of treatment was studied by several authors in the late 1970s and early 1980s.
Maple decline was assumed to be a result of multiple stress factors, such as manganese deficiency (Smith and Mitchell 1977; Funk and Peterson 1980) or excessive exposure to road salts (Rich and Walton 1979; Funk and Peterson 1980).
Rubens (1978) outlined four direct costs of maple decline: “1) periodic deadwood removal, 2) eventual removal cost, 3) replanting or replacement cost, and 4) loss in value of the mature tree” (p.
Rubens (1978) declared that, “The cost of soil desalination on a continuous basis to protect healthy sugar maples (Acer saccharum) not affected by other environmental or man-made stresses is less than the costs attributable to non-provision of this maintenance” (p.
41), although specific costs were not determined empirically.
Other authors have noted additional methods of mitigating maple decline without providing dollar figures, including application of manganese compounds directly to the trunk or foliage (Smith and Mitchell 1977), and soil injection or dry application of manganese sulfate monohydrate (Funk and Peterson 1980); applications of nitrogen were ineffective (Rich and Walton 1979).
Fixing chlorosis Himelick and Himelick (1980) analyzed methods of ameliorating chlorosis in several species via iron treatments, noting that excessive application of calcium or phosphorous in turf fertilizers or too much soil moisture could contribute to chlorosis.
These authors observed that injecting the tree with ferric citrate or ferric ammonium citrate is a “reasonably effective and economical” method of treating chlorosis in pin oak (Quercus palustris) and sweetgum trees (Liquidambar styraciflua) (Himelick and Himelick 1980), although again no costs figures were provided.
Smith (1988) also discussed methods for ameliorating nutrient-deficiency-related leaf chlorosis, but did not link chlorosis to tree performance, benefits, or other maintenance needs outside of the chlorosis treatment itself.
Costs of not managing soils or nutrients None of the aforementioned studies provided empirical estimates of the costs of nutrient treatments.
Additionally, few studies have quantified the impacts of nutrient treatments on tree structure (e.g., survival or growth), function, or benefits.
Studies that did provide estimates of the impact of treatments on tree survival (Gilman 2004; Rich and Walton 1979) and growth (Harris et al.
2008) found no effect of fertilization, or a small impact on root growth (Percival et al.
Tree support systems Several tree support systems, including staking, cabling, bracing, and propping serve the purpose of supporting a tree and improving strength during periods of vulnerability.
Staking serves to support small or recently planted trees or trees in windy areas (Smiley and Lily 2006).
Bracing, cabling, and propping serve as methods of supporting weakened, old, or severely damaged trees that would otherwise fail, thereby prolonging their useful life.
Relatively few studies have discussed the economic benefits of staking trees.
Black (1978) discussed staking young trees as a means of reducing vandalism.
Bracing and cabling as methods of supporting mature trees were discussed by Mayne (1975) and others, but the current literature review yielded no articles on the economics—benefits or costs—of cabling and bracing.
Protection during construction Protecting trees during construction is a means of preserving many of the benefits provided by trees that otherwise might be damaged or removed during construction of a building or road.
Protection activities theoretically have costs.
(2013) found that trees near road construction activities were twice as likely to succumb to mortality as trees not adjacent to road construction.
Tree protection during building construction can include establishing a barrier between the tree and construction activities, creating “disturbance-free zones” around wooded areas to limit root disturbance, and grading construction areas to guide potentially contaminated construction runoff away from root zones (Anderson and Barrows-Broaddus 1989).
Tree protection during road construction or utility installation can include tunneling and boring with an aim to avoid root damage (Yingling et al.
1979; Jim 2003).
Tree protection and preservation during construction is a specialized field composed of consulting arborists and contractors who rarely publish, and thus few studies explicitly examining the economics of tree protection exist.
Economics of tree protection The loss of forest benefits due to inadequate protection of existing trees or forests from damage during construction or other activities results in a number of types of costs: costs to the final homeowner, who might otherwise benefit from preserved trees, costs to the contractor or developer who pays to remove trees, and, where preserved trees would have increased final sale price, lost revenue for the developer or homebuilder (Anderson and Barrows-Broaddus 1989).
Additional costs not mentioned in the tree protection literature include: decreased home equity, loss of additional tax revenues that would have accrued due to increased property values of lots with mature trees, and costs to homeowners to remove trees not sufficiently protected.
A survey of residential homebuilders in Amherst, Massachusetts, and Athens, Georgia, U.S., revealed that the costs of removing trees on a heavily wooded lot during development averaged USD $3,844 ($1,000 in 1977$) in Amherst but only $707 ($250 in 1980$) in Athens (Siela and Anderson 1982).
Costs of preserving trees on lots averaged $6,535 ($1700 in 1977$) in Amherst and only $792 ($280 in 1980$) in Athens (Seila and Anderson 1982).
The authors reported that in both Amherst and Athens, builders recovered the higher cost of preservation in an increased final home price (Seila and Anderson 1982), although real estate data were not provided.
Tree protection efforts can also take the form of establishing boundaries around wooded areas near residential yards to protect them from substantial human intrusion in the form of yard extension, waste disposal, forest clearing activities, or more (McWilliam et al.
McWilliam et al.
(2010) estimated that approximately 20%–50% of the first 20 m of the edges of municipal forests in Ontario, Canada, were disturbed due to human encroachment.
Although encroachment could yield a significant loss in benefits provided by these forests, McWilliam et al.
(2010) did not provide data about magnitude of lost benefits, nor the costs of enforcement that could curb encroachment activities.
Other types of care and maintenance The costs of other types of tree care are even less certain than the types of maintenance costs previously examined: nursery management (Tate 1984a); use of growth control chemicals (Carvell 1975; Olenick 1977; Domir 1978; Domir and Roberts 1983; Holewinski and Johnson 1983); topping (Carvell 1978; Karlovich et al.
2000); root pruning (Gilman 1990; Achinelli et al.
1997); applying herbicides to control weeds (Smith 1975); general grass and turf management (Dawson et al.
2001); tree site (Berrang et al.
1985) or species (Miller and Miller 1991) selection; wrapping trees (intended to prevent frost crack, Hart and Dennis 1978; Hvass 1985); compaction and other soil remediation efforts (Day et al.
1995); managing woodlots or patches of forest in urban areas (e.g., Tyrvainen et al.
2003); and inventorying or monitoring trees to determine maintenance needs (e.g., Tate 1985; Sreetheran et al.
This literature review did not find literature on the costs of not performing these types of maintenance.
Tree Appraisal and Valuation Tree appraisal and valuation efforts are not a type of maintenance per se (although the de facto monitoring of trees that occurs during on-site appraisal is certainly connected to tree maintenance efforts in the most holistic of tree management situations).
However, tree appraisal and valuation is intimately connected to assessing the costs of maintenance and the value lost or benefits forgone due to inadequate maintenance of trees.
If a lack of adequate maintenance results in the complete loss of the tree, appraisal value is one measure of the cost of not maintaining the tree.
Many authors have examined tree appraisal and valuation, or methods of attributing value to a landscape tree.
Methods include expert appraisal value (e.g., Mayne 1978; Chadwick 1980; Watson 2002; Ponce-Donoso et al.
2009), replacement cost (cost of replacing the tree with one of similar size and species, e.g., Felix 1978; Mayne 1978), amenity value (property value change due to addition or removal of the tree, e.g., Mayne 1978; Morales et al.
1983; Tyrvainen 1997; Ishikawa and Fukushige 2012), current value (value of the benefits produced annually, e.g., Brown and Boogaerdt 2006), stated preference approach (willingness-to-pay for a preserved tree, e.g., Notaro and De Salvo 2010), and various accounting methods (that take into account discounting streams of benefits to their present value, e.g., McPherson 1992; Brown and Boogaerdt 2006; Peterson and Straka 2011), among other methods.
Different methods of appraisal can attribute dramatically different values to the same trees (Watson 2002; Price 2003; Ponce-Donoso et al.
2009), and all methods have at least some limitations (Price 2003).
Incorporation of maintenance into tree appraisal Most common methods of appraisal do not take into account the explicit value of maintained compared to unmaintained trees, or the direct value of maintenance performed on trees, although Felix (1978) mentioned that a lack of maintenance can affect appraisal value.
Condition and location—factors that may be correlated with past maintenance activities or current maintenance needs—are frequently included in appraisal values (Davis 1983).
A few appraisal methods include maintenance costs.
For example, the Standard Tree Evaluation Method used in New Zealand includes estimation of maintenance costs at 14% of the retail tree and planting costs (Watson 2002).
The CTLA Guide for Plant Appraisal Cost-of-Cure Method also includes long-term maintenance costs.
The capital gains method also includes maintenance costs; this method combines the cost of planting a replacement tree, the interest accrued on capital investments equivalent to the price of the tree during the time period in which it takes the replacement to grow to the size of the original tree, and the costs of maintenance over this time period into a more accurate assessment of the value of a tree (Mayne 1978).
Ponce-Donoso et al.
(2009) reviewed seven methods used by individual Chilean municipalities.
They found three methods that explicitly incorporate the value of annual maintenance performed on the tree, quantified as average municipal maintenance cost per tree for all trees maintained in a given year (although the authors note that this places a higher value on trees maintained by inefficient or more expensive maintenance practices; Ponce-Donoso et al.
Notaro and De Salvo (2010) conducted a contingent valuation analysis to uncover people’s willingness to pay for efforts to preserve and protect cypress (Cupressus sempervirens L.) trees from a threatening disease in the landscape of northern Italy.
They discovered that together, people would be willing to pay between EUR €122–€141 million over a 100-year tree life span (discounted to present value at 2%) for research and treatment efforts; unfortunately, the article presumed “economic viability of caring for the cypresses in order to maintain the current landscape” (Notaro and De Salvo 2010, p.
80), but did not present actual costs of disease control that could be compared to the willingness-to-pay values to determine the costs of not controlling the cypress canker.
Introduction Forest fires are an integral part of many terrestrial ecosystems such as boreal forests, temperate forests, Mediterranean ecosystems, savannas and grasslands, among others.
Fires in the Mediterranean basin account for a significant percentage of total fires occurring worldwide [14].
Forest fire prediction, prevention and management measures have become increasingly important.
Systems for forest fire-danger prediction represent an essential tool to predict forest fire risks, back up the forest fire monitoring and extinction phase, and to assist in the fire control planning and resource allocation [1].
At present many fire risk models make use of forest fire databases to construct and assess probabilistic models.
Brillinger et al.
proposed a model for each specific location based on its fire history, its elevation above sea level and the corresponding dates of fire days and non-fire days [3].
The system tries to fit different probabilistic models to data from different locations.
When the fitting is accomplished the system is used to estimate the probability of a forest fire taking place at a particular location and time.
No weather parameters are used and the main output is the probability of the number of fires being greater than a certain threshold.
This probability estimation is helpful for fire fighters' resources allocation.
Experiments show that the assessed risk is accurate for a specific area.
A shortcoming of this model is its close dependency on the trained area and its inability to generalize the model to nearby areas.
implemented a GIS-based forest fire risk model, to study the relationship between vegetation, climate, topography and their associated factor to causing forest-fires [11].
A forest fire risk zone map was constructed using a four-category risk scale.
The risk range is from very high to low.
The resulting map was found to have a strong correlation with the highly affected fire sites.
This method is also dependent on the studied area and the model cannot be generalized to other lands.
It is also notable that the use of satellite images and GIS is imperative in the construction of the models.
Estimation of forest fire risk on a global scale was introduced by Iliadis who developed a decision support system (FFIR-EDESSYS) that implements fuzzy logic and fuzzy algebra concepts [10].
The system was implemented in Greece, and it showed a good estimation of the forest fire risk areas but it has no indication of the estimated area of the fire which might compromise the resource allocation problem.
Some important clustering techniques using partitioning methods like k-means or density based clustering like DBSCAN that are normally used on spatial data, can be extended to spatiotemporal data.
Many models implement Spatio-temporal Data Mining (STDM) techniques, and demonstrate that these techniques have great potential in forest fire prediction.
Their application to forest fire is described by cheng et al.
as follows [4]:  Forecasting and trend analysis: basically one can make use of historical data related to burnt area to predict future forest fires.
These methods can also provide the ability to forecast the burnt area and the length of fire field.
Association rule mining for prediction of ongoing forest fire development: This is based on spatial forest data like the slopes or position of the slope as well as weather data (precipitation, wind speed and direction, temperature) and fuel type, to predict the spreading of the fire.
It will add the ability to create logical conditions such as: if a fire occurs in W then it is very likely to spread towards S and allows forest fire fighters to obtain an optimal plan.
Pattern Detection for sequence of fire events: using spatio-temporal data to discover sequential patterns that occur frequently, and hence having the ability to generate logical rules.
Cluster analysis and identification of fire spots: Spatiotemporal clustering may discover the cells (hot spots) that have a high probability of starting a fire.
The discrimination of fire spots will have a direct implication on the probability of forest fires.
developed a system for automatic identification of fire smoke using artificial neural networks applied to advanced very high resolution radiometer imagery [13], while Wiering and Dorgio were interested in knowing where to cut fire-lines to minimize the damage done by the forest fire [19].
The idea was to build a fire spread simulator and to search for good decision policies.
The parameters used to build the spread index are the fuel-type and the wind speed.
The system was achieved using evolving neural networks.
Naturally this system has to be calibrated on every type of terrain and helps in making policies for fire fighters.
used predictive geospatial data mining methods and constructed mathematical models to predict the forest fire hazardous areas, based on the FHR (Forest Fire Hazard Rate) and a PRC (Prediction Rate Curve) [9].
Furthermore, new techniques have emerged like cellular automata or agent-based modeling.
In the cellular automata models, a forest is considered to be a cellular space that evolves with time.
Each cell has an independent and a dependent state.
The independent state is its own evolution with time, while the dependent one is the influence of neighboring cells.
A burning cell is considered to be able to conduct fire to neighboring unburned cells, which will be useful to model fire propagation process between cells [16].
Cellular automata were applied by Clarke et al.
who made use of fractal geometry to predict wildfire propagation and extinction [6].
While Muzy et al.
implemented fire spread prediction using cellular automation model (Cell-DEVS)[15] and they combined it with a physical model of fire spread proposed by Rothermel [17].
A new technique was introduced by Dunn and Milne to overcome the problem of terrains of heterogeneous structure [8].
In the old techniques such terrains must be split into sub terrains and each one has to be modeled by itself.
This method encodes the spread of wild land fire in a set of interacting automata.
The system was able to simulate the fire spread on an irregular field.
Cheng and Wang made use of spatiotemporal data mining techniques and the model was focused on predicting the burnt area [5].
Their model uses recurrent neural network to combine historical fire data of the studied landscape as well as weather data.
The model was validated on Canadian soil and it achieved errors as low as 0.5ha for an area of 200ha.
Another relatively recent approach used data mining and meteorological data to predict forest fires and to estimate the burnt area corresponding to that fire [7].
They tried out several inputs in the aim of finding the best parameters that can be used for prediction.
As a result of this they found out that the useful parameters were: wind speed, temperature, humidity and precipitation.
They used 5 different data mining algorithms: multiple regression (MR), Decision Tree, Random Forest, Neural Networks and Support Vector Machines.
The best results were achieved using support vector machines and a Gaussian kernel function.
The overall performance was measured using two techniques: the Mean Absolute Deviation and the Root Mean Square Error.
The SVM implementation gave a MAD of 12.71ha and a root mean square error of 64.7ha.
Overall the challenge for a prediction system is how to combine the different indicators in order to make a decision and how to predict a large number of unseen patterns from a few known ones.
The prediction has to be accurate, consistent and computationally effective.
This paper deals with the prediction problem, it presents an algorithm for fire risk classification over four classes based on the historical number of fires and certain weather conditions.
This algorithm is based on support vector machines which is presented in the next section.
SECTION II.Proposed prediction algorithm and architecture The proposed method introduces a fire risk index on a scale of 1 to 4, where 1 corresponds to the lowest fire risk and 4 to the highest fire risk.
This index corresponds to the potential number of fires that could occur on a specific day and hence can be used to estimate the actual number of fires on that day.
In order to perform prediction, it is required to specify the parameters or features monitored during the day that are used in the prediction algorithm.
Feature selection Any prediction mechanism bases its prediction on a continuous observation of a number of specific features.
In this paper the aim is to reduce the number of monitored features, and to eliminate the need for weather prediction mechanisms.
The reason is to reduce the potential sources of error.
If weather prediction is not accurate then it becomes a source of erroneous data, and based on the data mining principle of “junk in, junk out”, it will lead to erroneous prediction even if the prediction algorithm was optimal.
Another challenge is to choose easily measurable features in the aim of reducing the cost of the system.
At the same time, the chosen features must have a high correlation with the risk of fire occurrence: The feature selected are the following:  The minimal temperature of the day, Tmin.
The maximal temperature of the day, Tmax.
The average humidity of the day.
The solar radiation over the day.
The average wind speed over the day.
The cumulative precipitation level: taken as precipitation year-to-date starting from October 1.
It is worth noting that this value is constant for all points of a certain year considered since the algorithm is applied only for the Lebanese fire season months of June, July, August, September and October, where typically no precipitation occurs.
The strategy used to eliminate weather prediction is discussed in section III.
In order to fuse the above features and to make fire predictions Support Vector Machines (SVM) are used.
The mechanism is introduced in the next section.
Support vector machines In the simplest form, SVM uses a linear hyperplane to create a classifier with a maximal margin [12].
In other cases, where the data is not linearly separable, the SVM maps the data into a higher dimensional space called the feature space.
This task could be achieved using various nonlinear mappings: polynomial, sigmoid and RBF such as gaussian RBF.
After the nonlinear transformation, SVM finds a linear separating hyperplane in this new feature space.
Not like other techniques, probability model and probability density functions need not be known before building the machine.
This is very important for generalization purposes, as in practical situations, there is not enough information about the underlying probability laws and distributions.
Since SVM has been recording high accuracies in many fields, and since it has an excellent generalization ability, it is used in the course of this paper.
What follows is an introduction to the theory of SVM and the general equation of the hyperplane that will separate the two classes.
In the case of linearly separable data the approach is to find among all the separating hyperplanes the one that maximizes the margin.
Any other hyperplane will have a greater expected risk than this hyperplane.
During the learning stage the machine uses the training data to find the parameters w=[w1w2…wn]T and b of a decision function d(x,w,b) given by: d(x,w,b)=wTx+b=∑i=1nwixi+b(1) View SourceRight-click on figure for MathML and additional features.
The separating hyperplane follows the equation d(x,w,b)=0.
In the testing phase, an unseen vector x, will produce an output y according to the following indicator function: y=sign(d(x,w,b))(2) View SourceRight-click on figure for MathML and additional features.
In other words, the decision rule is: if d(x,w,b)>0 then x belongs to class 1 and if d(x,w,b)<0 then x belongs to class 2.
The weight vector and the bias are obtained by minimizing the following equation: Ld(α)=0.5αTHα−fTα(3) View SourceRight-click on figure for MathML and additional features.subject to the following constraints: yTα=0;  α≥0 View SourceRight-click on figure for MathML and additional features.Where H denotes the Hessian matrix given by: H=yiyj(xixj) and f is the unit vector f=[1,1…1]T.
Having the solutions α0i of the dual optimization problem will be sufficient to determine the weight vector and the bias using the following equations: w=∑i=1lα0iyixi(4) View SourceRight-click on figure for MathML and additional features.
b=1N∑i=1N(1yi−xTiw)(5) View SourceRight-click on figure for MathML and additional features.where N represents the number of support vectors.
The linear classifier presented above has limited capabilities since it is only used with linearly separable data while in most practical applications data is random and is not linearly separable.
The nonlinear data has to be mapped to a new feature space of higher dimension using a suitable mapping function Φ(x) which is of very high dimension, potentially infinite.
Fortunately, in all the equations, this function appears only in the form of a dot product.
From the theory of reproducing kernel Hilbert spaces [2], which is beyond the scope of this paper, a kernel function is defined as: K(xi,xj)=Φ(xi)TΦ(xj).(6) View SourceRight-click on figure for MathML and additional features.
Equation (3) has this form in the feature space: Ld(α)=∑i=1lαi−12∑i,j=1lyiyjαiαjK(xi,xj)(7) View SourceRight-click on figure for MathML and additional features.
subject to αi≥0,∑i=1lαiyi=0.
View SourceRight-click on figure for MathML and additional features.
The decision hyper surface in equation (1) is given in the nonlinear space by the following equation: d(x)=∑i=1lyiαiK(xi,x)(8) View SourceRight-click on figure for MathML and additional features.
The solution of equation (7) yields the hard margin classifier.
In general, it is useful to use a soft margin classifier to preserve the smoothness of the hyperplane and prevent αi from tending to infinity.
This classifier is obtained using the same minimization process by just adding one more constraint to equation (7).
The constraint is: 0≤αi≤C, where C is defined by the user.
If C tends to infinity, the soft margin classifier tends towards the hard margin.
Detection architecture The above method has the ability to classify 2 classes and hence it is necessary to introduce an architecture that allows the classification of more than 2 classes.
The proposed architecture shown in figure 1 is well know for 4 classes classification [12], [18].
The training and optimization of this architecture is described below.
In training SVM 1, points of scale 1 and 2 are put together to form class (−1) while points of scale 3 and 4 are put together to form class (+1).
SVM 2 is trained by scale 1 as class (−1) and scale 2 as class (+1).
SVM 3 is trained by scale 3 as class (−1) and scale 4 as class (+1).
Hence a point that gets classified by SVM 1 as (−1) is passed to SVM 2, which will output its corresponding scale.
While a point classified as (+1) by SVM 1 is passed to SVM 3, which will output its final scale.
Table I shows the output scale based on the decision of each SVM.
As described in section III, each month has its own risk scale definition.
For example a day in September where 15 fires have occurred is considered to be a day of scale 3 while 15 fires for June or July is considered a day of scale 4.
As a result of this discrepancy, each month has its own architecture trained by training points taken only from that month.
- Four classes prediction architecture.
Four classes prediction architecture.
Show All  SECTION III.Experiment and Results The weather data provided by the Lebanese Agricultural Research Institute (LARI) covers the Lebanese territory and spans the nine years between 2000 and 2008.
The data is collected using fixed weather stations across the country.
The weather parameters provided are the daily minimum temperature, maximum temperature, average humidity, average wind speed, solar radiation and the cumulative annual precipitation.
In addition to the weather parameters, the daily number of forest fire was provided by the Lebanese Ministry of Environment.
For each day of weather data from LARI corresponds a specific number of fires that is extracted from the fire list.
The daily number of fires over the nine years is used to create the four scales of danger on which the prediction takes place.
The proposed method introduces a fire risk index on a scale of 1 to 4, where 1 corresponds to the lowest fire risk and 4 to the highest fire risk.
This index is based on the number of fires that occurred on a specific day and hence can be used to estimate the actual number of fires that could happen on that day.
Class 1 always corresponds to a no fire day.
As for class 2, it corresponds to any number of fires that falls between the first quartile and the third quartile of the number of fire distribution that is given by the historical data.
Class 3 corresponds to an increase of risk by 10% from the third quartile and class 4 corresponds to any risk greater than 10%.
Table II shows the corresponding number of fires per month per scale which defines the four classes.
A challenge is to have this index independent of weather prediction mechanisms; and thus avoid the problem created by potential erroneous weather forecasting.
To avoid weather prediction mechanisms, the training points are created as follows: the weather parameters of a given day are associated with the scale of the next day and hence the relationship that is being learned by SVM is the relationship between the weather parameters of today and the number of fires of the following day.
This architecture is used for daily prediction.
The above architecture could be used for monthly prediction, by associating the average weather parameters of a month with a scale for the following month.
Or it could be used for annual prediction by associating the average weather of the year with the scale of the next year.
Due to the limited amount of data which corresponds only to 9 years, it is not possible to create an annual classifier or a monthly classifier.
The architecture is then tested only for daily prediction.
After labeling the points using table II the training of the algorithm is performed.
Although each month has different parameters, the training is conducted the same way for all months.
Half of the points of a month are taken as training points.
The points are chosen in a way to be equally distributed between the four classes.
Then the architecture is tested on the remaining points of that same month.
This procedure is performed for all the months.
The performance of the architecture is tested by computing the average error on the number of fire predicted.
Denote by Ni the true number of fires that occurs on day i and by di the predicted scale for that same day.
Denote also by qmin,c the lower boundary of class c and by qmax,c the upper boundary for that same class.
Then the error on the decision made on day i is given by: Efi=⎧⎩⎨0qmin,di−NiNi−qmax,diifqmin,di≤Ni≤qmax,diifNi<qmin,diifNi>qmax,di(9) View SourceRight-click on figure for MathML and additional features.
TABLE I Output scale.
SVM1	SVM2	SVM3	Output Scale −1	−1	NA	1 −1	1	NA	2 1	NA	−1	3 1	NA	1	4 TABLE II Class boundaries.
Scale 1	Scale 2	Scale 3	Scale 4 June	0	1–3	4–7	≥8 July	0	1–4	5–8	≥9 August	0	1–3	4–15	≥;15 September	0	1–4	5–16	≥17 October	0	1–7	7–11	≥12 Another error parameter is the scale error.
If Ci is the true class of day i then the scale error is given by: Esi=|Ci−di|(10) View SourceRight-click on figure for MathML and additional features.
The results are presented in table III as follows: the second line corresponds to the expected value of the fire error computed over all the days of the month and the third line shows the expected value of the scale error taken also over all days of the month.
For example, in June the average error on the number of fires when the predicted scale was equal to 1 is 0.53 fires, while the average scale error is 0.4. It is worth noting that the average scale error is less than 0.8 except for four cases and drops as low as 0.2, which shows that the decision on average is very close to the true scale.
This 4-class classifier can be specialized for the case of binary classification.
By grouping scale 1 and 2 together and scale 3 and 4 together, it is possible to discriminate a high risk day from a low risk day with a high accuracy.
The two class accuracy is shown in table IV.
TABLE III Prediction results for the five-month fire season.
Table III- Prediction results for the five-month fire season.
TABLE IV Two-class classifier results.
Month	Accuracy June	89% July	85% August	96% September	90.2% October	78.4% SECTION IV.Conclusion The paper presented a forest fire risk prediction mechanism, based only on meteorological data and independent of any weather prediction mechanism.
The results demonstrates the ability to predict forest fire risk with a limited amount of data and has shown that support vector machines can be used for a two-class prediction of fire risk with a very high accuracy of up to 96% for August as well as four classes prediction with a low error on the number of fires as well as on the predicted scale.
Abstract The ecological value of tropical forests in water conservation district has been of great interest because of their rich vegetation types and higher biomass density than any other land cover types, it is urgent to evaluate the ecological value of tropical forests in water conservation district.
However, the monitoring of tropical forests in water conservation district is faced with many problems, such as high forest density, complexity and diversity of the forest structure, complex topography and climate conditions, and the difficulty of access for investigators.
In order to solve the above difficulties, this study combined 3D point cloud reconstruction based on Unmanned Aerial Vehicle - Structure from Motion (UAV-SfM) technology with forest type classification based on the Convolutional Neural Network (CNN) method, combined with a small amount of forest permanent sample plot survey data, to accurately evaluate the forest biomass distribution and forest biodiversity in water conservation district.
The results show that the overall classification accuracy of the 20 forest types in water conservation district based on the CNN method is 0.61, the overall Kappa coefficient is 0.59, and the conditional Kappa coefficient is concentrated in the range of 0.43–0.85.
The Root Mean Square Error (RMSE) of the plane measurement of UAV-SfM technology is 0.432 m, and the RMSE of the elevation measurement is 0.989 m, the effect of this UAV technology in tropical forest monitoring is superior.
Using the techniques mentioned above, this study can effectively and accurately monitor and evaluate the biomass distribution and biodiversity of tropical forests in the water conservation district.
Based on the precision forest ecological monitoring data, this study can develop a scientific and reasonable sustainable forest management plan for the water conservation district according to the distribution of forest biomass and biodiversity.
The combination of UAV-SfM technology and the CNN method is an innovative attempt, and the integration of UAV and artificial intelligence technology solves practical problems faced by sustainable forest management.
UAV and artificial intelligence will also provide an important foundation for forest ecological environment sustainability assessment research.
Previous article in issue Next article in issue Keywords Unmanned aerial vehicleArtificial intelligenceTropical forestForest ecological monitoringSustainable forest management 1.
Introduction For a long time, due to the economic development and expansion of comprehensive agriculture, many woodlands were damaged and the ecological security of the country was seriously threatened.
In the past two decades, in order to protect and improve the ecological environment, China has implemented the policy of returning grain plots to forestry (Li et al., 2016).
Among the various environments, the aquatic ecosystem is one that is most affected by human activities (Best, 2019).
Forests in water conservation district have been paid more and more attention by people because of their significant contributions to maintaining the stability of water bodies (Teng et al., 2019), improving the quality and quantity of fresh water, regulating river temperature, filtering and protecting nutrients, increasing biodiversity and habitat (Janssen et al., 2020), reducing erodibility, etc.
(Asanok et al., 2017; Bonansea et al., 2016; Johnson, 2002).
In particular, tropics have rich vegetation types, higher biomass and biodiversity density than any other areas (Pérez-Cárdenas et al., 2021).
Their ecological value has received extensive attention (Asanok et al., 2017; Sanches et al., 2020).
However, there are few studies on the correlation between biomass, biodiversity and forest structure of water conservation district.
It is urgent to evaluate the sustainability of tropical forests.
Forest biomass monitoring is necessary for forest ecological value evaluation, but it is difficult to monitor forest biomass in tropical areas.
Tropical regions are faced with such difficult problems as high forest density (Philippe et al., 2020; Linares-Palomino and Alvarez, 2005), high complexity and diversity of forest structure (Bojórquez et al., 2020; Chave et al., 2014), as well as complex topographic and climatic conditions (Kübler et al., 2020), which makes it difficult for investigators to enter.
In order to solve the above difficulties, satellite remote sensing, ground laser radar and other technologies are better solutions, but there are still problems such as low resolution, high labor costs and inconvenient carrying of machines (Koukal et al., 2014; Asner et al., 2010).
In the past 10 years, Unmanned Aerial Vehicle (UAV) technology has been widely used in ecological and environmental monitoring (Casazza et al., 2019; Jiang et al.,2021; Johansen et al., 2019; Zhang et al., 2020); it is increasingly used for forest resource inventory due to its greater availability and miniaturized sensors (Ma et al., 2015; Qiu et al., 2018b; Hao et al., 2021; Hu et al., 2021b).
UAV photogrammetry technology has also been widely used in tropical area forest surveys (Popescu, 2007; Lechner et al., 2020).
Since the concept of artificial intelligence was introduced, machine learning algorithms have been an important direction of artificial intelligence, and with the development of Artificial Intelligence (AI) technology, machine learning algorithms such as Support Vector Machine (SVM), Random Forest (RF), Extreme Gradient Boosting (EGB), K-nearest Neighbor (KNN), Ensembles of Classifiers (EC), Decision Trees (DT), Maximum Likelihood (ML) and Multilayer Perceptron (MP) are widely used to carry out forest type classification (Koukal et al., 2014), forest tree species classification (Dalla Corte et al., 2020), land use and cover change classification (Ge et al., 2020), urban tree classification (Rahman et al.,2020)and others by using UAV remote sensing images, especially in forest management, forest resources inventory, ecosystem modeling and other aspects.
However, there has been no substantial breakthrough in the study of complex tropical forests, especially tropical forests in water conservation district.
In complex tropical forests, deep learning algorithms have greater advantages and potential than machine learning algorithms in forest type classification of remote sensing images (Xi et al., 2020; Carbonneau et al.,2020; Hu et al., 2021a).
The Convolutional Neural Network (CNN) method, in particular, has the functions of automatic feature selection and feature management.
The CNN method usually consists of a long series of layers, each of which is a function of the previous layer.
By convolving deep layers, signals or features can be enhanced and filtered until features become easy to classify (Xi et al., 2020).
Carbonneau et al.
(2020) used machine learning algorithms such as ML, MP, RF and CNN-Supervised Classification to classify the RGB images of 11 rivers, and the indicators showed that the classification ability of deep learning algorithms was significantly higher than that of machine learning algorithms.
(2020) used the CNN method to draw temperate forest types in RGB images taken by high-resolution UAVs, which also proved the excellent classification ability of the CNN method.
In addition, compared to the traditional method of monitoring above-ground biomass, UAV remote sensing imaging improves the efficiency of forest biomass estimation (McRoberts et al., 2010; Navarro et al., 2020; Ruwaimana et al., 2018).
However, the accuracy of biomass estimation is limited when UAV remote sensing imaging alone is used for monitoring such a highly complex and high-density tropical forest (Bork and Su, 2007; Otero et al., 2018).
To some extent, 3D point cloud reconstruction based on Structure from Motion (SfM) technology can be used to estimate the overall forest biomass (Navarro et al., 2020; Ramalho de Oliveira et al., 2021), which is more accurate than the estimation accuracy using UAV remote sensing imaging through RGB band imagery (Sankey et al., 2017).
In addition, in the face of continuous global forest loss, planned sustainable forest management programmes are gradually restoring abandoned or degraded woodlands (Siry et al., 2005).
In order to support sustainable forest management, forest ecological monitoring data should be updated continuously as the basis (Wulder et al., 2008).
There is an increasing demand for low-cost and high-quality forest ecological monitoring data (Laudon et al., 2011).
The application of UAV remote sensing technology provides convenient, accurate and detailed spatial information of forest environment for sustainable forest management (Zhu et al.
(2014) combined UAV with LIDAR to obtain high-density forest environmental data as the research basis.
(2019) used UAV as a platform to obtain Digital Aerial Photogrammetry (DAP) data, which has high application value in the evaluation of forest ecological environment and sustainability.
This is enough to prove that UAV remote sensing can provide efficient and precision technical support for forest ecological environment monitoring and forest sustainable management.
Therefore, this study intends to complement the advantages of UAV-SfM technology and the CNN method, and use deep learning to classify forest types on UAV remote sensing images.
Combined with 3D point cloud reconstruction and measurement, the study on forest biomass distribution in water conservation district is carried out.
In addition, on the basis of the classification of forest types, the distribution of forest biodiversity in the water conservation district was explored through the diversity index.
On the basis of the results of forest biomass and biodiversity evaluation, the sustainable forest management plan for the water conservation district was developed.
The specific research technical route is shown in Fig.
1 Download: Download high-res image (852KB) Download: Download full-size image Fig.
Technology roadmap.
Methods 2.1. Data source This study area is located in the water conservation district of the Yongzhuang Reservoir in Haikou City (Fig.
2), with a study area of 383.161 ha.
It is located in the upstream part of the Wuyuan River in the Xiuying District of Haikou City, and was designated as one of the urban drinking water sources in 2008.
The study area has a complex forest structure, high forest density and diversity, and the woodland is a typical tropical secondary forest.
With the establishment of a free trade port in Hainan, this province is expected to grow by 5 million people and with the influx of people, fresh water resources are a top concern in Haikou City, which is the provincial capital and the most populous city.
Therefore, it is of great significance to study the protection of the water conservation district.
2 Download: Download high-res image (2MB) Download: Download full-size image Fig.
Water conservation district location of Yongzhuang Reservoir in Haikou City.
In this study, a DJI Mavic Pro UAV (SZ Dà-Jiāng Innovations Science and Technology Co., Ltd.) was equipped with a camera with a built-in 1/2.3 inch CMOS sensor, with an effective pixel of 12.35 million and a relative flight height of 100 m.
Through the designation of imaging range and image overlap (lateral overlap is 70%, fore-and-aft overlap is 80%) the flight path and exposure points were automatically calculated, and the area imaging was completed by spot-hover shooting.
In addition, the tripod head control shots were always straight down to ensure a relatively stable image attitude angle.
The built-in Global Positioning System (GPS) module of the UAV recorded the positions of exposure points and stored them in the images in the form of Exchangeable Image File Format (EXIF) information, and 3824 high-resolution UAV images were then obtained.
The CTI i70 (Centre Testing International Group Co., Ltd.) Global Navigation Satellite System - Real Time Kinematic Studio (GNSS-RTK) was used to calibrate 24 ground Photo-control-points in the WGS84 coordinate system, the RMSE of plane measurement was 2 cm, and the RMSE of height determination was 3 cm.
In addition, there were 29 forest permanent sample plots (100 m2) of forest survey, a total of 20 kinds of typical tropical forest types in water conservation district, with Casuarina equisetifolia or Microcos neroosa (Sample Plot 1), Ficus hispida (Sample Plot 2), Dracaena cochinchinensis (Sample Plot 3), Khaya seegalesis (Sample Plot 4), Areca catechu (Sample Plot 5), Mangifera indica (Sample Plot 6), Ravenea rivularis (Sample Plot 7), herb (Sample Plot 8), Acacia mangium or Viburnum Odoratissimum (Sample Plot 9), Bambusoideae (Sample Plot 10), Pachira aquatica or Psychotria rubra (Sample Plot 11), Elaeocarpus decipiens (Sample Plot 12), Eucalyptus robusta (Sample Plot 13), Clausena lansium (Sample Plot 14), Terminalia neotaliala (Sample Plot 15), Machilus pingii (Sample Plot 16), Ficus religiosa (Sample Plot 17), Pterocarpus indicus (Sample Plot 18), Plumeria rubra (Sample Plot 19) and Ehretia thyrsiflora (Sample Plot 20) as the main tree species.
This study used the method of tree-by-tree survey to record the plant height and Diameter at Breast Height (DBH) of trees (DBH 3 cm and above), shrubs, economic forests and bamboo forests, and record the plant height and surface area of large herbaceous plants.
In addition, the biomass of trees, shrubs, economic forests, bamboo forests and large herbaceous plants was measured by digging, cutting, sampling and drying.
There were 70 main tree species (280 trees) including trees, shrubs and economic forests, Bambusa textilis, Miscanthus and Eupatorium odoratum, each having 10 plants, establishing   -biomass mixture regression model   (Qiu et al., 2020), and the vegetation biomass of 29 forest permanent sample plots was calculated by the fitted model.
2.2. Forest type classification based on CNN method The CNN model consisted of an input layer, convolutional layer, pooling layer, fully connected layer and output layer.
As shown in Fig.
3, the preprocessed data passes through the input layer to generate a hidden convolutional layer C1, under the action of convolutional kernel and bias units.
Each unit in the feature diagram of C1 is independent and locally connected with the previous layer, and is given some weight and bias.
A new feature graph is generated under the action of activation function, forming the second hidden pooling layer S1 of the CNN model.
Through the alternating action of the convolution layer and the pooling layer, the full connection layer is established in the form of one-dimensional vector quantity for several feature graphs.
The full connection layer outputs the results through data processing, forming the output layer of the CNN model.
3 Download: Download high-res image (394KB) Download: Download full-size image Fig.
CNN model structure.
Assuming that the neural unit of j in the convolution layer of l of the CNN model is expressed as  , the characteristics of the convolution layer of l are shown in Formula (1): (1) in which   represents the convolution kernel between the feature of j in layer l, and the feature of i in layer  ;   is the corresponding bias, and   represents the corresponding connection matrix.
When  , it means that the corresponding features are related, and if  , it means that they are not related.
represents the feature vector, and   represents the activation function used by the neural network.
If the next layer of   is the pooling layer, then each feature after pooling is  .
is a pooling function, which selects non-overlapping data during operation and keeps the same feature number as the previous layer.
One of the purposes of pooling is to obtain data features, and the other is to reduce data dimensions.
The common pooling methods are maximum pooling method and average pooling method.
After pooling, a one-dimensional vector about features is generated.
If the next layer is a fully connected layer, the feature vector of the   layer is shown in Formula (2): (2) where   is the weight between this layer and the previous layer,   is the corresponding offset, and   is the activation function.
2.3. 3D point cloud reconstruction and measurement based on SfM technology To extract the three-dimensional surface structure of forest land, 3D point cloud reconstruction and measurement based on SfM were carried out on the original UAV images (Fig.
SfM algorithm steps were as follows: (1) feature extraction and matching of dense images with the same name; (2) using the feature points with the same name to carry out image relative orientation and calculate the external orientation elements; (3) generating sparse point clouds by three-dimensional processing and iterative beam adjustment; (4) dense point cloud obtained based on sparse point cloud encryption.
In this study, DJI Terra Professional Edition Software (SZ Dà-Jiāng Innovations Science and Technology Co., Ltd.) was used to process UAV images.
DAISY operator of feature matching and sub-pixel matching was used in feature point retrieval.
The UAV built-in GPS can provide the fuselage coordinates at the exposure time, which can be used as the initial coordinates of the external orientation elements of the image for iterative optimization.
And last, the Patch-Based Multi-View Stereo (PMVS) algorithm was used to search pixels in the image to get more matching points, that is, dense point cloud data.
In addition, DJI Terra Professional Edition Software has built-in volume measurement function, which can measure 3D point cloud accurately.
4 Download: Download high-res image (606KB) Download: Download full-size image Fig.
3D point cloud reconstruction process based on SfM technology.
2.4. Forest biomass estimation and biodiversity assessment According to WGS84 coordinates, 3D point cloud data is registered with Digital Orthophoto Map (DOM) images.
In the study area, 500 quadrats (10 m × 10 m) were selected equidistantly to measure the 3D point cloud, and the tropical forest types in water conservation district of the quadrats were determined according to the classification results of tropical forest types in water conservation district in DOM images.
The volume-biomass conversion coefficient K of different tropical forest types in water conservation district was obtained according to Formula (3): (3) where V is the measured volume of 3D point cloud in forest permanent sample plots,  ; W is the biomass for the forest permanent sample plots,  .
In this study, biodiversity of 20 forest types was calculated, and three species diversity indices, Shannon-Weiner diversity index (Formula 4), Pielou's species evenness index (Formula 5) and Simpson's diversity index (Formula 6), which are widely used in α diversity measure, were used to calculate species diversity.
(4) (5) (6) Where   is the ratio of the number of ith species   to the total number of all species   ( ).
can not only reflect the richness of species in the forest, but also express the evenness of species distribution.
is the total number of species in the sample plot of species  , which is the species richness index.
Results 3.1. Results of 3D point cloud reconstruction and DOM image generation Using DJI Terra Professional Edition Software to import 3824 images, combined with 12 ground Photo-control-points, the original UAV image was stitched and geocoded.
The initial correction error of camera parameters was 2.5%, and the average error of combined bundle adjustment was 0.3 pixels.
3D point cloud reconstruction was carried out in the study area, and the density of point clouds was 600–1000PCs/m2.
Orthophoto correction was carried out by using the point cloud elevation information, and a DOM image with spatial resolution of 0.05 m was generated as the base map of the experimental area.
The results of 3D point cloud reconstruction and DOM image generation are shown in Fig.
The other 12 ground Photo-control-points were used as accuracy verification, and the plane and elevation accuracy verification were carried out according to the RMSE formula (Qiu et al., 2018b).
The RMSE of the plane survey was 0.432 m, and that of the elevation survey was 0.989 m.
5 Download: Download high-res image (1MB) Download: Download full-size image Fig.
3D point cloud reconstruction and DOM image generation results.
3.2. Results of forest types classification based on CNN method Image pixel marking was carried out by using the initial marking estimation input by itself, and a new and accurate marking estimation was predicted.
The treating process was first to detect the incorrect initial mark estimation, then to replace the incorrect mark with a new mark, and finally refine the updated mark.
Iterative execution can correct the incorrect mark in a larger area, to finally obtain the correct result.
The experimental area was marked to obtain the experimental range, from which 50% samples were selected randomly to form a training data set, and 10% samples were selected randomly as a test data set.
The experiment of forest type classification was carried out on the platform of Matlab 2019a (MathWorks.
The initial value of learning rate was set as 0.02, and the initialization bias was set as 0; the number of nodes in a Boltzmann Machine should be between 20 and 148 since the classification number was 20.
The classification results are shown in Fig.
The classification accuracy was selected to represent the performance of the model, and the classification effect was measured by Kappa coefficient.
The accuracy analysis results show that the overall classification accuracy was 0.61, the overall Kappa coefficient was 0.59, and the conditional Kappa coefficient of sample plots was concentrated between 0.36 and 1.00, as shown in Table 1.
6 Download: Download high-res image (1MB) Download: Download full-size image Fig.
Tropical forest types classification in water conservation district.
Accuracy of tropical forest types classification in water conservation district.
Sample Plot Number	Conditional Kappa Coefficient	Sample Plot Number	Conditional Kappa Coefficient Sample Plot 1	0.89	Sample Plot 11	0.62 Sample Plot 2	0.36	Sample Plot 12	0.70 Sample Plot 3	0.43	Sample Plot 13	0.44 Sample Plot 4	0.36	Sample Plot 14	0.70 Sample Plot 5	0.79	Sample Plot 15	0.85 Sample Plot 6	0.52	Sample Plot 16	1.00 Sample Plot 7	0.48	Sample Plot 17	0.61 Sample Plot 8	0.68	Sample Plot 18	0.68 Sample Plot 9	0.64	Sample Plot 19	0.83 Sample Plot 10	0.43	Sample Plot 20	0.66 3.3. Results of forest biomass estimation and forest biodiversity evaluation The volume-biomass conversion coefficient K of 20 tropical forest types in water conservation district was quite different, as shown in Table 2.
Spatial interpolation analysis of biomass of 500 quadrats by using the anti-distance weighted average method of ArcGIS 10.8 (Environmental Systems Research Institute), and the biomass ranged from 0 to 1300 Mg/ha as shown in Fig.
Relationship between 3D point cloud volume (m3/ha) and biomass (Mg/ha) in 20 forest types.
Sample Plot Number	Conversion Coefficient (K)	Sample Plot Number	Conversion Coefficient (K) Sample Plot 1	0.001614	Sample Plot 11	0.001981 Sample Plot 2	0.000832	Sample Plot 12	0.000953 Sample Plot 3	0.000650	Sample Plot 13	0.009841 Sample Plot 4	0.007480	Sample Plot 14	0.000565 Sample Plot 5	0.002050	Sample Plot 15	0.003979 Sample Plot 6	0.000424	Sample Plot 16	0.002963 Sample Plot 7	0.003934	Sample Plot 17	0.003788 Sample Plot 8	0.000155	Sample Plot 18	0.000707 Sample Plot 9	0.001884	Sample Plot 19	0.001221 Sample Plot 10	0.003938	Sample Plot 20	0.001907 Fig.
7 Download: Download high-res image (436KB) Download: Download full-size image Fig.
Tropical forest of water conservation district biomass distribution.
Biodiversity indexes of 20 forest types were calculated, and the results were shown in Table 3.
The Shannon-Weiner diversity index was between 0 and 2.9533, the Simpson's diversity index was between 0 and 0.7844, and the Pielou's species evenness index was between 0 and 1.4203.
It can be seen that the biodiversity indexes of different forest types varied greatly.
The forest biodiversity index of plot 6, plot 10, plot 15, plot 18 and plot 20 is 0.00.
These five forest types are mainly Mangifera indica, Bambusoideae, Areca catechu, Pterocarpus indicus, Ehretia thyrsiflora and other artificial planted economic forests.
The common Kriging interpolation method of ArcGIS 10.8 was used to conduct spatial interpolation analysis on the forest biodiversity of 500 quadrats, and the results were shown in Fig.
From north to south, the forest biodiversity of the water conservation district is decreasing.
The forest biodiversity in the northeast and southwest is obviously low, which is close to the residential areas and is mainly planted with a large number of artificial forests.
In addition, the areas close to the reservoir with less human intervention have rich forest structure and higher forest biodiversity.
Biodiversity index of 20 forest types in water conservation district.
Sample Plot Number	S	Shannon-Weiner	Simpson	Pielou Sample Plot 1	6.6	1.8560	0.5830	0.9547 Sample Plot 2	8	2.6537	0.8091	1.2772 Sample Plot 3	6	2.0216	0.7142	1.1283 Sample Plot 4	5	1.1629	0.3863	0.7225 Sample Plot 5	3	1.5204	0.6378	1.3839 Sample Plot 6	1	0.0000	0.0000	0.0000 Sample Plot 7	8	2.3310	0.7169	1.1210 Sample Plot 8	8	2.9533	0.7844	1.4203 Sample Plot 9	8	2.1157	0.6927	1.0174 Sample Plot 10	1	0.0000	0.0000	0.0000 Sample Plot 11	7	1.7872	0.6326	0.9184 Sample Plot 12	2	0.4022	0.1472	0.5802 Sample Plot 13	6	1.7843	0.5996	1.1189 Sample Plot 14	2	0.5746	0.2355	0.8290 Sample Plot 15	1	0.0000	0.0000	0.0000 Sample Plot 16	2	0.6962	0.3047	1.0044 Sample Plot 17	2	0.2352	0.0740	0.3393 Sample Plot 18	1	0.0000	0.0000	0.0000 Sample Plot 19	7	1.4497	0.4308	0.7450 Sample Plot 20	1	0.0000	0.0000	0.0000 Fig.
8 Download: Download high-res image (1MB) Download: Download full-size image Fig.
Forest biodiversity index distribution in water conservation district.
Discussion 4.1. Feasibility analysis of applying UAV technology in forest ecological environment evaluation In order to solve the problem of the low efficiency and high cost of forest monitoring, researchers transformed 2D images into 3D point cloud data, which is widely used in forest monitoring.
(2018a) used a continuous terrestrial photogrammetry measurement system to acquire 3D point cloud data, which reduced the cost of data acquisition and improved the efficiency of field measurement.
In recent years, UAVs as a tool for forest investigation and monitoring have been widely used by the forest industry.
(2013) and Roşca et al.
(2018) found that UAV-SfM technology has a small defect in forest 3D point cloud reconstruction compared with Terrestrial Laser Scanner (TLS) technology.
However, the Pearson correlation coefficient between point cloud based on UAV-SfM technology and point cloud based on TLS technology is well correlated and has a good prospect.
(2020) combined Unmanned Aerial Vehicle-Light Detection and Ranging (UAV-Lidar) with Backpack-LiDAR, and measured the regional accuracy of healthy forests between 0.57 and 0.81, and the regional accuracy of severely withered forests may reach 0.92.
The research of Qiu et al.
(2018b), Bourgoin et al.
(2020) and Jayathunga et al.
(2018) also shows the advantages of cheap and portable UAVs in forest monitoring, forest type analysis and forest structure characteristics.
Compared with other regions, tropical forests have the characteristics of high forest density, heterogeneity and diversity, which bring many new challenges to forest monitoring.
To solve this problem, this study combined 3D point cloud reconstruction based on UAV-SfM technology and forest type classification based on the CNN method, combining the advantages of the two methods, and making up for the defect that 3D point cloud cannot classify forest types.
Because the canopy shapes of broad-leaved forest and mixed forest are irregular and overlapping, it is difficult to classify forest types.
(2018) combined multi-temporal SAR data and SPOT-5 images, using the RF algorithm to identify forest types, and the accuracy rate exceeded 88%.
(2021) combined UAV-SfM technology with the Region Growing algorithm, and obtained the highest overall accuracy of 0.79.
(2020) used an UAV combined with the RF algorithm to classify forest multi-dimensional features, and the Kappa coefficient was 0.72.
The research of Schiefer et al.
(2020) shows that the CNN method has the advantages of fast and flexible classification for temperate forest types in the high-resolution RGB images provided by UAV.
The above studies have achieved good classification accuracy in the classification of temperate forest types by using various techniques.
However, it is difficult to apply to forest monitoring in tropical areas with high forest density, heterogeneity and diversity.
In this study, the overall classification accuracy of tropical forest types was 0.61, and the overall Kappa coefficient was 0.59, which is slightly lower than that of temperate forest types.
However, compared with 3–5 types of temperate forests, the classification of forest types in this study was as high as 20 types, which is more suitable for forest monitoring in tropical areas with high heterogeneity and diversity, and has achieved satisfactory accuracy at this research stage.
Generally speaking, this study still has the problem of classification fragmentation caused by excessive classification of forest types.
In future research, it is necessary to further classify tropical forest types in combination with forest structure and forest environment, and to reduce the number of forest types without affecting the monitoring accuracy.
In addition, the UAV equipped with five lenses has gradually replaced oblique photography.
Combined with UAV-SfM technology, the accuracy of 3D point cloud reconstruction and measurement can be further improved in the future.
With the innovation of UAV and artificial intelligence technology, forest ecological environment monitoring will also be more efficient and precision, which lays an important foundation for the formulation of sustainable forest management plans more scientifically.
4.2. Policy analysis of sustainable forest management based on forest biomass and biodiversity Biodiversity is an important indicator to measure whether the ecological environment is sustainable (Dudgeon et al., 2006), and forest biomass is an important indicator for forest ecological environment monitoring.
Based on the efficient and precision monitoring of forest ecological environment by using UAV and artificial intelligence technology, this study can make a more scientific and precision sustainable forest management plan.
The sustainable forest management plan is as follows: 1.
Forest biodiversity and biomass in the study area gradually decreased from north to south, and in addition, forest biodiversity and biomass were positively correlated on the whole (Pyles et al., 2018).
Therefore, improving forest biodiversity and increasing forest biomass must be the development direction of sustainable forest management.
In the northeast and southwest regions and the cropland areas near villages, there is a general trend of high forest biomass and low biodiversity, because the forestland is mostly artificial planted trees.
It is concluded that, for a long time, plantation management in Hainan Province only aims at maximizing the acquisition of wood and economic products, but lacks consideration of the ecological functions of undergrowth vegetation and plant diversity, which leads to the sharp decline of plant diversity, the decline of land fertility and the low capacity of biomass carbon sequestration.
Therefore, according to the Technical Specifications for the Division of Drinking Water Source Protection Areas, the management and protection of the forestland in the first-level water conservation district (Fig.
9) should be strengthened, the functions of the forestland should be transformed, and the forestland in the first-level water conservation district should be changed from economic benefits to ecological benefits.
9 Download: Download high-res image (2MB) Download: Download full-size image Fig.
Study area within the first-level and second-level water conservation district.
In the study area, the biodiversity index of the forestland dominated by mango and bamboo was 0.
In addition, the artificial forest structure is single, lack of undergrowth shrub layer, has been relying on human management and protection, some areas close to the reservoir, long-term fertilization and cultivation may cause point source pollution to the reservoir.
Therefore, in this area, it is more necessary to change the forest structure of artificial forest through natural regeneration (Crouzeilles et al., 2017), enrich the forest structure levels, effectively prevent soil erosion, slow down surface runoff, and avoid point source pollution from flowing into reservoirs through runoff, so as to improve the forest ecological environment and achieve sustainable forest development.
The forest near the reservoir is in better condition than the forest far away from the reservoir.
The forest biodiversity and biomass near the reservoir are generally high.
This indicates that some areas have naturally germinated into nearly natural forest pattern and have more complex forest structure.
This discovery has positive significance for water conservation and is the main research direction for sustainable forest management in water conservation district in the future.
In the eastern part of the reservoir, the herbaceous layer and shrub layer are the main layer, and there is a lack of tree layer.
After the conversion of farmland to forest, it is still in the early stage, and the forest biodiversity is high, but the forest biomass is low.
Waterfront plants play an important role in maintaining nutrients and water purification in terrestrial habitats (Richardson et al., 2012).
With the rapid growth of tropical forests, sparse forest structures dominated by small pioneer species can emerge within 10–30 years (Marín et al., 2009).
Therefore, it is necessary to intensify the efforts of returning farmland to forest in this area, and form the periodic succession from herb layer, shrub layer, open forest, dense forest to climax community.
On the basis of ensuring the naturalization of forestland in the first-level water conservation district, the buildings, farmland and plantations in the second-level water conservation district should be adjusted.
For forests close to cities, it is difficult for any formal forest management system to control human disturbance, especially in meeting the living needs of surrounding farmers (Laudon et al., 2011).
Therefore, Participatory Forest Management can be applied to forestland in the second-level water conservation district, taking ecological and economic benefits into consideration.
Studies (Gurung et al., 2013; Treue et al., 2014) have shown that Participatory Forest Management, which is integrated with the government and the public, contributes to more effective management, restoration of degraded land and maintenance of forest conditions, and benefits the surrounding farmers.
The evolution process of forest ecological environment in the water source protection area should be monitored for a long time, and the problems in the process of forest sustainable management should be adjusted timely through scientific forest ecological environment data and forest management indicators (Maes et al., 2011; Mäkelä et al., 2012).
This initiative can improve the quality and efficiency of sustainable forest management and lay an important research foundation for the realization of near-natural forest structure.
The study area is faced with problems such as insufficient forest management and serious human interference.
In addition, the zoning management of the first-level and second-level water conservation district is not strictly implemented according to the regulations, leading to the confusion of forest types.
Therefore, it is necessary to establish an innovative mechanism guided by the government and participated by the masses, strengthen publicity and education, improve the ecological protection consciousness of the public, and maintain the sustainable development of the forest.
Conclusions Sustainable forest management urgently needs precision forest ecological environment data, therefore, sustainable forest management needs to use high-tech means to achieve efficient and accurate management.
The combination of UAV and artificial intelligence technology is an innovative attempt to provide an efficient and precision solution for ecological monitoring in areas with complex forest structure.
The acquisition of forest ecological monitoring data by UAV and artificial intelligence technology can lay the foundation for sustainable forest management planning.
The forest structure of Yongzhuang reservoir water conservation district is complex, so the research method is representative and universal, and can provide reference for forest ecological monitoring and sustainable forest management in 2466 county-level water conservation district in China.
At present, due to the continuous development of sensors and the continuous improvement of artificial intelligence algorithms, the precision of forest ecological monitoring is bound to be further improved, and this new technology will be more widely used in the future sustainable forest management.
When researchers collect audio recordings of birds, they are usually listening for the animals’ calls.
But conservation biologist Marc Travers is interested in the noise produced when a bird collides with a power line.
It sounds, he says, “very much like the laser sound from Star Wars”.
In 2011, Travers wanted to know how many of these collisions were occurring on the Hawaiian island of Kauai.
His team at the University of Hawaii’s Kauai Endangered Seabird Recovery Project in Hanapepe was concerned specifically about two species: Newell’s shearwaters (Puffinus newelli) and Hawaiian petrels (Pterodroma sandwichensis).
To investigate, the team went to the recordings.
With some 600 hours of audio collected — a full 25 days’ worth — counting the laser blasts manually was impractical.
So, Travers sent the audio files (as well as metadata, such as times and locations) to Conservation Metrics, a firm in Santa Cruz, California, that uses artificial intelligence (AI) to assist wildlife monitoring.
The company’s software was able to detect the collisions automatically and, over the next several years, Travers’ team increased its data harvest to about 75,000 hours per field season.
Results suggested that bird deaths as a result of the animals striking power lines numbered in the high hundreds or low thousands, much higher than expected.
“We know that immediate and large-scale action is required,” Travers says.
His team is working with the utility company to test whether shining lasers between power poles reduces collisions, and it seems to be effective.
The researchers are also pushing the company to lower wires in high-risk locations and attach blinking LED devices to lines.
For underfunded conservation scientists, AI provides an attractive alternative to manually processing huge troves of data, such as camera-trap images or audio recordings.
A PhD student could “spend months labelling it all by hand before they can get anywhere near answering their hypothesis”, says Dan Stowell, a computer scientist at Queen Mary University of London.
Citizen science is one option to help with the data, but it isn’t always the right one: volunteers might work too slowly, and recruiting for projects that involve non-charismatic species can be difficult.
AI tools don’t experience fatigue-related performance deterioration, as humans do, and they might be better at detecting infrequent or complex patterns.
Scientists need answers to pressing questions, such as whether conservation actions are working.
And some problems need near real-time results — for instance, law-enforcement agencies pursuing illegal wildlife traffickers need to determine quickly if an animal for sale on social media is protected.
AI could fit the bill.
Despite its reputation for requiring advanced computing skills, AI is now more accessible than ever, thanks to point-and-click tools and dedicated programming libraries.
The software isn’t as accurate or as sensitive as humans at many conservation research tasks, and the amount of data needed to train an AI algorithm to recognize images and sounds can present hurdles.
But early adopters in conservation science are enthusiastic.
For Travers, AI enabled a massive boost in monitoring.
“It’s a huge increase over any other method available,” he says.
Automated identification Researchers interested in AI can, as Travers did, outsource the work.
Conservation Metrics’ pricing starts at US$1–3 per hour of audio, but depends on data volume and project complexity; image-classification pricing is variable.
The company also informally takes on for free three to five projects per year that involve interesting conservation questions or technical challenges; researchers can contact the company for consideration.
Scientists can also use browser-based tools.
One option is Wildbook, a software framework produced by the non-profit organization Wild Me in Portland, Oregon, and its academic partners.
Wildbook uses neural networks and computer-vision algorithms to detect and count animals in images, and to identify individual animals within a species.
This information enables more precise estimates of wildlife population sizes, says Tanya Berger-Wolf, Wildbook co-founder and a computer scientist at the University of Illinois at Chicago.
Wildbook works for any species with stripes, spots, wrinkles, fin or ear notches, or other unique physical features.
The number of manually annotated images needed to start a project depends on the species, says Jason Holmberg, executive director of Wild Me. The team also uses AI to collect images of specific species from YouTube, and will start trawling through Twitter this year.
Researchers and citizen scientists can add images to be identified automatically.
So far, scientists have created projects for more than 20 types of animals, including whale sharks (Rhincodon typus), manta rays (Manta birostris and M.
alfredi), Iberian lynxes (Lynx pardinus) and giraffes (Giraffa sp.).
New users can join existing Wildbook projects for free; setting up a project for a new species typically costs $10,000–20,000, Holmberg says.
Other tools process acoustic data.
The Automated Remote Biodiversity Monitoring Network (ARBIMON) is a browser-based tool produced by Sieve Analytics in San Juan, Puerto Rico.
Researchers upload their recordings, and the company recommends that they manually identify a couple of hundred clips that contain the species call of interest, and hundreds more that do not.
ARBIMON then uses machine learning to classify the remaining data.
So far, about 3.4 million 1-minute recordings have been uploaded, and researchers have monitored animals such as birds, amphibians and cetaceans.
The company charges $0.06 per minute of audio.
Refind Technologies in Gothenburg, Sweden, has even incorporated AI software into custom hardware.
The firm created a device called the Fish Face ID Tunnel to help researchers identify fish subspecies on the basis of photographs taken inside the device.
“You could say it’s a photo booth for fish,” says Johanna Reimers, the firm’s chief executive.
Refind and the environmental charity The Nature Conservancy, based in Arlington, Virginia, installed the device on a fishing boat in Indonesia last year, and the charity is analysing the data.
Researchers interested in a similar device, or a customized version, should expect to pay around $50,000, Reimers says.
Training data Tech-savvy researchers can take advantage of ‘command-line’ AI software to answer conservation questions.
Most cutting-edge results in deep learning use the open-source machine-learning libraries TensorFlow, developed by Google, and PyTorch, led by Facebook, Stowell says.
For the past few years, his team has run contests, called the Bird Audio Detection Challenge, in which participants develop and test algorithms to determine whether bird calls are present in sound clips.
Prizes go to the highest-scoring open-source entries; code from some of the other entries is also posted online.
TensorFlow in particular has a large user community, and many code examples are available online, says Scott Loarie, co-director of the nature app iNaturalist, a joint initiative of the National Geographic Society in Washington DC and the California Academy of Sciences in San Francisco.
Conservation biologists can get up to speed with AI through online classes offered by DataCamp, Coursera, Udacity or the NVIDIA Deep Learning Institute.
The online guide Machine Learning for Humans (see go.nature.com/2sbjasb) offers resources for beginners, and the podcast This Week in Machine Learning & AI (see go.nature.com/2ts36bv) can help biologists to stay up to date.
Collaborations with AI specialists can also help.
Ruth Oliver, an ecologist at Yale University in New Haven, Connecticut, took this approach when analysing about 1,200 hours of audio from the Arctic.
She worked with an electrical engineer, who had experience in machine learning, and ran AI algorithms using the software tool MATLAB to estimate when songbirds arrived in the Arctic and how environmental factors affected vocalizations (R.
4, eaaq1084; 2018).
Despite its apparent ubiquity, AI isn’t an easy solution.
Estimates of the amount of training data required for machine learning vary widely, from hundreds to tens of thousands of manually classified examples, depending on the model, study goals and task complexity.
But for endangered species, it might be “difficult or impossible” to collect a very large sample, says Mitch Aide, a tropical ecologist at the University of Puerto Rico Río Piedras Campus in San Juan and founder of Sieve Analytics.
“In these cases, you do the best you can.”  AI software can also be more error-prone than trained people.
Stowell suggests validating results with a small sample and testing the model on data from a different research project or country to ensure that it generalizes as expected.
To assess accuracy in its work, Travers’ team performed extensive tests comparing Conservation Metrics’ results with on-the-ground observations.
The AI software picked up about half of the strikes seen and heard by humans, and an analyst at the firm manually removed false positives.
To estimate the actual collision rate, the scientists roughly doubled the number detected by the software.
The AI program “doesn’t have to be 100% accurate”, Travers says.
“We just have to know exactly how accurate it is.”  And then there’s the concern that users might blindly accept AI results without understanding how they were generated.
To mitigate that, Peter Ersts, a software developer at the American Museum of Natural History’s Center for Biodiversity and Conservation in New York City, suggests using open-source tools; biologists could ask a colleague with software-development expertise to review and explain the code.
Ersts and his colleagues hope to build a curated set of labelled wildlife images that researchers can use to test new models.
Their open-source program Andenet-Desktop allows users to label species manually and export training data in formats that can be read by frameworks such as TensorFlow and PyTorch.
Researchers can use those libraries to create their machine-learning model, load model parameters back into Andenet and automatically annotate remaining data.
Although early results are promising, human input is still needed.
“We can’t fully replace people yet, and nor should we,” Ersts says.
first_pageDownload PDFsettingsOrder Article Reprints Open AccessReview Potential for Artificial Intelligence (AI) and Machine Learning (ML) Applications in Biodiversity Conservation, Managing Forests, and Related Services in India by Kadukothanahally Nagaraju Shivaprakash 1,*ORCID,Niraj Swami 2,Sagar Mysorekar 1,Roshni Arora 1,Aditya Gangadharan 1,Karishma Vohra 1,Madegowda Jadeyegowda 3 andJoseph M.
Kiesecker 4 1 The Nature Conservancy Center, 37 Link Road, Lajpatnagar-3, New Delhi 110024, India 2 The Nature Conservancy, Arington, VA 22201, USA 3 College of Forestry, Keladi Shivappa Nayaka University of Agricultural and Horticultural Sciences, Ponnampet 571216, India 4 Global Lands Program, The Nature Conservancy, Fort Collins, CO 80524, USA * Author to whom correspondence should be addressed.
Sustainability 2022, 14(12), 7154; https://doi.org/10.3390/su14127154 Submission received: 31 March 2022 / Revised: 3 June 2022 / Accepted: 6 June 2022 / Published: 10 June 2022 (This article belongs to the Special Issue Sustainable Use of Natural Resources in a Changing Climate) Downloadkeyboard_arrow_down Browse Figure Review Reports Versions Notes Abstract The recent advancement in data science coupled with the revolution in digital and satellite technology has improved the potential for artificial intelligence (AI) applications in the forestry and wildlife sectors.
India shares 7% of global forest cover and is the 8th most biodiverse region in the world.
However, rapid expansion of developmental projects, agriculture, and urban areas threaten the country’s rich biodiversity.
Therefore, the adoption of new technologies like AI in Indian forests and biodiversity sectors can help in effective monitoring, management, and conservation of biodiversity and forest resources.
We conducted a systematic search of literature related to the application of artificial intelligence (AI) and machine learning algorithms (ML) in the forestry sector and biodiversity conservation across globe and in India (using ISI Web of Science and Google Scholar).
Additionally, we also collected data on AI-based startups and non-profits in forest and wildlife sectors to understand the growth and adoption of AI technology in biodiversity conservation, forest management, and related services.
Here, we first provide a global overview of AI research and application in forestry and biodiversity conservation.
Next, we discuss adoption challenges of AI technologies in the Indian forestry and biodiversity sectors.
Overall, we find that adoption of AI technology in Indian forestry and biodiversity sectors has been slow compared to developed, and to other developing countries.
However, improving access to big data related to forest and biodiversity, cloud computing, and digital and satellite technology can help improve adoption of AI technology in India.
We hope that this synthesis will motivate forest officials, scientists, and conservationists in India to explore AI technology for biodiversity conservation and forest management.
Keywords: forest; artificial intelligence; forest resource management; machine learning; biodiversity conservation 1.
Introduction Artificial intelligence (AI) is a wide-ranging branch of computer technologies concerned with building smart machines capable of augmenting, automating, and accelerating key day-to-day tasks that typically require human intelligence.
It involves extracting patterns, predicting “future states”, and detecting anomalies.
The computational, technological and research breakthroughs in the field of AI have promoted a rise of their application in every field (e-commerce, social network, agriculture, education, environmental sustainability, healthcare, combating information manipulation, social care and urban planning, public safety, transportation, environment conservation, and many more) including forest and wildlife sectors [1,2,3,4,5,6,7,8].
The advancements have been driven by the following factors: (1) the pace with which information is available has increased—creating the opportunity to drive impactful insights and decision-making; (2) the costs of data storage and computing have dropped due to availability of cloud technologies—allowing us to build complex solutions at scale to accelerate experimentation and research; and (3) availability of holistic data sources due to availability of (a) high-resolution satellite imagery, (b) drone and camera technologies, (c) sensors and telemetry technologies (IoT), and (d) people-centric data sources (social networks, citizen science, and other open data sources).
However, the impact of AI technology has been uneven, mostly benefiting high economic return sectors, with fewer applications for forestry [9,10] and biodiversity conservation [11,12,13,14].
Though, application of artificial intelligence (AI) in forest and natural resources management started three decades before [15], the research and adoption of AI technology in the forestry sector lagged behind other fields such as health, transportation, and agriculture [3].
Forests cover approximately 30% of global land area and are dominant terrestrial ecosystems harboring 90% of terrestrial biodiversity [16,17].
Forests are vital for proper functioning of our planet as they provide several critical functions for sustaining life, such as protective functions and environmental services.
For instance, they provide clean, breathable air by stabilizing greenhouse gasses in the atmosphere, and they absorb as much as 30% (2 billion tons/year) of annual global atmospheric CO2 emissions [18].
They play a major role in global food security by supporting pollinators, natural predators of agricultural pests, and the hydrological cycle.
They are an important source of medicinal plants and supply about 40% of global renewable energy (biofuels) [19].
They are critical for hydrological integrity of various ecosystems and contribute to people’s and the ecosystem’s resilience to extreme events such as floods and droughts.
To add to that, about 1.6 billion people depend on forests for their livelihood [20].
Unfortunately, forests also face many challenges.
Globally, forests are undergoing rapid degradation due to exploitation for timber, agriculture expansion, and urbanization.
Impacts of climate change, such as wildfires, are further contributing to global forest degradation [21].
In the last 25 years, 129 million hectares of forest area were lost globally, resulting in a reduction of global carbon stock by 17.4 Gt [22].
It is predicted that the current global trend of forest decline and carbon loss will continue in the near future [19].
Despite the benefits the forest provides and the kind of threats it is experiencing, the forest sector is still using traditional techniques to manage them.
In fact, it is one of the few sectors where adoption of new technology is slow [23].
For example, in many countries including India, forest officials still use pen and paper to conduct forest inventories.
Such traditional methods pose many drawbacks, like the introduction of personal bias, slowing data collection and analysis, and lack of scalability of the approach [24].
In comparison to the forestry sector, other sectors like agriculture—one of the prominent drivers of deforestation—have embraced technological solutions at a rapid pace [25].
Precision agriculture is a result of companies like sagarobotics.com, and farm.bot which use robots for precise de-weeding, precise fertilization, or pesticide applications, as they contribute to higher yields per acres.
Unlike agricultural systems, forests are dynamic in nature, and so they need to be managed accordingly, especially when many governments are currently identifying ways to achieve transformational change to meet their nationally determined contributions—NDCs [19].
This is where technology can play a significant role by filling the gaps/drawbacks of traditional approaches of data collection and analytics, which is crucial for effective forest management and conservation.
The forest sector will benefit significantly by technology’s inherent ability to support innovation and adopt innovation to various geographies and at various scales, and at a much faster pace.
This synthesis article discusses the scope of artificial intelligence and its applications to the Indian forest sector and biodiversity conservation with following objectives: (1) provide a global overview of AI application in the forest sector and biodiversity conservation, and (2) discuss challenges in the Indian forest sector, biodiversity conservation, and relevance of innovative AI technology to solve those challenges.
Materials and Methods We identified published literature and reports that addressed the application of artificial intelligence (AI) and machine learning algorithms (ML) for biodiversity conservation, forest management, and related services across the globe and in India using a systematic literature search.
To establish a database, we searched the ISI Web of Science (http://webofknowledge.com, accessed on 3 August 2021) and Google Scholar (https://scholar.google.com/, accessed on 18 June 2021) for peer reviewed journal articles published since 1980.
Literature/reports published by the industry, nonprofit organizations, and government organizations were also considered.
We used a different combination of keywords such as AI and ML application in: biodiversity conservation, wildlife conservation, forestry, illegal logging, plant inventory and identification, forest classification and mapping, wildlife identification and monitoring, forest restoration and conservation, above-ground carbon stock, forest health and phenology monitoring, detecting, and predicting anthropogenic threat to forest, etc.
The initial search yielded 900 peer-reviewed studies after removing duplicates (300 studies), of which we excluded 628 studies by reading title and abstract, as they did not qualify the objective of our study.
We reviewed full texts of the remaining 272 publications to find studies that reported application of AI and ML in forest management and their related services across the globe and in India.
We only included studies that reported application of AI and ML at least in one of the areas related to forestry, biodiversity research, and conservation as mentioned in Table S1.
We gave priority to primary studies to avoid the duplication.
Following the mentioned search and criteria for literature selection, we finally selected 172 studies to include in the review.
Additionally, we also collected data on AI-based startups and non-profits in forestry, and biodiversity conservation from published reports, literature, blogs, and from google search.
Results and Discussion 3.1. Global Overview of AI Research and Application in Biodiversity Conservation and the Forest Sector One of the main pre-requisites for developing and applying AI in any field is access to high-volume and high-quality datasets, network infrastructure of the Internet-of-Things (IoT), advanced technology (high resolution camera, satellite technology, sensors, drones, and unnamed aerial vehicles (UAVs)), and computational space and storage.
Access to a combination of these requirements has motivated AI application research in many domains of biodiversity conservation and forestry, ranging from forest inventory and detecting illegal wildlife and timber trafficking and felling [6,26,27] (Figure 1 and Table S1).
Further, these research efforts have revolutionized real-time application of AI technology in biodiversity conservation [28,29,30] and forestry sectors [9,10,31], as indicated by an increasing number of related AI-technology-based start-ups (Table S2).
Sustainability 14 07154 g001 550 Figure 1.
The overview of artificial intelligence application in forest and wildlife sector.
Refer to Table S1 for details and reference related to respective sector 3.3. The economic market for AI-based forestry start-ups.
3.2. The Growth of AI-Based Start-Ups and Non-Profits in Biodiversity Conservation and the Forest Sector Balancing preservation with sustainable utilization of forest resources is a daunting task, particularly given the lack of transparency and the persistent corruption in the forestry sector.
Unlawful practices such as illegal logging, deforestation and illegal timber trade have increased over time.
While technology cannot solve all the problems, it can certainly contribute to prevention of such unlawful practices, ultimately improving transparency in the forestry sector and even helping tackle climate change through sustainable practices.
In the following section, we describe economic markets for AI applications in the forestry sector and how such economic growth has led to a number of promising AI technology start-ups and non-profits all over the globe, that aim to digitize forests, improve forest management [7,32,33,34], combat rising levels of CO2 [35,36,37,38], protect endangered animal species [39,40], prevent wildlife trafficking and illegal trading [41,42,43,44], help in wildlife census and monitoring [27,45,46,47], and automate taxonomic identification and classification of animals and plants, ect.
[48,49,50,51,52,53] by embracing digital advancements (Table S2).
AI applications in the forestry sector are expected to significantly contribute to the global economy primarily through the precision forestry market which was worth USD 3.9 billion in 2019 and is projected to reach USD 6.1 billion by 2024.
The major drivers of the precision forestry market are increasing mechanization in emerging countries of Europe, Asia Pacific, and Africa for logging operations, rising construction activities, growing demand for timber from sawmills, decreasing cost of forestry mapping technologies, and advanced monitoring and surveillance technologies, as well as the push to drive prevention of illegal logging and deforestation, and increase government support towards digitalization of forest resources.
Additionally, the AI technology market in inventory and logistics management, fire detection, digital mapping of forest for biomass, and carbon and timber resources is also expected to grow in the coming years.
Such promising AI technology market growth relevant to the forestry sector has encouraged multiple start-up companies and non-profits to use AI-powered technology to tackle a wide range of problems such as detecting anthropogenic threats to the forest (deforestation, illegal felling), hazard assessment and prediction (fire, pest, and disease prediction and detection; predicting storm and flood damage to forest), restoration and reforestation, forest resource quantification and mapping (forest classification, estimating forest cover in real time, estimating carbon stock, and biomass and timber resource), tracking illegal wood trafficking, and monitoring forest health and phenology (Table S2).
Most of these starts-ups and non-profits are located in developed countries such as the USA, Europe, Canada, Australia, and South Africa.
Except Brazil, most developing countries which hold biodiversity-rich tropical forests are very slow in adoption of AI technology (Table S2).
3.3. AI and ML Application in Managing Forests and Their Resources, and Biodiversity Conservation 3.3.1. Addressing Challenges of Deforestation and Illegal Felling AI and machine learning algorithms coupled with spatial analysis have been used to predict and monitor deforestation rates across the globe [54,55,56,57,58,59].
For instance, Rainforest Connection (https://rfcx.org/, accessed on 26 June 2021) is working to address the challenge of deforestation.
The company is using old, discarded cellphones, powering them with solar power, and installing them on the treetops to record chainsaw sounds from the forest.
These recordings/data are sent to cellphone towers and then to the base station where Google’s AI and machine learning library called TensorFlow is used to identify and detect chainsaw noise over others.
Once identified, this information along with location information of installed sensors is then shared with forest managers so that further due diligence can be carried out to identify and stop illegal tree felling.
Similarly, other startup companies and non-profits such as Outland Analytics, Terramonitor, Global Forest Watch, and Future Forest Map project also make use of open-source satellite data and AI technology to map and monitor deforestation in real time.
For example, Outland analytics makes use of audio recognition AI algorithms to detect chainsaw sounds or unauthorized vehicles and sends real-time alerts via email to officials to efficiently manage environmental crime.
Terramonitor and Satelligence use a database of satellite images collected every day by multiple satellites and AI to create low-cost satellite data for natural area management and to monitor deforestation and forest health in real time (Table S2).
The World Resources Institute in collaboration with Central Africa Regional Program for the Environment (CARPE) used spatial modeling and AI to understand what factors influence deforestation in the Democratic Republic of Congo and to map where future forest loss is most likely to occur.
Their analysis suggests that human presence factors such as shifting cultivation, and the presence of roads, had highest influence on forest loss followed by climatic variable precipitation.
Further, analysis suggested that forests near to farmland are most vulnerable to deforestation.
Their study can help DRC authorities to proactively make land use decisions that shift development pressure away from high-value forests.
3.3.2. Forest Inventory, Mapping, Carbon, and Biomass Estimation Various startups are also making use of openly available and proprietary high-resolution satellite imageries and combining them with various other datasets to produce highly detailed maps of forests and landcover [60,61,62,63].
For example, SilviaTerra combines openly available high-resolution satellite imagery with field survey data from the US forest department to develop a predictive model that estimates forest conditions at a 15 m × 15 m resolution.
The data contains information about tree height, type, and diameter, for example, which is being used by various timber and conservation organizations for guiding their plans (https://silviaterra.com/bark/index.html, accessed on 26 June 2021).
Chesapeake Bay Conservancy teamed with Esri, and the Microsoft Azure team used machine learning libraries, to develop a highly detailed (one square meter resolution) landcover map of the region (https://chesapeakeconservancy.org/, accessed on 26 June 2021).
Now, that the algorithm and mechanics are available, with some modification, to develop a detailed landcover map either for the entire US or other parts of the globe.
20tree.AI, a start-up in Portugal, made use of remote sensing, big data, cloud computing, and artificial intelligence for real-time forest inventory and monitoring.
The Finnish forest center makes use of GIS data, imagery sources, climate and weather data, and AI for accurate measurements of forest stands and to better predict forest inventory.
Similarly, CollectiveCrunch a for-profit company based in Germany and Finland has developed an AI platform dubbed as “Linda Forest”, that predicts wood mass, wood species, and wood quality of target areas far more accurate than any existing conventional methods.
Linda Forest uses multiple sources of data, such as VHR2 image of Europe from the Copernicus Land Monitoring Service, Sentinel-2 images for growth modeling, and Copernicus Climate Change Reanalysis data for microclimate modeling and growth predictions, to accurately estimate wood mass and wood quality in standing forest of the target area.
Using this information, companies can then estimate resource-efficient production and consumption of wood products.
Deforestation and forest degradation account for approximately 11% of carbon emissions, more than the entire global transportation sector and second only to the energy sector.
Reducing emissions from deforestation and forest degradation (REDD+) is a mechanism developed by Parties to the United Nations Framework Convention on Climate Change (UNFCCC).
It creates a financial value for the carbon stored in forests by offering incentives for developing countries to reduce emissions from forested lands and invest in low-carbon paths to sustainable development.
However, designing effective REDD+ policies, assessing their GHG impact, and linking them with the corresponding payments, is a resource-intensive and complex task.
AI and machine learning techniques have shown a high potential in mapping and monitoring CO2 stock and other ecosystem services in forests [35,36,37,38].
Start-ups such as GainForest and Panchama make use of AI technology to solve such complex tasks.
GainForest uses large amounts of unlabeled satellite imagery, a video prediction model, game theory, and machine-learning-based Measurement, Reporting, and Verification (MRV) processes to monitor and forecast deforestation and design carbon payment schemes.
Similarly, Panchama uses machine learning on a combination of satellite, drone, and lidar images to precisely estimate individual tree size, volume, and carbon density.
Non-profit collaboration such as for Erol Foundation, the Center for Global Discovery, and Conservation Science (GDCS) at ASU and non-profit Planet.Inc use computer vision models, LiDAR, and satellite imagery at 3–5 m resolution for automatic and cost-effective direct measurement and mapping of carbon stock and emission at high resolution and high frequency in the Peruvian forest.
3.3.3. Automated Reforestation and Afforestation Another example of AI application is reforestation of recently deforested areas that can promote the planting of 1.2 trillion more trees on the planet [64].
This has the potential to absorb CO2 from the atmosphere in the order of hundreds of gigatons [64].
Three start-ups, Droneseed, Dendra, and Land Life, are creating products to address this challenge.
Droneseed is a company which has developed an innovative product called the seed vessel that carries seeds of desired species, helping to protect and germinate faster once planted.
The company deploys drone swarms and FAA heavy lift certified a group of four or five drones that carry weight of about 57 lbs, scan the study area to be planted to identify suitable conditions for planting-like moisture availability, and drop seed vessels.
This technology provides numerous advantages over manual reforestation method because it enables faster dispersal of seeds, and it can cover a larger area than planting by hand; most importantly, it also provides the ability to quickly monitor and measure the status of reforestation using drones.
As it provides a bird eye view, it also helps to identify exact locations of problematic areas where appropriate interventions could be done to achieve better results (https://www.droneseed.com/, accessed on 26 June 2021).
The Nature Conservancy’s Oregon chapter has teamed up with Droneseed to restore rangeland that was disturbed by invasive species in Oregon (https://uavcoach.com/droneseed-oregon/, accessed on 26 June 2021).
A similar start-up in UK called Dendra uses AI-based automation and digital intelligence to identify suitable planting areas to disperse seedpods filled with seeds of desired species and nutrients to support germination.
Land Life, a start-up in Amsterdam, uses multiple technologies such as GPS, satellite imagery, an automated driller, Cocoon (a seedling support technology), and AI technology for mass-scale reforestation and monitoring reforestation success.
3.3.4. Hazard Assessment and Prediction Another area where technological advances are bringing transformational changes to the forestry sector is through the collection of inventory data.
Such advances have led to novel ways of collecting and preparing highly accurate, high-resolution data that will significantly improve the way we are managing forests and conservation activities.
For example, a lot of data exists in paper format from past forest monitoring, which technologies like Optical Character Recognition (OCR) and Natural Language Processing (NLP) can digitize.
Once the data is available in digital format, they can be fed into several analytical algorithms for conducting analyses.
Internet-enabled sensors (Internet of Things devices), that can measure temperature, moisture, etc., when installed in forests, provide near-real-time information about forest activities and conditions.
Such data are being used to develop predictive models for identifying and getting insights into forest health and threats like deforestation [55,56,57,58,59], drought [65,66], wildfires [67,68,69], pests, diseases outbreak [70,71,72], soil health, storm damage, and other forest disturbances [71].
Terrafuse, a start-up in Canada, uses physics-enabled AI models to understand climate-related risk at the hyperlocal level.
Terrafuse leverages historical wildfire data, numerical simulations, and satellite imagery on Microsoft Azure to model wildfire risk for any location.
It also estimates temporal change in carbon density because of fire, deforestation, and other calamities.
Further, researchers in Columbia University are using AI technology to understand the effect of Hurricane Maria on Puerto Rico forests.
Researchers want to understand how tropical storms, which may worsen with climate change, affect the distribution of tree species in Puerto Rico.
In 2017, a NASA flyover of Puerto Rico yielded very high-resolution photographs of the tree canopies, using this images and AI technology, scientists hope to analyze which tree species were destroyed and which withstood the hurricane to predict patterns associated with future hurricanes.
3.3.5. Tracking Illegal Wood Trafficking The illegal timber trade is considered as lucrative as the illegal wildlife trade.
According to Interpol, the illegal timber trade is worth USD 50 billion to 150 billion annually.
The supply of illegal timber not only contributes to deforestation (leading to significant loss of carbon) but also threatens many rare tree species such as rosewood, dipterocarps and mahogany.
Illegal timber trade lowers global timber prices by 7 to 16%, costing source nations up to USD 5 billion as losses in annual revenue and providing a significant incentive for governments to act.
Thus, to protect forests from illegal felling and to guide legal timber use globally, there is a need for a system which can track illegal timber [73].
Timbeter is a start-up in Estonia, which uses the world’s largest database of photometric measurements of roundwood and AI for online tracking of roundwood to individual shipments and piles to fight illegal logging and timber trafficking.
Xylene, a start-up in Germany, uses a combination of space technology, blockchain and supply chain mapping, automatic data gathered by IoT devices, and Earth Observation and AI technology to track the wood supply chain in real-time.
3.3.6. Monitoring Ecosystem Health and Biodiversity Conservation The conservation community often seeks to promote forest characteristics that influence richness and diversity of fauna in the forest, making it critical to understand what interventions are successful, and AI technology is helping in such interventions [11,12,13,14].
Scientists from The Nature Conservancy and its partner organizations have developed a novel way of automated soundscape monitoring to evaluate the impact of conservation actions on biodiversity.
To understand how species respond to disturbances like recent deforestation or poaching, they developed tiny sound recorders and installed them across various locations in the forest.
They recorded sounds of the forest, referred to as a soundscape, which was then analyzed to identify various species sounds, and activity across various times of the day and various periods of the year.
They are developing a global platform to store such data from various efforts across the globe and provide analytical services to analyze these datasets to understand benefits of conservation interventions.
Such technology has various implications for understanding how species react to disturbance or benefit from interventions [13].
Classification of vibration patterns from oncoming trains using machine learning has also been used in providing early warning to wildlife in Banff National Park, Canada, where train strikes have been a major source of mortality for grizzly bears Ursus arctos horribilis [74].
By using such classifications to trigger sound and light-based alarms before trains reached the location, animals were found to leave the track 29–62% earlier than they would have otherwise done [74].
Apart from sound recognition, the widespread use of imagery in wildlife monitoring has led to a strong use-case for AI-based automation for identification of species [48,49,50,51,52,53] (Tables S1 and S2).
Imagery may be obtained, for example, through automated camera traps, which are triggered by heat and motion.
Millions of photographs or video clips may result from the widespread deployment of such devices.
Given the massive amount of data, this may make it challenging to analyze and extract data on species of conservation importance.
The application of AI to this problem can result in accurate species classification.
For example, in the Serengeti ecosystem, a community of 48 species was classified using such an approach [27].
Similar methods have also been applied in the identification of individual animals.
For example, the strip patterns of tigers, (Panthera tigris) have been used to identify individuals [75].
Based on this, Shi et al.
[76] developed a convolutional neural network (CNN) to identify individual tigers.
The ability to identify both species and individuals has important implications for monitoring biodiversity, but also in conservation applications such as mitigating human-wildlife conflict.
For example, farmers could be provided with early warning on the entry of elephants (Elephas maximus) into crop fields and villages by combining automated cameras with image analysis software.
Similarly, individual tigers that become habituated to humans, increasing risk of conflicts, can be identified using such systems.
A key requirement in implementing such systems in the field is rapid classification and information transfer, for this computation on the device itself is ideal but can be expensive to set up.
Further, the lack of mobile towers in remote forested areas can hamper information transfer.
3.3.7. Solving Supply and Demand Problem With rising global population, there is high demand for timber and non-timber forest products.
Therefore, the forestry sector, globally, is facing demand uncertainty, higher supply risk, and increasing competitive intensity.
Thus, there is a need for smart supply chain management to solve supply and demand problems in the forestry sector [77,78].
One area of AI’s potential application is the emerging management philosophy of supply chain management (SCM).
in Canada, for over 20 years, has been focusing on systematic technologies to solve demand and supply problems in the forestry sector with AI algorithms.
The aiTree has applied its typical application Forest Simulation Optimization System (FSOS) in British Columbia, Canada to solve demand and supply problems in the forestry sector.
The demands from a forest include wildlife habitat, biodiversity, water quality, visual quality, carbon storage, timber production, and economic contributions.
FSOS focuses on both “what we can take from the forest” and “what we can create in the forest”.
Forest design is a complicated problem because the trees are growing and dying, and all the values must be considered every year for over 400 years.
FSOS is a good example that uses AI, big data, and cloud computing technologies to solve the complicated demand and supply problems.
3.3.8. Forest Hydrology One of the most critical aspects of forest management is understanding its linkages with watershed/forest hydrology, as it drives nutrient cycling, precipitation inputs, and surface and subsurface flow networks that support forest growth and downstream water quality [79].
With improvements in technologies such as high-performance sensors, smart phones, autonomous vehicles, remote sensing, and GIS, increasing volume and complexity of data on ecohydrological parameters are being collected.
Tools such as AI and ML are being applied in the field of ecohydrology, including forest hydrology, to fully realize the potential of these data and obtain new insights into ecohydrological processes [80].
For instance, AI/ML methods have been used to estimate and model precipitation interception by forest canopies [81,82], canopy water content [83], spatiotemporal behavior of soil moisture in vegetated areas [84,85,86], global [87] and regional [88] terrestrial evapotranspiration, water-use efficiency in terrestrial ecosystems [89], vegetation water storage [90], terrestrial/groundwater storage [91] using vegetation cover as an indicator [92], and plant water stress [93].
The recent growth of big hydrologic data through remote sensing and data compilation has also fostered the adoption of ML in land surface modeling which simulates land surface processes including partitioning of water between land and atmosphere, such as in groundwater dynamics [94].
Big data and AI/ML have been increasingly used to predict extreme geoclimatic events such as droughts, floods, and landslides [95], which have direct implications for forest management.
More recently, efforts are being made to improve prediction of terrestrial ecohydrological extremes (TEE) (e.g., the extremes of evapotranspiration, soil moisture, streamflow, and terrestrial water storage) at seasonal to decadal scales using AI-based integrated modeling [96].
Taken altogether, these advances in technology, data interpretation, and modeling are slowly transforming our ability to understand forest and watershed hydrology [97] and have important policy and management implications [80].
Use of AI/ML methods for forest hydrology, however, seem to be limited to scientific research and are yet to be applied for conservation and management at a large scale.
These methods have a tremendous potential for better decision support in forest hydrology management.
3.3.9. Aquatic and Marine Biodiversity and Water Resource Conservation Artificial intelligence (AI) applications in aquatic and marine biodiversity and water resource optimize the conservation of aquatic and marine flora and fauna and water resources and attracted significant reserch attention since last decade.
For instance, AI and ML models have been used to predict stream flow [98,99,100,101,102,103], water quality [104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125], water pollution and toxicology [126,127,128,129,130,131,132], aquatic and marine biodiversity diversity prediction and extinction [133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149], predicting species distribution and habitat mapping [150,151,152,153,154,155,156,157,158,159,160,161,162,163,164], and marine and aquatic species recognition and classification [165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183].
Above mentioned AI research in aquatic and marine biodiversity and water resource conservation highlight that AI will be key to developing new technology to uncover new aspects of conservation and potential threats to aquatic and marine ecosystems’ structures and functions, thereby informing effective monitoring and conservation of aquatic and marine biodiversity and managing water resources.
This new knowledge will directly address several of the key challenges identified for the aquatic and marine ecosystems, from effective water resource management and biodiversity conservation, to creating a digital representation of the freshwater and ocean ecosystems and delivering data, knowledge, and technology to all.
3.4. Status of Indian Forests and Need of AI Technology Indian forests are an important defining feature of the country’s landscape that hold both cultural and biological importance [184].
India’s wide range of climate, geography, and culture is unique among biodiversity-rich nations and is known for its diverse forest ecosystems and megabiodiversity.
It ranks as the 10th most forested nation in the world [19] with 24.56% (81Mha) of its geographical area under forest and tree cover [185].
Out of 34 global biodiversity “hot spots,” four are located in India, namely, the eastern and north-eastern Himalayas, Indo-Burma (North-east India), Sundaland, and Western Ghats [186].
Being one of the 17 megadiverse countries, with only 2.4% of global land area, India accounts for 7 to 8% of recorded species in the world [98].
In addition, Indian forests provide many ecosystem services and livelihoods to people.
Approximately 275 million people of India live in the fringes of forest and earn the bulk of their livelihood from forests [187].
It is estimated that Indian forests sequester 5.84–7.39 Gt of carbon every year [188].
Despite their cultural, economic, and ecological importance, Indian forests face many adverse challenges.
About 85% of forest area is publicly owned and 15% privately owned [19].
Most of the public forests are administered by the government, and some of them by communities and indigenous groups, and only around 27% of publicly owned forest is protected in 2019, compared to 31.63% in 2003.
Further, 14% of tree cover assumes unclassified status (Table 1), indicating that Indian forests suffer from low protection status.
Of the approximately 81 Mha of forest, 9928 Mha are dense primary forests, 30.847 Mha are moderately dense forests, 40,775 Mha are open forests, and 9503 Mha consists of agroforestry, social forestry, and plantations [185].
The forest cover data from 2003 to 2019 suggests that there is a consistent increasing trend in open forest and a decrease of dense forest cover with the gain of 1,917 Mha of open forest and loss of 2599 Mha of moderately dense forest (Table 1), indicating a continuous degradation of dense forest in India.
Further, Indian forests suffer from low growing stock.
The data from 2003 to 2019 suggest that there is an loss of 507,944 million cubic meters of growing stock in forests, whereas trees outside forests show a gain of 0.61 million cubic meter, suggesting that Indian forests are poorly managed (Table 1).
Illegal logging and trade of high-value timber is a major problem in many parts of the country.
In 2009, the Ministry of Environment and Forests estimated that 2 million m3 of logs were illegally felled per year.
Underlying this logging are several uncertainties relating to legal rights to harvest, tax, perform timber harvesting activities, third parties’ rights, and trade and transport.
As India is one of the world’s largest importers of wood-based products, it is also a major consumer of illegal timber.
The volume of illegal imports has increased, and in 2012, almost 20% of timber imports were estimated to be illegal [189].
India’s population and economic growth in the last several years has raised several concerns in terms of its present and future resource demands for timber and non-timber material and energy needs from the forest.
With 18% of global livestock and 17% of the human population on 2.4% of the world’s land area, the Indian forest faces immense biotic pressure.
Around 30% of fodder needs for cattle and 40% of domestic fuel wood needs directly come from these forests.
Despite protection status, 87% of national parks experience grazing.
Further, in eastern and northeastern India, around 1.2 Mha of forest land is under shifting cultivation.
Therefore, there is high anthropogenic and other biotic pressure on Indian forests.
Moreover, the Indian forest sector still depends on resource-intensive and time-consuming traditional forestry practices to manage and protect forests.
Compared to the wildlife sector, the forestry sector in India has been slow in adapting innovative technology, which can bring transformative change in conservation and management of forests and their resources.
While these challenges persist in the Indian forest sector, they coincide with an era in which there is unprecedented innovation and technological change.
The rapid advancement in AI technology supported by the Internet of Things (IoT), open-source big data, unmanned aerial vehicles (UAVs), high-resolution satellite images, sensors, and cheaper computing, is a boon to the Indian forestry sector for solving many of its challenges.
Given the similar nature of problems plaguing tropical forests globally and in India (such as deforestation, encroachment for farming, forest degradation to extract timber and non-timber resources, illegal logging, illegal timber import and export, and inefficient supply chain management), AI technologies being developed for the forestry sectors in other countries and related learnings can also be applied for improving forest management in India (Table S2).
Status of forest in India from 2003 to 2019.
Table 3.5. Barriers to Adoption of AI-Based Systems for India’s Forests and Biodiversity Conservation 3.5.1. Inadequate Awareness There is often a lack of awareness among stakeholders (such as forest managers, policymakers, and civil society) on the availability and applicability of technologies.
This is partly due to the inherent complexity of these new technologies, which may lead to disinterest.
On the other hand, the use of terms such as artificial intelligence may also create unrealistic expectations for solutions.
Therefore, building the capacity of stakeholders on the appropriate use of these technologies is an important step in applying them in the field.
Strong case studies and pilot demonstrations are important in building both understanding and realistic expectations.
3.5.2. Lack of Ethical Standards and Safeguards The use of technologies such as AI brings with it several possibilities for misuse.
When using such technologies in areas with particularly vulnerable communities, such as indigenous groups or forest-dependent communities, safeguards need to be especially strong.
Concepts such as free, prior, and informed consent, data security, and permitted applications need to be defined and followed.
Such standards also need to be accompanied by capacity development of communities in areas where such technologies are deployed, to ensure equity in outcomes.
3.5.3. Limited Suitability to Harsh Field Conditions Technologies that are implemented under the harsh conditions of the field need to be robust enough to function over meaningful timeframes.
Climatic and weather conditions, animal damage, and vandalism are key challenges for such technologies.
Inadequate planning for such conditions may lead to equipment failures, thereby also undermining trust in the concept itself.
Such planning is particularly important given the high capital and running costs of such technologies.
Further, inadequate supporting infrastructure in the field, such as unstable connectivity, may limit the reliability of equipment.
3.5.4. Limited Commercial Scalability Applications of AI in the forest sector in India are currently driven by enthusiasts and small startup companies.
The lack of a strong market limits the investments that can be made in the sector, in turn leading to inadequate scaling.
Further, the fragmentation of efforts among small competitors working on similar applications may hinder the large-scale economic development of AI technology.
Such limitations may also prevent the development of user-friendly interfaces, leading to AI models being deposited in repositories such as GitHub but not being used by practitioners.
3.6. Uncertainties Associated with AI Though, AI technology has potential applications in forestry and biodiversity conservation, it is increasingly important to evaluate the reliability and efficacy of AI and ML systems before they could be applied in practice.
Because the predictions made by AI and ML models may not be always reliable due to uncertainty associated with data and expert knowledge.
For example, the AI and ML algorithms will not be able to differentiate plantations from reforestation areas and natural forest, especially in a species-rich tropical forest, if there is no good number of labeled images of natural forest, plantations, and reforestation areas.
Thus, the reliability of output produced by AI and ML models depends on large amount of training and test data and expert knowledge.
Conclusions Globally, there is a need for forestry practices to contribute to sustainable development goals that attempt to conserve forests as carbon sinks and biodiversity habitats, and to sustain and cultivate forests as green infrastructure.
The emerging technological innovation to manage, monitor, and conserve the forest and its resources is helping the sector achieve sustainable development goals.
Globally, there is an increasing number of countries adapting smart forest and precision forestry techniques which make use of technological innovation in digital, satellite, sensors, and AI technology to manage, protect, and sustainably utilize forest resources.
However, adoption of these innovations is mostly limited to developed countries and a few developing countries where forest is managed for commercial purposes.
On the other hand, for countries like India, where forests are mostly managed for non-commercial purpose of biodiversity conservation, storing carbon, and benefiting rural livelihood, the adaption of innovative technologies in the forest sector has been slow.
Challenges or limitations, such as (1) the unavailability of better data or limited access to available big data, and (2) technical and computation challenges of using technologies like AI (e.g., accessibility to the wider community), have resulted in a limited application of these technologies in the Indian forest sector.
Therefore, to make technologies like AI more beneficial and accessible to the Indian forest sector, we suggest the following actions: Interdisciplinary collaborations between forestry practitioners, forest ecologists, conservation practitioners, forestry officials, academicians working in the forestry sector, and technologists will be important in facilitating long-term adoption of AI technology for forestry sector applications (for example, corporations like Microsoft and Google initiative’s “AI for earth innovation” bringing together researchers and conservationists to incorporate AI solutions into nature conservation by providing technical support, infrastructure, and training [190]), Cheap and cost-effective computational resources for both data analysis and storage (e.g., cheaper cloud-based options for online data analysis and storage) will have an advantage of minimal investment and hardware maintenance [191].
Continued expansion of data collection capabilities (for example, emerging technologies such as the wireless sensor networks, digital recording devices, drones and camera technology, and crowd-sourced data approaches like citizen science, development of algorithms to extract data from social media, and other online sources), and Development of computationally less intensive, fast processing algorithms to analyze big data.
Further, these developments will have tremendous potential to drive transformational changes in the way we manage our forests, biodiversity, and design appropriate conservation measures.
Supplementary Materials The following supporting information can be downloaded at https://www.mdpi.com/article/10.3390/su14127154/s1.
Table S1: Summary of AI and machine learning application research in biodiversity conservation and forest sector; Table S2: AI start-up companies and non-profits in biodiversity conservation and forest sector.
Author Contributions Conceptualization, K.N.S., S.M. and N.S.; methodology, K.N.S.; software, writing—original draft preparation, K.N.S., S.M., R.A., A.G. and N.S.; writing—review and editing, K.V., M.J. and J.M.K.; All authors have read and agreed to the published version of the manuscript.
Funding This research received no external funding.
Institutional Review Board Statement Not applicable.
Informed Consent Statement Not applicable.
Data Availability Statement No new data were created or analyzed in this study.
Data sharing was not applicable to this study.
Acknowledgments We greatly acknowledge the initial review of the manuscript by colleagues from Lands team—The Nature Conservancy Center, India.
Conflicts of Interest The authors declare no conflict of interest.
Abbreviations AI	Artificial intelligence ML	Machine learning CNN	Convolutional Neural Network FSI	Forest Survey of India FAO	Food and Agriculture Organization IoT	Internet of Things UAVs	Unmanned Aerial Vehicles GIS	Geographic Information System SCM	Supply Chain Management FSOS	Forest Simulation Optimization System UNFCCC	United Nations Framework Convention on Climate Change REDD+	Reducing Emissions from Deforestation and Forest Degradation CARPE	Central Africa Regional Program for the Environment NDCs	Nationally Determined Contributions DRC	Democratic Republic of Congo LiDAR	Light Detection and Ranging  AI AND THE ENVIRONMENT : TOWARD SUSTAINABLE DEVELOPMENT AND CONSERVATION Abu Rayhan1 In the midst of escalating environmental challenges, artificial intelligence (AI) has emerged as a powerful tool for tackling sustainability and conservation issues.
This research article explores the multifaceted role of AI in environmental conservation and sustainable development.
Through a comprehensive analysis of various AI applications, from remote sensing and wildlife protection to climate change prediction, this narrative seeks to shed light on how AI can revolutionize our approach to safeguarding the environment.
Addressing the ethical, technical, and policy-related challenges associated with AI, this article emphasizes the need for responsible development and application of AI technologies.
Drawing from success stories and case studies, the narrative paints a promising picture of AI's potential in shaping a sustainable future for humanity and the planet.
Keywords: Artificial Intelligence, Environment, Sustainable Development, Conservation, Remote Sensing, Wildlife Protection, Climate Change, Ethics, Policy.
Background on the increasing environmental challenges faced by humanity The current era stands witness to unprecedented environmental crises, marked by climate change, biodiversity loss, deforestation, and pollution.
Human activities have taken a toll on the delicate balance of the Earth's ecosystems, with consequences that reverberate across the globe.
The magnitude of these challenges necessitates innovative and transformative solutions to ensure a sustainable future for generations to come.
The role of artificial intelligence in addressing environmental issues Amidst these challenges, artificial intelligence has emerged as a technological marvel that holds immense promise for environmental conservation.
AI's ability to process vast amounts of data, learn from patterns, and make informed decisions in real-time presents an unparalleled opportunity to revolutionize our approach to environmental protection and sustainable development.
Purpose of the research article The purpose of this research article is to comprehensively explore the manifold applications of AI in environmental conservation.
From harnessing AI for remote sensing and wildlife protection to its pivotal role in climate change prediction and adaptation, we aim to elucidate the transformative potential of AI in safeguarding our planet's natural resources.
Furthermore, we will delve into the challenges and ethical considerations associated with AI  deployment, paving the way for responsible development and policy frameworks.
AI APPLICATIONS IN ENVIRONMENTAL A.
Remote Sensing and Earth Observation 1.
Use of AI for analyzing satellite data to monitor environmental changes Satellite imagery offers an unprecedented view of the Earth's surface, providing invaluable data for environmental monitoring.
However, the sheer volume of data generated requires sophisticated processing capabilities to detect meaningful patterns.
AI algorithms, such as convolutional neural networks (CNNs), excel in extracting information from satellite images, enabling the detection of deforestation, habitat loss, and land degradation with unprecedented accuracy.
Applications in detecting deforestation, habitat loss, and land degradation AI-powered remote sensing tools enable near-real-time monitoring of critical environmental indicators.
By continuously analyzing changes in vegetation cover, forest density, and land use, AI-driven systems can promptly detect illegal logging, encroachments, and unsustainable agricultural practices.
This early warning capability empowers conservationists and policymakers to respond swiftly to emerging threats, fostering a proactive approach to environmental preservation.
Wildlife Protection and Conservation 1.
AI-driven monitoring systems for tracking endangered species The plight of endangered species necessitates comprehensive monitoring to prevent their extinction.
Traditional methods of tracking wildlife can be laborintensive, expensive, and limited in scope.
AI, however, has revolutionized wildlife conservation through its application in camera trap image analysis, acoustic monitoring, and GPS tracking.
By identifying individual animals, estimating population sizes, and monitoring migration patterns, AI augments conservation efforts by providing invaluable insights into species behavior and habitat usage.
Applications in preventing poaching and illegal wildlife trade Poaching and illegal wildlife trade pose severe threats to endangered species and their habitats.
AI technologies, such as machine vision and natural language processing, can analyze vast amounts of online content to identify and combat illegal wildlife trade networks.
Furthermore, AIdriven surveillance systems equipped with facial recognition capabilities can aid law enforcement in apprehending poachers and traffickers, acting as a deterrent to illicit activities.
Climate Change and Weather Prediction 1.
AI models for climate modeling and predicting extreme weather events Climate change remains one of the most pressing global challenges, impacting ecosystems, human societies, and economic activities.
AI-powered climate models have demonstrated their potential to enhance our understanding of complex climate processes and improve the accuracy of long-term climate predictions.
Additionally, AI-driven algorithms enable the identification of trends and patterns in historical climate data, facilitating the projection of future scenarios and informing policymakers about potential risks and vulnerabilities.
Applications in climate change adaptation and mitigation strategies AI's analytical prowess empowers decision-makers to devise targeted climate change adaptation and mitigation strategies.
From optimizing energy consumption and carbon emissions reduction to designing resilient infrastructure, AI-guided solutions play a pivotal role in building climate resilience at both local and global scales.
Furthermore, AI technologies can help in developing efficient renewable energy systems, contributing to a sustainable transition away from fossil fuels.
Smart Cities and Urban Planning 1.
AI-driven solutions for optimizing energy consumption and transportation As the world's population gravitates towards urban centers, the concept of smart cities gains momentum.
AI  technologies play a central role in transforming urban living by optimizing energy consumption, traffic flow, and public transportation systems.
Smart grids, enabled by AI, allow for real-time monitoring and control of energy distribution, reducing waste and promoting the integration of renewable energy sources.
Applications in waste management and urban sustainability The proliferation of AI-driven waste management systems contributes to minimizing the environmental impact of urban areas.
AI-powered waste collection and recycling algorithms enhance efficiency and reduce costs by optimizing waste collection routes and sorting processes.
Additionally, AI-driven urban planning models enable the design of sustainable and resilient cities, considering factors such as green spaces, public amenities, and infrastructure optimization.
Renewable Energy and Resource Management 1.
AI's role in improving the efficiency of renewable energy systems The transition to renewable energy sources is crucial for curbing greenhouse gas emissions and combatting climate change.
AI's ability to analyze complex energy data and optimize renewable energy systems has propelled the development of more efficient solar panels, wind turbines, and energy storage technologies.
These advancements make renewable energy more economically viable and accessible, accelerating the global transition to clean energy.
Applications in optimizing resource allocation and reducing waste Inefficient resource management contributes significantly to environmental degradation.
AI algorithms can analyze data on resource usage, supply chains, and consumption patterns, enabling organizations to optimize resource allocation and reduce waste.
This optimization extends across various sectors, from agriculture and manufacturing to water management and recycling, fostering sustainability and ecological balance.
Precision Agriculture and Sustainable Food Production 1.
AI applications in optimizing agricultural practices and minimizing environmental impact Feeding a growing global population while minimizing the environmental footprint of agriculture is a formidable challenge.
AI-driven precision agriculture offers a solution by combining data from sensors, satellites, and drones to create a granular understanding of soil conditions, crop health, and water usage.
AI-powered insights facilitate precision nutrient application, smart irrigation, and pest management, promoting sustainable and efficient agricultural practices.
Role of AI in ensuring food security and reducing food waste Food waste poses a considerable strain on the environment and global food security.
AI's predictive capabilities enable real-time monitoring of supply chains, facilitating timely interventions to prevent food spoilage and loss.
Furthermore, AI algorithms can analyze consumer  behavior patterns and optimize inventory management, reducing food waste at retail and consumer levels.
CHALLENGES AND LIMITATIONS OF AI IN A.
Ethical Concerns and Bias 1.
Addressing ethical considerations in AI applications for conservation The increasing reliance on AI in environmental conservation raises ethical questions regarding the use of data, potential infringements on privacy, and the impact on local communities.
Transparent and ethical frameworks must govern data collection, storage, and utilization to ensure that AI-driven initiatives align with conservation goals and respect human rights.
Mitigating biases in data and algorithms to ensure equitable outcomes AI algorithms are inherently influenced by the data they are trained on, making them susceptible to biases.
In the context of environmental conservation, biased data can lead to unfair decision-making and exacerbate existing environmental inequalities.
Addressing and mitigating biases in AI models is essential to ensure equitable and just conservation outcomes.
Data Availability and Quality 1.
Challenges in accessing and processing environmental data AI's effectiveness in environmental conservation relies heavily on the availability and quality of environmental data.
However, data accessibility and interoperability pose significant challenges, particularly in remote and underresourced regions.
Collaborative efforts are needed to ensure data sharing and open access to facilitate widespread AI applications for conservation.
Strategies for improving data collection and sharing To overcome data-related obstacles, partnerships between governments, non-governmental organizations, and private entities are crucial.
Investing in innovative data collection methods, such as citizen science initiatives and crowdsourcing, can bolster environmental datasets and provide valuable inputs for AI-driven conservation efforts.
Policy and Governance 1.
Regulatory frameworks for responsible AI use in environmental contexts The rapid pace of AI development has outpaced the establishment of robust regulatory frameworks.
Policymakers must proactively address the ethical, social, and environmental implications of AI in conservation.
Building on existing privacy and data protection laws, specific regulations for AI applications in environmental contexts can promote responsible and transparent deployment.
Addressing legal and policy challenges for AI-driven conservation efforts National and international collaboration is vital to tackle cross-border conservation challenges effectively.
Harmonizing legal and policy frameworks across regions can facilitate seamless cooperation and data sharing, fostering global efforts in preserving biodiversity and combating climate change.
Examples of successful AI applications in environmental conservation 1.
AI-Powered Anti-Poaching Efforts in Africa In Kenya's Maasai Mara National Reserve, AI-driven surveillance systems have significantly reduced poaching incidents.
Smart camera traps equipped with AI algorithms can distinguish between animals and humans, alerting rangers in real-time when potential threats are detected.
This proactive approach has led to a decline in poaching activities, safeguarding endangered species like elephants and rhinos.
AI-Based Climate Change Adaptation in Bangladesh Bangladesh, prone to climate-related disasters like cyclones and floods, has adopted AI-based early warning systems.
AI algorithms process meteorological data, historical patterns, and satellite imagery to predict extreme weather events.
The timely warnings enable authorities to evacuate vulnerable communities, saving lives and reducing the impact of natural disasters.
Impact assessment and benefits of AI-driven solutions 1.
Positive Environmental Outcomes in the Amazon Rainforest AI-powered satellite monitoring in the Amazon Rainforest has aided in identifying and combatting illegal deforestation activities.
By detecting forest clearing in realtime, law enforcement agencies and environmental organizations can take immediate action, preventing further destruction and conserving this critical ecosystem.
Improved Agricultural Yields and Sustainability AI-guided precision agriculture practices have led to significant increases in crop yields while reducing the use of fertilizers and pesticides.
This sustainable approach benefits both farmers and the environment by optimizing resource usage, conserving water, and minimizing agricultural runoff.
Lessons learned from the implementation of AI in conservation projects 1.
Data Collaboration and Knowledge Sharing Successful AI-driven conservation projects underscore the importance of collaboration between researchers, conservationists, and local communities.
By sharing data and knowledge, stakeholders can collectively develop effective AI solutions tailored to local contexts, maximizing their impact on conservation efforts.
Interdisciplinary Approaches The integration of diverse disciplines, such as environmental science, computer science, and social  sciences, is essential for unlocking AI's full potential in environmental conservation.
Bringing together experts from various fields fosters innovation and ensures that AI solutions are contextually relevant and ethically sound.
THE FUTURE OF AI IN ENVIRONMENTAL A.
Opportunities for further integration and advancement of AI technologies The future holds tremendous promise for AI's impact on environmental conservation.
Advancements in AI algorithms, coupled with the increasing availability of environmental data, will enable more precise and proactive conservation efforts.
As AI technologies become more accessible, their application in conservation will expand, empowering individuals, communities, and organizations worldwide to play an active role in safeguarding the environment.
Potential collaborations and partnerships to enhance AI applications in conservation Collaboration between academia, industry, governments, and non-governmental organizations will be instrumental in advancing AI applications in conservation.
Publicprivate partnerships can facilitate technology transfer and capacity building in regions with limited resources, ensuring that AI-driven solutions reach the communities that need them most.
Speculation on AI's role in shaping the future of sustainable development As AI continues to evolve, its potential to influence sustainable development on a global scale becomes increasingly apparent.
AI's ability to optimize resource usage, design resilient infrastructure, and predict environmental trends will catalyze sustainable development efforts, contributing to a greener, more inclusive future for humanity.
The transformative power of AI in environmental conservation is evident in its diverse applications, from remote sensing and wildlife protection to climate change prediction and adaptation.
Despite challenges in ethics, data accessibility, and policy, the responsible development and deployment of AI offer unparalleled opportunities to address pressing environmental issues.
Harnessing the potential of AI requires collective efforts from governments, organizations, and individuals to foster innovation, data collaboration, and knowledge sharing.
By embracing interdisciplinary approaches and integrating AI technologies into conservation strategies, we can pave the way for a sustainable future that harmonizes human development with the preservation of our planet's rich biodiversity and natural resources.
Responsible and ethical AI deployment holds the key to unlocking a future where humanity and nature thrive together in harmony.
Highlights Following a horizon scan methodology with a panel of 27 conservation scientists and artificial intelligence (AI) experts, 21 ideas likely to significantly impact on the success of global biodiversity conservation were identified from a long list of 104.
Our 21 issues include novel interpretation of image and audio data, digital twins for ecosystems, improving species distribution models, and AI-powered conservation advisors.
We believe that adoption of AI in conservation will lead to beneficial outcomes for conservation effectiveness and improve our understanding of the natural world.
However, it is not a panacea, and will not wholly replace established conservation techniques, education, and on-the-ground research.
Moreover, careful and creative measures must be taken to ensure equitable access, development, and deployment.
Abstract Artificial Intelligence (AI) is an emerging tool that could be leveraged to identify the effective conservation solutions demanded by the urgent biodiversity crisis.
We present the results of our horizon scan of AI applications likely to significantly benefit biological conservation.
An international panel of conservation scientists and AI experts identified 21 key ideas.
These included species recognition to uncover 'dark diversity', multimodal models to improve biodiversity loss predictions, monitoring wildlife trade, and addressing human–wildlife conflict.
We consider the potential negative impacts of AI adoption, such as AI colonialism and loss of essential conservation skills, and suggest how the conservation field might adapt to harness the benefits of AI while mitigating its risks.
Keywords artificial intelligence machine learning conservation biodiversity Delphi The intersection between conservation and AI Biological conservation science is concerned with understanding the causes and consequences of biodiversity loss, and developing and testing solutions to halt and reverse that loss.
Given the urgency of the biodiversity crisis [1], more effective solutions are rapidly required.
Biodiversity is complex and multifaceted [2], meaning that understanding status and trends often requires processing large quantities of data, which are time-consuming to collect and analyze.
In addition, conservation operates in a coupled human and natural system in which there are complex feedbacks between social and ecological components [3] that can be difficult to fully understand and model accurately [4], obstructing decision-making.
One hope of lifting these barriers is to look to methods of artificial intelligence (AI, see Glossary) which have been transformative in many domains such as healthcare [5] and international security [6].
The key to this success has been the use of machine learning (ML) which, given sufficient data, can demonstrate high predictive performance on tasks where good mathematical models are lacking [7].
Even in scientific areas that do rely on well-understood mathematical models, such as weather forecasting, ML can often increase modeling performance at reduced computational cost [8].
Decades of systematic and opportunistic data collection by ecologists and conservation scientists (whether using citizen/community science, expert, or remote sensing approaches) have provided a wealth of data, much of which is underutilized [9].
Moreover, the increasing availability of novel sensors (e.g., for remote sensing, biotelemetry, and biologging) and hardware (including smart phones) for conservation applications has led to the rapid accumulation of new data, and analytical tools to keep pace with these advances are required.
Combining these data with the power of AI represents a potentially revolutionizing force to increase the effectiveness of conservation approaches, and thus accelerate efforts to the levels necessary to meet the targets in the recently agreed Kunming–Montreal Global Biodiversity Framework [10].
Public interest in AI has exploded in recent years, and platforms such as ChatGPT and Midjourney have captured our imaginations through their generation of human-like text and image content.
However, AI is not a novel topic in scientific research and has been adopted by researchers in some form for decades [11].
Nonetheless, the rapid investment in AI within academic and industrial research has irrevocably altered the scientific landscape.
The functions of AI in scientific understanding can be outlined as follows [12].
(i)	 Providing information through advanced simulation and data representation, that cannot be obtained through experimentation, to reveal properties of a physical system that are otherwise difficult or even impossible to probe.
In conservation, AI systems are making a rapidly growing contribution to providing better information and, in some cases, more effective actions such as 'Skylight.global' – which identifies illegal and unreported fishing in near real time from satellite datai.
(ii)	 Providing information that expands the scope of human imagination or creativity, such as identifying surprises in data, models, and the literature.
Recent projects allow researchers to automatically gain ecological and animal behavioral insights from audioii and image dataiii.
AI technology is also helping to model species distributions from partial observations [13].
(iii)	 Providing insights to human experts by translating observations into new knowledge.
Platforms such as CAPTAIN [14] take the first steps to allow policymakers to identify optimal areas for protection to preserve species and habitats.
These advances not only improve current practices in conservation (e.g., by improving methods for monitoring trends in species, habitats, and threats) but also open completely novel areas for R&D.
However, new technology also brings challenges.
There is growing awareness that the deployment of wildlife monitoring technologies might have unintended consequences and could potentially undermine conservation efforts [15], and wider use of drones, audio recording, camera traps, and electronic tagging and tracking tools brings risks of misuse by bad actors.
There are also justifiable concerns about the energy-use requirements of AI [16] and the way in which use of AI could aggravate existing inequalities and biases [17].
Furthermore, current large language models (LLMs) can 'hallucinate' – generating inaccurate or nonsensical outputs which are presented as fact.
The aim of this paper is to identify the key areas where AI can help to improve the effectiveness of conservation, as revealed through a horizon scan methodology in consultation with both conservation and AI experts, as well as to reflect on the challenges remaining to ensure that this powerful emerging technology is a force for good in improving the effectiveness of conservation.
Recent developments in AI and machine learning The potential for AI methods to process and analyze large datasets, identify subtle patterns, and generate novel insights offers promising opportunities for conservation and ecology [18].
An overview of AI and ML is available in Box 1.
Much of the media excitement in recent years has been the promise of LLMs and generative models.
These have been shown to be generalizable even with no additional training data for a given task (zero shot learning) [19] and can also reduce the cost of training new models across a wide range of domains through fine-tuning or transfer learning.
LLMs in particular have seen rapid adoption through chat interfaces such as ChatGPTiv and assistive copilots such as Github Copilotv.
Further, their reasoning capabilities are starting to be used to drive AI agents [20] that can sense their environment, make decisions, and take action.
Box 1 An overview of AI and machine learning Although AI covers the broad field of intelligent software systems, today the term is most often used to refer to systems that implement ML algorithms.
An ML algorithm is one that incorporates a data structure (called a model) obtained as a compression of the 'training' data, usually with the aim of approximating probabilities of interest.
Neural networks are the best-known example of such models, and the field of deep learning has shown outstanding success in applying large-scale neural networks to many previously intractable tasks in image and audio processing, natural language processing (NLP), and other areas.
In its simplest form, the training of ML algorithms is supervised (i.e., supervised learning).
This means that the training data comprise (usually human-labeled) pairs such as image pixels and the type of object in the image or audio spectrogram (e.g., the bird species).
Example applications include predicting taxonomic identity from a photo or an audio recording of an animal, or predicting land-cover class from remote sensing tiles.
The process of generating trustworthy labeled data for supervised learning is, and remains, labor-intensive.
However, there are powerful variants of the supervised approach: the 'training signal' on which model training depends need not always come from human-generated labels.
It may come from structures observed within the data itself (e.g., next-term prediction in sequential data such as text) or between datasets (e.g., machine translation models learn from comparison of many parallel texts).
This is commonly referred to as self-supervised learning.
It may also come from transfer learning, where a model trained on one task (e.g., recognizing road traffic objects) is fine-tuned with limited data to solve another task (e.g., alerting to the presence of a pedestrian).
Reinforcement learning solves decision problems (such as in game-playing) and takes its training signal from direct exploratory interaction with its environment.
It learns a decision policy as a ML model, often a neural network, and can converge to superhuman skill levels (e.g., in chess, Go, and some video games).
Sequential models, in particular, have reached a high degree of sophistication in LLMs (such as ChatGPT) which use a combination of large-scale neural networks and transformer architectures, and can be further fine-tuned with reinforcement learning.
Finally, the idea of transfer learning can potentially be taken a long way with the proposal of foundation models (FMs) [21].
The idea here is to invest one-off (for an application domain of interest) in very large-scale and ideally self-supervised, models.
The resulting FM can then be retuned at relatively low cost for specific predictive tasks in the domain.
However, it is important to note that the current success of foundation models is derived from their access to large high-quality datasets for training, which are often manually annotated in an expensive and time-consuming process and are therefore not based purely on unsupervised learning.
These foundation models [21] take unlabeled input and exploit structure from within the data to learn.
A common and general approach is to hide part of each input example and train the model to predict the missing parts.
This process is part of the training of the model, not a model evaluation method such as cross-validation in conventional statistics.
The next-word prediction task used to train LLMs such as ChatGPT is one example of self-supervised learning.
Freed of the need for labels, models can be trained with large amounts of data and through their self-supervised task can learn generic representations.
For example, examination of large visual models trained through self-supervision reveals specialized structures for detecting different classes of objects or animals [22].
Once trained, these models can be fine-tuned to a specific task.
Consider a visual model that can detect various tree species and leaf shapes.
It will require fewer new labeled examples of a specific endangered tree species of interest to be able to classify new examples compared to training a new visual model from scratch [23].
Current successful deployments of LLMs often take the form of copilots, where AI systems improve user productivity by assisting decision-makers, surfacing information, suggesting changes, and receiving corrections.
This approach leverages the strengths of AI by synthesizing large amounts of information while mitigating risks associated with potential errors or biases.
However, challenges remain, including the need to address biases in training data and the importance of human oversight in key applications.
Scanning the horizon for future applications of AI to improve conservation To identify the areas where AI has considerable potential to revolutionize conservation, we applied a modified Delphi technique to select and rank suggestions from experts [24,25] (Box 2Figure 1).
This technique maintains the transparency, repeatability, and inclusivity of the process [26].
Participants in the horizon scan were selected based on consultation of the professional networks of the organizing committee and internet searches, and attempted to produce a mix of subject area expertise and geographical representations.
The organizing committee produced an initial document summarizing recent advances in AI, the needs of conservation, and the main areas where AI is relevant to conservation.
This provided a grounding in AI for conservation experts who may have had little exposure to AI advances, and gave AI experts an understanding of the interests of conservationists to facilitate discussion at the workshop.
Authors were asked to suggest 2–8 potential developments, each with a short explanation.
In some cases the authors gathered ideas from within their organizations, thus further expanding the sample of experts consulted and the geographical spread of idea generation.
Figure 1 Figure 1 The process used and the resulting filtering of ideas to produce a ranked list of how AI could revolutionize conservation effectiveness.
Show full captionFigure viewer Box 2 Conducting the horizon scan In July 2024 a panel of 27 experts accepted an invitation to participate in the horizon scan, comprising 18 conservation scientists and nine computer scientists and AI specialists.
Some experts sit across both areas of expertise.
These experts are the authors of the present paper.
Participants were required to submit 2–8 ideas detailing how AI could be leveraged in conservation across a range of applications, including image and audio recognition, environmental DNA (eDNA) analysis, modeling, and data interpretation and integration.
Participants canvassed their networks and colleagues to broaden the perspectives captured in the horizon scan.
Figure 1 provides an overview of the process used to identify and score ideas.
For this horizon scan, 104 ideas were submitted by participants for consideration (Table S1).
Participants then confidentially and independently reviewed each idea submitted, and ranked them by assigning a score of between 1 (least significant) and 1000 (most significant) to each idea.
The large range of scores was simply to make it easy for scorers to rank items, and the scores themselves were not used.
Participants assigned a single score to each idea by subjectively combining two criteria: (i) its potential to have an important impact on the field of conservation science and/or practice, and (ii) its likelihood of coming to fruition.
Notes were added by participants to provide further information as to whether ideas should be retained for the second round.
To counter the effect of voter fatigue [91], participants were randomly assigned to one of three lists of ideas presented in different orders.
Ideas were clustered into broad topics (audio, images, reviewing literature, modeling, data, generating text, negative consequences, citizen science, eDNA, remote sensing, robotics, society, and other) by the lead author.
Participant scores were then converted into ranks (1–104) where the highest score denotes the highest rank.
The median rank across all participants for each idea was calculated, and the 30 top-ranked ideas were brought forward for discussion in the workshop.
All rank calculations were conducted in R statistical software [92], and the code is available via GitHubxi.
Two ideas in the top 30 were deemed by the organizing committee to be similar to two other ideas suggested, and were therefore presented together in the shortlist.
This led to 28 distinct ideas being shortlisted.
Figure 1 provides an overview of the process used to identify and score ideas.
For this horizon scan, 104 ideas were submitted by participants for consideration (Table S1).
Participants then confidentially and independently reviewed each idea submitted, and ranked them by assigning a score of between 1 (least significant) and 1000 (most significant) to each idea.
The large range of scores was simply to make it easy for scorers to rank items, and the scores themselves were not used.
Participants assigned a single score to each idea by subjectively combining two criteria: (i) its potential to have an important impact on the field of conservation science and/or practice, and (ii) its likelihood of coming to fruition.
Notes were added by participants to provide further information as to whether ideas should be retained for the second round.
To counter the effect of voter fatigue [91], participants were randomly assigned to one of three lists of ideas presented in different orders.
Ideas were clustered into broad topics (audio, images, reviewing literature, modeling, data, generating text, negative consequences, citizen science, eDNA, remote sensing, robotics, society, and other) by the lead author.
Participant scores were then converted into ranks (1–104) where the highest score denotes the highest rank.
The median rank across all participants for each idea was calculated, and the 30 top-ranked ideas were brought forward for discussion in the workshop.
All rank calculations were conducted in R statistical software [92], and the code is available via GitHubxi.
Two ideas in the top 30 were deemed by the organizing committee to be similar to two other ideas suggested, and were therefore presented together in the shortlist.
This led to 28 distinct ideas being shortlisted.
A meeting was held with 13 participants attending in person and 12 attending online.
Two participants were unable to attend the workshop but participated in the initial long-list scoring and preparation of the manuscript.
To account for participants attending from different time zones, the meeting was held in three sessions.
Session 1 with 25 participants in attendance discussed audio, reviewed the literature, and generated text, whereas session 2 with 25 participants discussed images and remote sensing, including a focused discussion on the potential negative consequences and pitfalls of AI.
The final session with 24 participants focused on modeling and data followed by a discussion of how the field of conservation may need to adapt to take full advantage of AI.
Each idea was discussed for 10 minutes.
After each discussion, participants scored each idea on a scale of 1–1000 (low to high).
High scores denote the most significant ideas, low scores the least significant.
The scores of each participant were converted into ranks at the end of the workshop (the highest-scoring idea being assigned to rank 1), and the 20 ideas with the highest median ranks (therefore the most significant ideas) were identified.
Not all online participants could attend the full workshop.
To incorporate their partially scored lists with the lists of participants who scored all ideas, we computed a 'division factor'.
The division factor is the ratio of total number of ideas to the number of ideas scored, plus one (Equation I): DF= TI SI+1   [I] where DF is the division factor, TI is the total number of ideas, and SI is the number of ideas scored by the expert.
The partially scored lists were then ranked (e.g., if only 10 ideas were scored, they were assigned ranks 1 through 10, where rank 1 is the most significant idea).
To calculate the appropriate final rank for integration with the fully ranked score sheets, we used the following equation (Equation II): FR=PR×DF [II] where FR is the final rank, PR is the rank given when all partially scored ideas are ranked, and DF is the division factor.
This creates a buffer in the ranking scale that allows for the possibility that ideas unranked by a participant could potentially be ranked higher than their partially ranked ideas if they were to be evaluated.
This adjustment expands the range of the partial rankings to align with a full ranking scale, leaving space for potentially unranked items between them.
Ideas that were not scored by a participant did not have a rank imputed and were left blank.
Therefore, participants only contributed to the ranking of items they were able to score.
Two ideas were related to identifying the expansion frontiers of human disturbance, and it was proposed that these ideas should be amalgamated into a single idea.
In addition, there was a tied rank at 20, and it was decided that both ideas should be included, therefore 21 ideas are included in the final list.
We recognize that there may be limitations to ideas generated in the horizon scan process and that a different group of experts may identify a different set of ideas.
Our methodology of inviting participants from a range of subject backgrounds and global regions, and asking them to canvass their network of colleagues and collaborators, aims to identify as broad a set of issues as possible and limit bias towards a particular discipline or study area.
We note also that Sutherland et al.
[27] reported no significant correlation between the areas of research expertise of the participants and the top issues selected in a horizon scan conducted in 2009.
Therefore, horizon scans do not necessarily represent ideas that reflect the expertise of participants.
Potential applications of AI in conservation In the following we present the 21 ideas where AI has considerable potential to revolutionize biological conservation (Figure 2).
The ideas are presented in thematic groups rather than in rank order.
The full list of 104 ideas is included in Table S1 in the supplemental information online.
Ideas in the full list vary in their detail, relevance, and completeness, but may provide a useful insight for additional applications of AI within conservation.
They include ideas relating to the use of robotics and citizen science, and understanding the connections between people and nature.
In the following we present the 21 ideas where AI has considerable potential to revolutionize biological conservation (Figure 2).
The ideas are presented in thematic groups rather than in rank order.
The full list of 104 ideas is included in Table S1 in the supplemental information online.
Ideas in the full list vary in their detail, relevance, and completeness, but may provide a useful insight for additional applications of AI within conservation.
They include ideas relating to the use of robotics and citizen science, and understanding the connections between people and nature.
Figure 2 Figure 2 The 21 artificial intelligence (AI) applications identified in the horizon scan placed into a framework adapted from Krenn et al.
Show full captionFigure viewer Interpretation of images collected by ground-based sensors Automated species recognition from images collected by devices such as camera traps and mobile phones is well advanced and is available through applications such as iNaturalist [28], Pl@ntnet [29], ObsIdentifyvi, Google Lensvii, and Merlinviii.
However, improvements in AI will enable substantial acceleration of its implementation and application, including real-time identification systems that can send alerts, for example, when specific species, large numbers of individuals, or threats are detected [30].
Scaling up image acquisition could be achieved through citizen science, community-based monitoring, harvesting images from social media, or repurposing existing datasets (e.g., Google Street View).
This supports applications, such as mapping species distributions and range extensions, monitoring the establishment or spread of invasive alien species, and detecting and identifying illegal imports of traded species at customs [31].
Identifying and monitoring of individuals from images Scaling up automated recognition of individual animals from images could enable more widespread and accurate assessment of population sizes, for example by using mark–recapture [32], leading to more accurate assessment of status and trends, as well as other opportunities such as quantifying home ranges and identifying movement patterns.
Detecting new species from images AI workflows have recently been developed for the detection and confirmation of unknown species identity from images, also known as novel category discovery [33].
This technique could accelerate the documentation of 'dark diversity', especially in combination with DNA analysis.
These approaches could be used both on images captured from the field and from digitization of museum collections [34].
AI camera systems for monitoring environmental compliance AI systems for monitoring compliance could be as broad as measuring biodiversity gains promised by developers, analyzing water quality measurements from treatment plants, and detecting illegal deforestation from satellite imagery.
An obvious candidate area would be monitoring compliance with measures to mitigate commercial fishery bycatch.
Bycatch of seabird species are resulting in mortality rates that are driving some species towards extinction [35].
Regional Fisheries Management Organizations already require implementation of measures to counter this [36].
However, detecting compliance relies on boat-based observers, which is resource-intensive and dangerous.
AI-enabled onboard camera systems can facilitate monitoring seabird presence, interactions with fishing gear (e.g., cable strikes), bycatch (i.e., ensnared birds), and the use of mitigation measures, thus enabling safer, cheaper, and more reliable monitoring of compliance.
Audio AI is already being used extensively to identify species from audio recordings, principally for birds and bats.
For example, using ML, BirdNET can currently identify ~3000 of the most common bird species worldwide [37].
However, there is considerable potential for scaling up to cover the remaining 75% of bird taxa, as well as other vocalizing animals including invertebrates.
In combination with distribution of autonomous recording units or other devices running identification algorithms locally, this could transform our ability to monitor biodiversity [38].
AI is already being used to assess soundscapes to generate insights into the state of ecosystems such as coral reefs [39] and tropical forests [40].
Audio recognition of individuals In some cases it is already possible to distinguish individuals within a species from their sounds [41].
There is likely to be considerable opportunity to extend this given that (i) voice recognition in humans is well understood (using 'voiceprint' vectors) [42], and (ii) many species are observed to recognize individuals from their vocalizations [41].
Potential applications include estimating population sizes, tracking individual movements, and quantifying dispersal.
Distributed acoustic sensing Novel AI-enabled technologies for detecting sounds in the marine environment could transform monitoring of marine fauna.
For example, distributed acoustic sensing (DAS) can detect sounds in real time using the dense network of fiber-optic telecommunication cables that cover both deep ocean and coastal areas worldwide.
It could be used for audio recognition of marine fauna such as cetaceans, seals, and fish, as well as of human activities (shipping and deep-sea mining) that may impact on them [43,44].
This would enable monitoring even in the most remote areas or at oceanic features that are difficult to access, such as seamounts.
Similarly, scaling up the application of hydrophones with built-in low-powered AI audio classifiers could revolutionize our understanding of the distribution and abundance of marine animals [45,46].
Satellite and airborne remote sensing ML is commonly used to interpolate data from satellite sensors to classify ecosystems and track degradation and land-use change [47].
There is also a rapidly advancing application of this technology to identify species from space [48,49].
Increasingly, deep learning approaches can detect patterns not easily picked up by conventional approaches [50].
The surface of the planet can be obscured by clouds, and imagery quality is affected by illumination angle and atmospheric effects, requiring the inclusion of complex preprocessing steps: AI is more effective than conventional approaches at making these corrections [51].
Foundation models for satellite remote sensing Pretrained foundation models (Box 1) can facilitate the monitoring of areas with restricted availability of training and validation data [52].
However, the fine tuning of these models for specialized tasks can be highly challenging [53].
AI can facilitate the fusing of multiple data modalities, such as optical and radar imagery, as well as the use of time-series analyses for improved land cover classification, threat detection [54], and monitoring [55,56].
Predicting biodiversity loss or restoration using Earth observation foundation models Global biodiversity monitoring uses a series of metrics, but there are often challenges in keeping the agreed metrics up to date and as close to real time as possible.
AI could facilitate the automated production of Earth observation-based datasets used in policy and business applications, such as the Human Footprint Index and the Biodiversity Intactness Index which assess the degree to which terrestrial ecosystems are affected by land-use change and intensification.
However, applying this will require some care to avoid error propagation and its associated impact on biodiversity science [57].
Combining datasets for new insights Primary observational datasets are the 'fuel' for ML algorithms, but AI also creates opportunities to improve higher-level datasets by combining diverse types of input data.
For example, training models on photo catalogs together with remote sensing images has facilitated the development and validation of land-cover change products such as Dynamic World [58].
Gains are likely when bringing multiple datasets together.
For example, the CAPTAIN project [14] uses reinforcement learning to train models to identify areas for conservation prioritization by integrating species distribution data, anthropogenic disturbance data, human population densities, phylogenetic diversity, land-use data, and climate change projections, while another project combines similar datasets to estimate extinction risks for 89% of known tree species [59].
Federated AI learning Several biodiversity data systems contain 'data islands' that cannot be directly shared for the purposes of training AI models (e.g., critically endangered species locations, or illegal hunting and trade data).
Using expertise in managing sensitive data from other fields, such as healthcare [60], it may be possible through federated learning to train a distributed model for biodiversity characteristics which is an accurate representation of the underlying raw sensitive data and delivers real-time insights into the status and trends in biodiversity, pressures, responses, and benefits.
If possible, this would allow the unification of numerous distributed databases into models that facilitate decision-making without revealing sensitive raw data.
However, much work will be necessary to ensure that these models can be made robust to attacks that leak the original sensitive training data [61].
Monitor online wildlife trade Computer vision (i.e., automated processing and understanding of images), natural language processing (i.e., automatic processing of textual content), and multimodal models can be used to understand where, when, how, why, and what species and wildlife products are being traded on which online platforms [62].
For example, a recent study of global trade in chameleons used multiple lines of evidence to understand trade patterns and the impacts of trade bans [63], but automation and AI-assisted insights could have dramatically speeded up the process.
Research using these methods must prioritize adherence to the highest standards of data privacy and protection [64].
Improving models of areas of habitat from diverse data Our understanding of the areas of habitat (AoH) of different species currently relies on extremely patchy sampling, estimated range maps, and incomplete knowledge of species ecology and habitat preferences.
AI could improve AoH maps by integrating occurrence data on specimen locations, habitat and cohabitation preferences, environmental and ecological data, remote sensing data, and spatial datasets on human impacts.
These approaches are already being tested [65] and could move from relatively simple correlative AoH models (e.g., masking estimated species range maps with elevation and climate) to more sophisticated covariates that describe species habitat selection across diverse ecosystems, and deep learning could make more comprehensive predictions of species ranges and perhaps also populations [66,67].
Predicting and mitigating human–wildlife conflicts Human–wildlife conflict, where people themselves, or their property, crops, or livestock, are harmed by wildlife is a serious problem for some human communities and, when it results in retaliatory killing, is an important threat to some species [68].
AI-powered cameras are already being used in various countries to warn communities when particular mammal species are nearby, for example elephants in Africa or tigers in Asia [69].
Similar technology can also track humans within landscapes set aside for animalsix.
However, there are important ethical and privacy concerns with such technology which potentially may exacerbate conflict between conservation and local communities [15].
AI-enabled systems combining short- and long-term data on factors correlated with human–wildlife conflicts will provide more accurate predictions and opportunities to take action earlier.
Modeling and causal inference Using datasets, usually in combination, there is the potential to apply AI to build system models that can be used to test hypotheses or to build credible counterfactuals for the evaluation of conservation policy and practice.
Uses could include simulating the outcomes of policy decisions and predicting projections based on a range of data sources.
Large-scale modeling of biodiversity outcomes from different policy interventions, using general ecosystem models, are increasingly available [70,71].
However, they are time-consuming and resource-intensive, and are typically used to inform international policy formulation – for example the Global Biodiversity Framework [72] and the EU New Green Dealx.
AI may offer opportunities to accelerate these large-scale modeling efforts and observe emerging patterns that are important for policy decision-making.
Digital twins for ecosystems Digital twins are used in engineering and Earth sciences [73], but they can also be applied to the problem of predicting outcomes of conservation interventions.
Digital twins for ecosystem modeling and prediction could be developed, and potentially paired across multiple domains (e.g., physics, fish demography, and seabird ecology), to understand and model the likely outcomes of different interventions [74,75].
Moreover, where we seek to apply AI to optimize intervention policies (as in CAPTAIN), simulation from a digital twin can provide an additional training signal.
Prioritizing restoration efforts Restoring degraded habitats is essential to avert extinctions, recover populations, and minimize climate change.
AI could help us to direct such efforts more efficiently by identifying the most important locations for restoration given habitat loss and degradation to date, the distribution of species and ecosystems, projected climate change, and shifts in energy production, food production, and human population distributions.
Artificial neural networks have been previously explored for prioritizing areas for wetland restoration (utilizing multiple inputs including elevation), as well as for generating soil texture and permeability maps, identifying protected areas for waterbirds, and estimating the likelihood of dust storms and urbanization [76].
Improving species distribution models Species distribution models (SDMs) are valuable for conservation decision making such as assessing land-use change impacts.
Using species distribution records and remotely sensed data, SDMs produce maps of the (relative) probability of occurrences.
ML models are well suited to integrate heterogeneous and multi-fidelity datasets efficiently, and can handle missing data, noise, and non-linear relationships; they can automatically learn relevant features from raw spatial data and uncover complex patterns and interactions.
However, current limitations include the scarcity of labeled data (especially for plants and non-vertebrate animals), spatial biases in data, temporal mismatches between field and remotely sensed data, data accuracy, over-reliance on abiotic conditions, limited consideration of biotic interactions, and overfitting.
New AI approaches [e.g., physics-inspired AI and explainable AI (xAI)] and rapidly increasing citizen science datasets may help to address these problems.
Predicting deforestation and agricultural expansion Deep learning can be used to analyze satellite imagery and other geospatial data to predict where land-use change is most likely by learning spatiotemporal patterns from the remote sensing data [77] instead of using the mechanistic modeling approaches that are currently used.
Such models could be used to predict where deforestation would have occurred under business-as-usual scenarios to allow better estimates of the effectiveness of interventions aimed at slowing land conversion [such as zero deforestation commitments or reducing emissions from deforestation in developing countries (REDD+) projects].
Similar techniques can also be applied to training predictive models from time-series maps of agricultural expansion which has seen rapid acceleration in the past two decades [78].
Parameter estimation for global ecosystem models Global ecosystem models (GEMs) simulate the dynamics of life on Earth, including the interactions between plants, animals, and the environment.
GEMs are valuable for modeling the impacts of climate change on nature.
However, predictions of dynamic GEMs do not align well with field measurements (e.g., of fluxes of greenhouse gas); they fail to make reliable predictions of large-scale fires and droughts, and they rarely include plant–animal interactions.
Many processes in dynamic GEMs are represented by semi-empirical semi-theoretical equations.
AI optimization techniques could automate the calibration of the parameters in these models across multiple scales.
Physics-inspired AI techniques, such as reduced-order modeling, could potentially find low-dimensional representations that capture the essential dynamics while being much faster to compute [75].
Reviewing the literature There is considerable potential for using AI to improve the efficiency of extracting, screening, and collating literature for conservation [79], as is already underway to some extent in medicine [80].
For example, the creation of systematic reviews could be automated such that they can be carried out in days rather than months or years, enabling more timely guidance drawing on the full range of evidence.
LLMs for evidence synthesis Evidence syntheses for biodiversity conservation are key for effective decision-making, but are challenged by increasingly time-consuming tasks, a broad evidence base, and persistent underfunding.
Moreover, most evidence syntheses produced in the conservation space are static and fail to incorporate new evidence as it is generated.
AI has the potential to be harnessed to identify relevant (new) evidence and integrate it into the existing evidence base and synthesize key messages rapidly (i.e., living evidence syntheses [81]).
Doing so will ensure decision-makers have access to the best available evidence to guide them.
Multilingual literature scanning LLMs enable multilingual literature searches for non-English evidence [82], which is key given that non-English languages typically dominate in areas of most conservation concern [83], although there is a growing quantity of non-English evidence [84].
LLMs to interpret gray literature LLMs can be used for identifying gray literature and text matching to cluster relevant evidence.
They can accelerate evidence synthesis and make it more timely, equitable, and inclusive in terms of the evidence base and the perspectives considered.
Assessing extinction and collapse risk from diverse sources Assessments of extinction risk for species and collapse risk for ecosystems currently rely on manual compilation of information on the population sizes of species and their distributions and trends, as well as trends in areas and biotic/abiotic factors for ecosystems, to produce parameter estimates that are applied to IUCN Red List criteria.
AI could accelerate and expand the process by scanning the scientific literature and other online materials to locate relevant information in published and unpublished sources in all languages, including real-time land-cover change.
This would substantially accelerate and improve the process of assessing extinction and collapse risk while significantly reducing costs.
More ambitiously, extinction and collapse risk could be estimated directly in the future by combining relevant literature-derived parameter estimates with spatially explicit predictive models informed by remote sensing.
Generating text The success of LLMs in creating novel text, images, and videos is well recognized.
There has long been a distinction between the use of generative AI for error-tolerant commercial applications such as marketing and social media, as well as for safety-critical or politically sensitive applications in specialist use cases.
However, their recent success has led to their application being debated in medicine [85].
Their ability to generate personalized outputs and recommendations based on a synthesis of available evidence has led to suggestions that they could play a role as policy advisors [86].
This could include synthesis of multiple data sources for a specific location to provide bespoke management recommendations, or application to complex numerical datasets to provide non-specialist text summaries for decision-makers.
LLM conservation advisors LLMs could synthesize the evidence of impact for different conservation management options [79], and combine this with data on species, land-use, or socioeconomic factors for a specific context to produce easily understandable and evidence-based information for practitioners and policymakers.
The inclusion of human in the loop, whereby human experts are involved in providing feedback and evaluating advisor outputs during model training, would be essential to limit biases and hallucinations [86], as would fine-tuning and retrieval augmented generation (RAG) based on curated, robust evidence and data.
Negative consequences of AI AI will undoubtedly lead to substantial changes in conservation in the coming years.
Although many will be positive, there is also the potential for unintended negative outcomes.
These need to be understood and mitigated.
There is a danger that AI could have a polarizing effect on conservation and conservation funding.
If AI-supported conservation becomes the 'gold standard', because people are impressed by the novelty, claims of large impacts, or the promise to revolutionise conservation, then we may risk seeing a shift in funding and leadership in conservation.
Support for conventional experimentation and on-the-ground practices, which already struggle to attract resources, could be redirected towards financially wealthy institutions which are able to undertake AI work.
This could be especially true in conservation research where grounded field-based and participatory studies, which have a role in advancing understanding and local ownership, may become ever more difficult to fund.
This could undermine efforts to improve the diversity of voices, knowledge, and approaches in conservation.
Hence it is important that funders recognize the importance of supporting a spectrum of conservation research and practice that embraces both conventional and AI approaches.
There is a fear that we could see a loss of essential skills in conservation if people in the field pivot towards implementing AI over conventional techniques.
Retaining species, ecosystem, and community experts will be integral to creating reliable AI technology.
Data is the fuel of AI, and data collected by conservation experts will be essential for producing better models, and this crucial data-collection work must be appropriately recognized.
Moreover, information itself, however it is obtained, does not lead to better conservation, and it is important that any recommendations are designed to work in the real world and are not detached from the social and ecological reality on the ground.
AI colonialism is a central concern – data potentially extracted from the Global South might be forwarded predominantly to data centers in the Global North for training AI models, followed by AI-driven mandates being issued to the Global South on how land and resources should be managed.
This would undermine the efforts of the conservation community to address the colonial legacy of contemporary conservation and recognize the importance of indigenous rights and voices.
Furthermore, there is a risk that AI contributes to a militarization of conservation – where computer systems, developed far from the area concerned, identify infractions and trigger enforcement without understanding the local context.
Given that local perceived legitimacy is essential to promote compliance with conservation rules [87], this could create or exacerbate conflict.
To address digital inequalities and injustices, and to produce less biased, fairer, and more robust information for conservation actions, there is a need to integrate epistemic feedback loops into black box models.
This can be achieved by leveraging human-in-the-loop designs as well as political agencies and democratic decision-making [88].
Combining AI models can create inherent biases and propagate errors, leading to 'AI pollution' if the outputs of biased models are used to train new models.
This may lead to increasingly poor representation of understudied species or ecosystems, potentially pushing people away from considering these understudied areas if we are over-reliant on AI for decision-making, and this needs to be explicitly considered in any AI-based approaches.
Much of the promise of AI lies in bigger and better models.
However, the bigger the models become, the more expensive they are to run in terms of computation, bandwidth requirements, power, and expertise.
There is already significant concern about the environmental implications of the power consumption and cooling requirements of AI infrastructures, and these are likely to increase.
The cost of using these models may push AI beyond the current resources (financial and human) of conservation.
However, in conservation there is less call for large generalist AI models such as Chat GPT, and the focus is instead on smaller and more specialized models for specific use cases.
It would be helpful for the conservation community to adopt a code of practice to address the sustainability considerations associated with AI research.
Finally, although AI models to further the effectiveness of conservation are built with good intentions, it must be remembered that they could also be used by bad actors.
For example, image and audio tools used by conservationists to track and locate endangered or protected species can equally be exploited by poachers or be coopted by government regimes to monitor the movement of people.
Similarly, remote sensing data could be contaminated or poisoned by malicious private companies to exaggerate restoration efforts so as to attract greater revenue from carbon or biodiversity credit schemes.
It is important that significant steps are taken to protect data and to ensure that tools are used only for their intended purpose.
How might conservation be organized to take advantage of AI and reduce problems?
To take advantage of the potential ability of AI to identify new patterns, generate accurate predictions, run more accurate simulations drawing on diverse data sources, and help decision makers to better assess the efficacy of potential interventions, society and the field of conservation will need to adapt.
Reproducibility of results, one of the pillars of the scientific method, becomes challenging when there is insufficient documentation, limited access to the underlying codes and data, and a lack of understanding of how AI tools reach conclusions, which makes it difficult to scrutinize, verify, and replicate experiments [11].
Improved literacy concerning AI will help to counteract its misinterpretation and recognize its limitations.
Improved AI literacy will also be essential to ensure sufficient peer review of papers using AI.
To counteract the influx of outputs from generative AI models, it will be important for society to identify a way to segregate human-produced content from that produced by AI.
One such example could be digital kitemarks, where individuals, organizations, and institutions are assigned digital signatures that can be used to authenticate the human-generated origin a document or dataset.
Interdisciplinary collaboration between AI specialists, domain experts in the natural and social sciences, and indigenous and local knowledge will be central to building accurate AI models.
There is a danger of decoupling between the creators and users of AI tools.
Hallucinations in outputs are more likely to be detected by subject experts.
This also extends to ensuring that there is close consultation between the developers of AI tools and the experts who manage underlying datasets to ensure that data limitations are understood and the data are not used inappropriately because inaccurate use of data can lead to misleading advice for decision-makers [89].
Moreover, researchers should not incorporate advanced AI techniques at the cost of appropriate conventional methodologies.
It should be remembered that AI is only one of the tools in the toolbox.
There are additional barriers to broad uptake of new approaches which will need to be considered.
There is a large inequality of data availability between the Global South and the Global North.
This needs to be acknowledged and understood to avoid embedding biases in AI models that are intended to predict outputs on a global scale.
This inequality extends also to ecosystems and species where there is a disparity in data availability – for example, data on birds in the Amazonian rainforest are more numerous than for marine bryozoans in Antarctica.
Access to the infrastructure and resources that are necessary to train and run these models is currently limited and is disproportionately held by elite academic institutions, governments, and technology companies in the Global North.
Training foundation AI models is expensive and requires a large amount of computing power, as well as IT expertise, high internet bandwidth, and reliable power supplies.
Methods of access to these resources, as well as overcoming language barriers, need to be thoughtfully considered to widen participation in AI research by conservation practitioners, researchers, and governance institutions including civil society associations, non-governmental organizations (NGOs), and government conservation managers based in the Global South.
The role of expert data labelers will be crucial for maintaining data quality, preventing biased outputs, and addressing data fabrication.
Many species and ecosystem experts are based in the Global South, and it is imperative that their skills and labor are equitably used and recognized.
It also highlights the value of conventional conservation expertise in the production of these models.
Moreover, concerted efforts will be needed to substantially strengthen the connection between the outputs of AI models and the ecological and social realities of implementing and sustaining on-the-ground conservation actions [90].
Although AI systems have potential to make monitoring of infractions of conservation rules cheaper and therefore more widespread, they cannot by themselves overcome social and governance challenges which strongly influence compliance.
For example, regulators can put AI-enabled cameras on board ships to monitor bycatch, but the utility of the technology will depend on compliance and follow-through.
Concluding remarks Following a horizon scan methodology, we identified 21 areas where AI can help to revolutionize conservation.
These represent both a cross-section of research areas within conservation science and practice, as well as methods through which AI contributes to scientific understanding.
AI stands to rapidly improve our ability to understand distributions of species; locate rare or so far unknown species; identify, model, and monitor threats; identify priority areas for conservation; model the effectiveness of planned conservation actions; monitor adherence to environmental legislation; and assimilate and interact with scientific evidence.
However, we need to ensure that AI-supported conversation does not replace valuable established conservation techniques, education, and on-the-ground research.
The intersection within conservation between scientists, practitioners, governments, local communities, and indigenous peoples is nuanced and complex.
It is important that AI technologies are developed and deployed with understanding of local contexts.
Moreover, the fact that many of the intact ecosystems of our planet reside in the Global South poses many significant challenges to the equitable implementation of AI technologies because at present these are predominantly trained and developed in the Global North.
AI will be an invaluable tool to support conservation, but it is not a panacea.
Proactive and creative efforts to embrace AI, while also ensuring that proper protections and attention to equitable and just conservation practices are in place, will be necessary for AI to reach its transformative potential (see Outstanding questions).
Outstanding questions How do researchers and practitioners ensure that funders recognize the importance of supporting a spectrum of research embracing both traditional and AI approaches?
There is a danger that AI could have a polarizing effect on conservation funding, and directs funds away from effective traditional methods of conservation.
How can the field of conservation redress the unbalanced access to computing resources required for AI research between the Global North and Global South?
AI colonialism should be a central concern of AI technology in conservation.
With data potentially being sent from the Global South to data centers in the Global North where they are used to train AI models, we must be careful not to issue AI-driven mandates to the Global South on how land and resources should be managed.
What protections can be put in place to prevent exploitation by bad actors?
These technologies could be coopted by bad actors to track human populations, locate endangered and/or valuable species, or identify and pollute data sources for financial gain.
How this can be prevented requires careful consideration.
Should the conservation community create and adopt a code of practice to address sustainability, equity, equality, and data privacy and security in AI research?
To ensure that these issues are considered in the pursuit of producing AI technologies for conservation, the creation of a centralized code of practice may lead to more robust and considered applications.
Abstract Preserving biodiversity is crucial for maintaining ecological balance; however, traditional conservation methods often face various limitations.
In most cases, the efficacy of these approaches is frequently constrained by difficulties in scaling and the absence of up-to-date data, hence requiring the incorporation of novel technology.
The latest progress in the field of artificial intelligence (AI) offer transformative potential for enhancing contemporary conservation endeavors.
There is a growing utilization of AI technologies, like machine learning and data analytics, to improve species identification, habitat monitoring, and threat assessment with exceptional precision and effectiveness.
This study explores how AI is incorporated to enhance conventional conservation methods, particularly in the areas such as data analysis, species identification, and habitat monitoring.
This paper examines a number of case studies that demonstrate the successful use of AI, with a particular focus on notable advancements in data management, predictive modeling, and resource allocation.
The findings highlighted the significance of synergistic methodology that integrates the strength of traditional techniques with the flexibility of contemporary technologies, hence facilitating the development of more resilient conservation solutions.
This study also discusses the potential implications for future research and the practical use of AI in the field of conservation.
It highlights the strategy of seamless integration to justify both scientific investigation and conservation results.
Similar content being viewed by others  Improving biodiversity protection through artificial intelligence Article Open access 24 March 2022  Harnessing artificial intelligence to fill global shortfalls in biodiversity knowledge Article 20 February 2025  Artificial Intelligence and Crowdsourced Social Media Data for Biodiversity Monitoring and Conservation Chapter © 2024 Explore related subjects Discover the latest articles, books and news in related subjects, suggested using machine learning.
Biodiversity Conservation and Preservation Conservation Biology Conservation genomics Pulp conservation Artificial Intelligence Introduction Biodiversity conservation is crucial for maintaining natural equilibrium and promoting human welfare (Rawat and Agarwal 2015).
The preservation of biodiversity ensure the long-term viability of ecosystem, providing essential ecological, social, and economic benefits(Niesenbaum 2019).
These services encompass furnishing essential resources i.e., food, water, and medicine; regulatory functions like disease management and climate regulation; supporting functions such as soil formation, nutrient cycling, and cultural functions (Naeem et al.
Traditionally, biodiversity conservation has relied on approaches such as creating protected areas, relocating endangered species, and implementating legal safeguards to protect habitats (Heywood 2019).
However, these conventional methods face significant challenges in today’s rapidly changing global landscape, characterized by ongoing difficulties such as habitat degradation, climatic variability, and the proliferation of non-native species (Richardson and Whittaker 2010).
In response to these challenges, recent approaches have begun integrating advanced technologies such as AI, remote sensing, and genetic analysis to enhance conservation efforts.
As natural and human landscapes change, the efficacy of these traditional methods is being increasingly scrutinized (Redclift and Springett 2015).
Contemporary methodologies, particularly those applying AI for tasks like data analysis and predictive modeling, present auspicious prospects for enhancing biodiversity conservation (Obaideen et al.
AI possesses the capability to efficiently and accurately analyze extensive quantities of data, enabling tasks such as species identification through image recognition and habitat monitoring via satellite imagery (Ditria et al.
This technological transition serves as a crucial connection between traditional conservation techniques and modern challenges, enabling the implementation of more adaptable, flexible, and efficient conservation strategies (Bibri et al.
This research is justified by the urgent need to enhance biodiversity conservation efforts, as traditional methods alone are insufficient to address the escalating threats posed by global change and human activity.The primary objectives of this study are to: (1) evaluate how AI can enhance traditional conservation methods, (2) analyze case studies demonstrating successful AI applications in biodiversity conservation, and (3) propose a framework for integrating AI technologies into existing conservation strategies.
AI is a potent instrument for swift, data-centric observations that can result in more efficient conservation measures.
The aforementioned viewpoint holds significant importance in the conservation of biodiversity, which subsequently upholds the provision of vital ecological services necessary for human life and the overall well-being of the planet.
By achieving these objectives, this article aims to present a revolutionary approach to environmental stewardship that integrates conventional conservation strategies with modern computational methodologies, ultimately leading to more effective and resilient conservation solutions (Fig.
The combination of traditional and contemporary approaches can enhance the ability to make well-informed and proactive decisions regarding conservation, so establishing a higher benchmark for environmental study and action.
1 figure 1figure 1 Integrating AI in biodiversity conservation framework  Full size image Classical approaches to biodiversity conservation Discussion on traditional conservation strategies Historically, conventional conservation measures have formed the foundation for protecting biodiversity, such as the establishment of national parks like Yellowstone in the USA, which has successfully preserved numerous species (Robinson 2006).
The primary emphasis of these techniques lies in the conservation of habitats, the creation of protected areas, and interventions tailored to specific species (Watson et al.
Although traditional conservation methods such as the creation of protected areas, species relocation, and legal protections have shown favorable results in various contexts,, their execution frequently encounters substantial obstacles, such as financial limitations, clashes with indigenous communities, and restricted expandability (Lister 1998).
To enhance the success of these conservation measures, it is crucial to strengthen policy enforcement and engage the community (Fig.
2 figure 2 Left Side: Illustration of a natural ecosystem with diverse species monitored using traditional tools like genetic sequencing and environmental assessments.
Right Side: AI-driven conservation using satellites, global monitoring, and data analytics to track and protect biodiversity worldwide  Full size image Habitat preservation Traditional habitat preservation efforts often involve establishing reserves and implementing restoration projects aimed at maintaining ecosystems (Lister 1998).
For instance, the restoration efforts in the Atlantic forest of Brazil have been instrumental in recovering native species and restoring ecological functions (Hoffmann 2010).
This technique serves the dual purpose of safeguarding biological diversity and maintaining the ecological functions, thus playing a vital role in the long-term survival of species (Moonen and Bàrberi 2008).
However, habitat conservation faces significant challenges, including habitat fragmentation due to urban development, agricultural expansion, and climate change impacts, which can disrupt ecological connectivity and reduce habitat quality (Hoffmann 2022; Ssenku et al.
Given that habitat fragmentation is primarily driven by human activities such as urban development, agriculture, and climate change, habitat conservation alone may not suffice to address these multifaceted challenges.
Therefore, it is essential to integrate habitat conservation with complementary strategies that target these external pressures.
These complementary efforts may include community engagement initiatives that promote sustainable land use practices, restoration projects that reconnect fragmented habitats, and policy advocacy aimed at reducing human impacts on ecosystems.
Legal frameworks and policies Legal frameworks and policies play a crucial role in establishing the essential foundation for the enforcement of conservation initiatives (Cooney 2004).
Examples include the Endangered Species Act (ESA) in the U.S.A (Act 1973) and the Convention on Biological Diversity (CBD), which aim to protect endangered species and their habitats.
The Endangered Species Act in the United States has led to the recovery of species like the bald eagle and gray wolf through stringent legal protections (Cooney 2006).
The purpose of these regulations is to safeguard endangered species and habitats, govern detrimental actions, and promote the sustainable utilization of resources (Berrens 2001).
Although legal frameworks have demonstrated some effectiveness, they must undergo continuous evolution in order to effectively tackle emerging environmental concerns and integrate scientific discoveries and community rights into conservation activities (Techera 2013b).
Studies have shown that populations of listed species under the ESA have increased significantly due to targeted recovery plans and habitat restoration efforts (Act 1973; Evansen et al.
These frameworks must include recent AI based approaches to effectively tackle emerging environmental concerns and integrate scientific discoveries and community rights into conservation activities (Techera 2013a).
Community-based conservation Community-based conservation entails the active participation of local populations in the administration and safeguarding of natural resources, acknowledging that local administration can result in more enduring conservation results.
An example is the CAMPFIRE program in Zimbabwe, which empowers local communities to manage wildlife resources, leading to increased wildlife populations and community benefits (Pimbert and Pretty 1997).
This methodology utilizes conventional knowledge and customs, cultivating a perception of possession and accountability among individuals within the group (Shackeroff and Campbell 2007).
For instance, local fishing practices that incorporate seasonal cycles and sustainable harvesting methods reflect conventional knowledge that can enhance fish populations and ecosystem health.
Similarly, indigenous land management techniques, such as controlled burns, have been shown to improve habitat conditions for various species.
Nevertheless, in order to achieve optimal effectiveness, it necessitates sufficient assistance in terms of enhancing capabilities and ensuring fair distribution of benefits.
Strengths and limitations of classical approaches Traditional conservation approaches have notable strengths due to their historical use and substantial empirical evidence supporting their effectiveness.
While these methods have successfully prevented species extinction, they often struggle with scalability, as seen in overexploited fisheries where traditional regulations failed to adapt the increasing demand (Agrawal and Redford 2006).
These approaches primarily focus on habitat preservation, regulatory measures, and targeted interventions designed to protect specific species.
However, these methods often face significant limitations.
For instance, protected areas may not adequately account for shifting species distributions caused by climate change, leading to ineffective conservation outcomes (Richardson and Whittaker 2010).
Additionally, traditional methods may lack flexibility and responsiveness; this has been evident in cases where invasive species management has been slow to adapt to new threats (Moonen and Bàrberi 2008).
They have played a critical role in preventing the extinction of several species and safeguarding essential ecological systems.
Nevertheless, these approaches are frequently restricted by their responsiveness rather than proactiveness, budgetary and logistical limitations, and occasionally insufficient incorporation with contemporary scientific methodologies and community requirements (Moonen and Bàrberi 2008; Ibisch et al.
The aforementioned constraints underscore the imperative of incorporating novel, adaptable, and all-encompassing methodologies, such as those offered by nascent technologies like AI.
Modern approaches including AI technologies in biodiversity conservation Introduction to modern technologies in conservation Contemporary technologies, especially AI, are significantly transforming biodiversity conservation by enhancing data analysis capabilities and enabling real-time monitoring.
Technologies such as satellite imagery for land-use monitoring and AI-driven analytics for species identification are revolutionizing conservation practices (Ritts and Bakker 2021).
Modern conservation techniques heavily rely on various tools and technologies, including genetic analysis methods, remote sensing, AI, and autonomous systems (Ditria et al.
2022; Bibri et al.
These technologies provide valuable insights and efficiency that were previously unachievable.
Such technologies facilitate the ability of conservationists to forecast alterations, simulate probable consequences, and proactively execute strategies to save biodiversity (Fig.
Genetic technologies Genetic technologies play a vital role in contemporary conservation efforts by offering techniques to evaluate biodiversity, comprehend population genetics, and monitor the genetic well-being of species.
Methods such as DNA barcoding and environmental DNA (eDNA) analysis enable the recognition of species based on small genetic remnants present in the environment, providing a non-intrusive approach to monitor biodiversity and the well-being of the ecosystem (Cristescu and Hebert 2018; Antonelli et al.
2021; Piaggio 2021; Silvestro et al.
These methodologies are particularly valuable for identifying rare or elusive species and assessing the impacts of environmental changes on genetic diversity.
By enabling precise species identification and monitoring genetic health, these technologies support conservation strategies aimed at preserving genetic diversity and informing management decisions.
AI algorithms can analyze genetic data more efficiently, allowing for quicker assessments of biodiversity (Cristescu and Hebert 2018).
These methodologies hold significant value in the identification of uncommon or enigmatic species, as well as in the evaluation of the effects of environmental alterations on genetic variability.
Remote sensing and monitoring Satellite images and airborne drones are examples of remote sensing technologies that offer extensive capabilities for monitoring habitats, land-use changes, and species distributions over vast regions.
These tools capture high-resolution images that can reveal changes in vegetation cover, land use, and habitat fragmentation over time (Lahoz-Monfort and Magrath 2021).
This ongoing monitoring capability allows conservationists to respond quickly to threats such as deforestation, wildfires, and illegal wildlife activities, thereby enhancing the effectiveness of conservation efforts.
Remote sensing data can be processed using AI to identify habitat changes with greater accuracy (Lahoz-Monfort and Magrath 2021).
These technological advancements enable the ongoing monitoring of environmental fluctuations, hence facilitating prompt reactions to various challenges such as deforestation, wildfires, and illicit wildlife operations (Jiménez López and Mulero-Pázmány 2019; Buchelt et al.
State-of-the-art sensors and imaging have the capability to identify alterations at the micro-habitat level, which is essential for implementing focused conservation measures (Simaika et al.
Data-driven conservation planning Data-driven conservation planning leverages extensive datasets derived from many sources, including remote sensing, field observations, and genetic data (Shaikh et al.
These methods analyze spatial patterns and relationships within the data to inform strategic decisions(Shaikh et al.
By forecasting the most effective locations for conservation measures and evaluating the potential results of various management systems, this methodology allows for the optimization of resource allocation (Xiang et al.
This ensures that conservation efforts are both efficient and impactful.
Exploration of AI in conservation The integration of deep learning for species identification, computer vision for habitat assessment, and predictive analytics for forecasting species migration into ecological research and management results in the transformation of conservation methods through the utilization of AI.
For instance, AI algorithms have been employed to analyze camera trap images for species identification in projects like Snapshot Serengeti, leading to improved data collection efficiency (Lamba et al.
AI systems have the capability to handle and examine extensive amounts of environmental data, ranging from identifying species in camera trap images to detecting patterns in temporal data (Lamba et al.
2019; Green et al.
This enables the making of conservation decisions in real-time (Ditria et al.
AI has been employed to automate the identification and quantification of species, assess the condition of habitats, and forecast the migration patterns of animals across various terrains, thereby furnishing conservationists with a versatile set of tools.
Machine learning models for species identification and behavior prediction The AI models have demonstrated notable efficacy in the domains of species identification and behavior prediction (Merabet et al.
Through the examination of data derived from many sources, including audio recordings and field-captured images, these models possess the capability to effectively and precisely classify species, even within intricate ecological habitats (Zhang et al.
In addition, predictive models have the ability to forecast the behaviors and movements of species, which can assist in the management of conflicts between humans and wildlife, as well as in the creation of wildlife corridors that improve connection between environments that are fragmented (Nandutu et al.
AI-driven data analytics for habitat monitoring and threat assessment AI-driven data analytics transform habitat monitoring and threat assessment by combining several data streams to offer a comprehensive perspective on the health of the ecosystem.
The aforementioned techniques has the capability to accurately examine alterations in vegetation patterns, water quality, and land use, hence providing valuable insights into the effects of human-induced stresses on natural environments (Chowdhury et al.
AI models play a crucial role in forecasting forthcoming environmental conditions and evaluating prospective hazards, hence facilitating proactive conservation efforts (Isabelle and Westerlund 2022; Akter 2024).
Autonomous systems for invasive species control Autonomous systems, such as unmanned aerial vehicles (UAVs) and robotic devices, are utilized for the purpose of managing invasive species, which pose a significant risk to biodiversity.
These systems are capable of functioning in difficult conditions to eliminate or control exotic species, administer specific pesticides, or revive indigenous plants (Gonzalez et al.
2016; Martinez et al.
The incorporation of AI allows these systems to effectively detect and focus on particular species, resulting in decreased labor expenses and mitigated human influence on delicate ecological systems (Galaz et al.
Case studies highlighting AI in conservation The integration of AI into conservation efforts has led to significant advancements in monitoring endangered species (Amur leopards in Russia) and managing habitats effectively (Rozhnov et al.
The video traps were strategically placed by researchers inside the habitat of leopards in order to facilitate the automated identification of individual animals based on their distinct coat patterns (Alibhai et al.
By using AI algorithms that have been trained on a vast collection of photos, it is possible to differentiate leopards from other animals and effectively track their population and overall well-being.
This technology enables uninterrupted, instantaneous monitoring without the need for human involvement, resulting in a substantial decrease in the labor and expenses typically linked to such endeavors.
Consequently, it plays a vital role in updating population estimates and assisting conservation strategies.
Consequently, it plays a vital role in updating population estimates and assisting conservation strategies, as demonstrated by studies showing improved population monitoring and management outcomes.
For example, research highlights how AI-driven camera trap systems have enabled real-time tracking of Amur leopards, leading to more accurate population estimates and enhanced conservation actions (Alibhai et al.
Similarly, a study found that AI analysis of satellite imagery significantly improved the detection of deforestation activities in the Amazon, allowing for timely interventions that contributed to better forest conservation and species protection (Casas and Torres 2023).
Furthermore, the cost-effectiveness of AI technologies allows for savings that can be reinvested into further conservation efforts.
For instance, the automation of data collection processes reduces labor costs, enabling funds to be redirected toward habitat restoration projects or community engagement initiatives (Albuquerque et al.
AI has the capacity to significantly improve project efficiency, successfully handle extensive information, and provide timely insights crucial for preserving species and ecosystems.
The effective use of AI technology in these situations highlights their usefulness in tackling intricate conservation issues across various ecological environments.
AI has been used for ecological management in the Amazon rainforest.
Conservationists used AI to examine extensive satellite footage in order to promptly identify deforestation operations, alterations in land utilization, and disruptions.
The training of machine learning models aimed to distinguish between natural and anthropogenic alterations occurring within the ecological system (Casas et al.
The utilization of AI technology has facilitated proactive management strategies by accurately forecasting deforestation patterns and promptly detecting illicit activities, surpassing conventional approaches.
This has played a crucial role in influencing policy choices and allocating resources for conservation endeavors (Albuquerque et al.
Moreover, AI has revolutionized marine conservation efforts in the Coral Triangle region of Southeast Asia (Hoeksema 2007).
AI was used by scientists to assess and map coral reefs using photographs captured by underwater drones (McLeod et al.
The AI was assigned the responsibility of detecting coral health indicators, such as instances of bleaching, and evaluating the dynamics of fish populations.
The use of this program has facilitated a much expedited and precise evaluation of reef well-being in comparison to conventional techniques, hence enabling prompt treatments (Clifton & Foale 2017).
In addition, the use of AI insights is employed in the optimization of conservation results by designing marine protected areas that are more successful.
AI has the capacity to significantly improve project efficiency, successfully handle extensive information, and provide timely insights that are crucial for the preservation of species and ecosystems.
The effective use of AI technology in these situations highlights their usefulness in tackling intricate conservation issues in many ecological environments.
Discussion Comparative analysis of classical and modern approaches An examination of classical and modern approaches to biodiversity conservation highlights the unique advantages and difficulties associated with each paradigm.
While traditional methods have been effective in creating protected areas, they often lack flexibility; modern technologies like AI offer adaptive solutions that can quickly respond to environmental changes (Anderson and Jenkins 2006).
Traditional methods for addressing these challenges include establishing protected areas and implementing restoration projects aimed at reconnecting fragmented habitats.
For instance, wildlife corridors have been created to facilitate species movement between isolated habitats, thereby enhancing genetic diversity and resilience (Noss et al.
The utilization of these techniques has played a crucial role in regions such as the Galapagos Islands, where rigorous conservation efforts have effectively preserved distinct species (Muñoz-Viñas 2012).
Despite these conventional strategies, limitations remain in their scalability and adaptability to rapidly changing environments.
Table 1 explain the comparative analysis of traditional and AI based conservation.
Table 1 Comparative analysis of traditional and AI-enhanced approaches to biodiversity conservation Full size table In contrast, contemporary methods utilize technology progress such as genetic technologies, AI, and remote sensing to overcome these constraints (Marvin et al.
2016; Kerry et al.
2022; Singh et al.
These tools provide flexible, expandable, and accurate approaches for conservation, easily adjusting to the intricacies of worldwide environmental issues (Shwartz et al.
AI-powered models have revolutionized conservation tactics by offering real-time data and predicted insights for habitat and species monitoring, hence improving decision-making processes.
AI has been employed in the Amazon jungle to forecast deforestation patterns and detect illicit logging activities, surpassing the efficiency of traditional methods (Raihan 2023).
AI technologies can significantly enhance habitat preservation efforts by providing real-time data analytics for monitoring habitat conditions and predicting changes based on environmental variables.
For example, machine learning models can analyze satellite imagery to identify areas at risk of degradation and prioritize them for conservation interventions (Ditria et al.
The incorporation of contemporary technologies in the field of conservation also facilitates the utilization of extensive data analysis capabilities that exceed conventional approaches (Pimm et al.
Initiatives like as eBird utilize citizen science and AI to collect and analyze worldwide bird observation data, providing valuable information on migration patterns and population dynamics that guide conservation efforts at both local and global levels (Kelling et al.
2012; Johnson et al.
The aforementioned demonstrates the potential of contemporary methodologies to supplement traditional techniques, hence augmenting their scope and effectiveness (Di Marco et al.
Moreover, contemporary conservation methods can more effectively address the socio-economic dimensions of biodiversity preservation (De Groot et al.
Predictive modeling and real-time monitoring are utilized to facilitate more sophisticated management of human-wildlife interactions, thereby mitigating the constraints associated with traditional approaches that frequently encounter difficulties in community engagement and socio-economic integration (Du et al.
AI models employed in wildlife corridors in Africa play a crucial role in forecasting and alleviating human-elephant conflicts, a task that cannot be accomplished only by static protected zones (Morrison 2019).
While AI has shown great promise in enhancing biodiversity conservation efforts, several emerging challenges must be addressed to ensure its effective application in the future.
As AI systems rely heavily on vast amounts of data, concerns regarding data privacy and security are paramount.
Ensuring that sensitive ecological data is protected from misuse is critical.
AI algorithms can inherit biases present in training data, which may lead to skewed results and misinformed conservation strategies.
Addressing algorithmic bias is essential for equitable conservation outcomes.
The implementation of AI technologies often requires significant financial and technical resources, which may not be available in all regions, particularly in developing countries.
Ensuring equitable access to these technologies is vital.
Synergies between traditional methods and AI technologies The potential synergy between the integration of AI technologies with traditional conservation methodologies offers a significant opportunity to increase biodiversity conservation by capitalizing on the respective strengths of both approaches (White et al.
The convergence of AI's analytical powers with the grounded, locality-specific actions of classical methods is exemplified by a range of real-time applications.
An illustrative instance is the utilization of AI to enhance the administration of protected areas (Fig.
AI algorithms have greatly improved traditional tactics, such as patrol routes and anti-poaching operations, by accurately predicting poaching hotspots using historical data and real-time inputs (Cronin et al.
2021; Chisom et al.
Predictive modeling in African national parks assists rangers by predicting the probability of poaching episodes, enabling proactive measures that are consistent with conventional patrolling methods (Sarkar et al.
3 figure 3 The integration of AI in biodiversity conservation.
A Depicts how AI technologies, such as data analysis and monitoring tools, are being incorporated to enhance conservation efforts.
B Highlights the diversity of species, and C shows the projected forest cover loss over time, emphasizing the urgency of conservation efforts.
D Demonstrates the use of AI-powered drones and robotic technologies for wildlife monitoring, enabling real-time habitat assessment and species tracking.
E Visualizes the projected forest cover loss from 1986 to 2034, further underscoring the need for intervention.
Lastly, E presents a circular representation of various conservation technologies and strategies that combine traditional approaches with modern AI-driven methods to improve biodiversity preservation  Full size image Additionally, AI technology can provide efficient assistance for the community-based conservation programs, which are a conventional method that incorporates indigenous knowledge and practices related to resource management (Ruiz-Mallén and Corbera 2013).
The effective monitoring of environmental changes and animal trends can be achieved by communities through the utilization of AI-driven data analytics (Chisom et al.
The utilization of AI technologies in Nepal has been implemented to analyze photos and data obtained from community-managed forests (Paudel and Sah 2015).
This utilization aids local stakeholders in making well-informed decisions regarding sustainable practices and intervention measures.
Furthermore, AI significantly improves the efficacy of habitat restoration initiatives that have conventionally relied on manual monitoring and labor-intensive procedures (Haq et al.
The utilization of AI-powered drones and remote sensing technologies has become prevalent in the mapping and monitoring of restoration work across extensive regions.
These technologies offer high-resolution data that effectively inform reforestation initiatives and facilitate biodiversity evaluations (Lock et al.
The utilization of this technology was successfully implemented in the Amazon Rainforest, where AI-driven drones evaluate the results of reforestation efforts and assist in optimizing planting techniques to guarantee the restoration of the ecological system (Hodel 2023).
Challenges and limitations of implementing AI in conservation Although the incorporation of AI in conservation has demonstrated encouraging progress, it also poses several obstacles and constraints that require thorough assessment (Sarkar et al.
A notable obstacle is to the caliber and accessibility of data necessary for the training of AI models (Hu and Xu 2023).
In certain biodiversity hotspots, such as tropical forests, the limited availability of data can hinder the efficacy of AI applications.
The efficacy of species identification and behavioral prediction models is contingent upon the size and caliber of the input data, which may be limited or insufficient in biodiversity areas (Sarkar and Chapman 2021).
Another constraint pertains to the expenses and intricacy associated with implementing and up keeping AI technologies, particularly in distant or underprivileged regions.
The establishment and continuous upkeep of sensors, drones, and other AI-powered devices can pose significant financial and technological challenges, necessitating specific expertise that may not be readily accessible within the local context (Bibri et al.
Long-term field studies aided by AI in the conservation of marked ungulates encounter logistical problems, such as the requirement for ongoing finance and human resources (Eikelboom 2021).
In addition, the dependence on AI might give rise to ethical considerations, namely pertaining to monitoring and privacy (Kochupillai et al.
The utilization of AI-powered cameras and tracking equipment in wildlife monitoring gives rise to concerns regarding the effects on animal welfare and the ethical implications of continuous surveillance (Basu and Nath 2024).
The integration of AI in conservation efforts necessitates a careful equilibrium between technological encroachment and the preservation of wildlife's natural behavior and environment.
Moreover, AI models can occasionally function as opaque systems, with decision-making procedures that lack transparency or comprehensibility for conservation practitioners (Wünscher and Engel 2012).
The absence of transparency can impede the establishment of confidence and acceptance of AI technologies, as it is imperative that decisions pertaining to species conservation and habitat management are comprehensible to a wide range of individuals, including those lacking technical proficiency (Raihan 2023).
AI technologies have the potential to worsen inequities if they are not implemented with careful consideration (Dauvergne 2020).
In specific circumstances, the use of high-tech solutions has the potential to redirect financial resources away from conventional conservation approaches that are seen more culturally suitable or environmentally sustainable (Lama and Sattar 2002).
This phenomenon has the potential to result in a disparity in technological availability, wherein more affluent conservation initiatives possess advanced tools, while economically disadvantaged regions fall behind.
Ethical considerations and long-term sustainability of AI-driven conservation The ethical implications and enduring viability of AI-driven conservation are contingent upon various interconnected aspects that involve the integration of ethical theory and practical implementation (Kochupillai et al.
Environmental ethics must fundamentally influence the implementation of AI in conservation initiatives, guaranteeing that technology progress does not overshadow ecological or social principles (Nandutu et al.
Ethical AI in environmental situations frequently entails making intricate choices that strike a balance between technology capabilities, ecological consequences, and human welfare.
The environmental impact of AI technologies themselves is a significant concern when considering the sustainability of AI-driven conservation efforts (Akter 2024).
AI systems, especially those that utilize huge data centers and substantial computational resources, make a substantial contribution to carbon emissions (Gaur et al.
Therefore, it is imperative to create' sustainable AI' that takes into account the ecological expenses associated with technology (Akter 2024).
The utilization of advancements in AI hardware and software to mitigate energy consumption, as well as the integration of renewable energy sources to support power-intensive AI operations.
Furthermore, ethical AI must tackle concerns regarding prejudice, unfair treatment, and the possibility of worsening disparities (Ozmen Garibay et al.
Within the realm of conservation, it is imperative to guarantee that AI does not unintentionally exhibit bias towards some species or ecological systems, while disregarding others (Ditria et al.
Additionally, AI must not disregard the perspectives and entitlements of local communities impacted by conservation initiatives (Taylor et al.
For example, the utilization of AI in the administration of animal territories and parks should not result in the implementation of exclusionary measures that isolate indigenous communities who may depend on these lands for their sustenance.
An additional ethical consideration arises from the potential danger of over dependence on AI solutions, which could result in a disengagement from conventional conservation techniques and knowledge systems.
It is necessary to adopt a well-rounded strategy that utilizes AI to augment, rather than supplant, conservation initiatives headed by humans.
This entails actively involving stakeholders at every level to guarantee the responsible and transparent utilization of AI tools.
Conclusion This study has presented the interactions between classical and modern methodologies in the field of biodiversity conservation, emphasizing the specific advantages and obstacles that each approach brings in the pursuit of safeguarding the biological diversity of our world.
Classical approaches, which are based on well-established techniques such as the establishment of protected areas and the implementation of species-specific management, provide a robust framework of proven strategies.
However, these methods frequently lack the adaptability required to effectively respond to swift environmental transformations and intricate socio-economic circumstances.
In contrast, contemporary methodologies, driven by advancements in AI and associated technologies, introduce a sense of dynamism and scalability to conservation endeavors.
These methodologies offer tools capable of analyzing extensive datasets and automating intricate operations with unparalleled accuracy.
The incorporation of AI into conservation methods signifies a revolutionary change that has the capacity to improve the extent and efficiency of conservation efforts greatly.
AI powered solutions enhance the process of gathering and examining data, while also facilitating live monitoring and predictive analytics.
This empowers conservationists to anticipate and address possible hazards before they materialize.
However, further research should be conducted to investigate the potential synergies between classical and modern AI techniques.
By adopting a comprehensive strategy that acknowledges the value of conventional conservation techniques as well as the capabilities of contemporary technologies, it is possible to envision the simultaneous attainment of ecological preservation and sustainable development objectives.
Abstract:The  escalating  environmental  crises  of  the  21st  century—ranging  from  deforestation  and  climatechange to biodiversity loss and ocean acidification—have underscored an urgent need for innovative, scalable,and data-driven solutions.
Artificial Intelligence (AI) has emerged not only as a powerful technological forcebut also as a vital enabler in the global pursuit of environmental sustainability.
By harnessing AI’s capabilitiesin predictive analytics, pattern recognition, real-time monitoring, and automation, conservationists, researchers,and policy makers are now equipped with unprecedented tools to mitigate environmental degradation.
This paperexplores the multifaceted ways in which AI is transforming the landscape of environmental conservation, withan emphasis on practical applications, case studies, ethical considerations, and future prospects.
It argues thatwhile AI is not a panacea, it is an indispensable ally in the fight to protect Earth’s natural systems.Keywords:Artificial Intelligence, Environmental Monitoring, Climate Change, Conservation Technology, Bio-diversity, Ecological Forecasting, Sustainable Development, AI for Earth, Planetary Health, Machine Learningfor Nature1.
IntroductionThe  environmental  crises  of  the  21st  century  are  not  confined  to  isolated  incidents  of  ecological  degra-dation—they  represent  a  complex,  systemic  unraveling  of  the  planet’s  life-support  systems  [1],  [2],  [3].From the scorching heatwaves that render parts of the Earth uninhabitable, to the unprecedented scale ofpolar ice melt threatening to inundate coastal megacities, the Anthropocene epoch is defined by the depthand  interconnectedness  of  human  impact  on  nature  [4],  [5].
Climate  change,  biodiversity  collapse,  soilerosion, desertification, air and water pollution, deforestation, and the acidification of oceans are unfoldingsimultaneously  and  reinforcing  one  another  in  nonlinear  ways  [6].
This  convergence  of  environmentalstressors is testing the resilience of natural systems and human societies alike [7], [8].Traditional environmental conservation practices—often centered on protected area designations, species-specific  interventions,  and  community-level  environmental  stewardship—  remain  vital  but  increasinglyinsufficient  [9].
These  methods  tend  to  be  reactive  rather  than  predictive,  local  rather  than  global,  andmanual rather than data-driven.
Their effectiveness diminishes in the face of rapidly changing conditions,exponential population growth, and transboundary ecological threats [10], [11].
What is needed is a shift inparadigm—a reimagining of conservation through the lens of intelligence, scale, speed, and adaptiveness.Artificial  Intelligence  (AI)  has  emerged  as  one  of  the  most  transformative  tools  of  our  era,  offering  anew mode of engagement with the natural world [12], [13].
AI’s strength lies in its capacity to process vastvolumes  of  data  across  spatial,  temporal,  and  thematic  scales.
Unlike  human  cognition,  which  struggleswith high-dimensional complexity, AI can identify hidden patterns, optimize decisionmaking, learn fromcontinuous inputs, and deliver real-time insights that are actionable and scalable [14], [15].
When appliedto environmental challenges, AI becomes a multidimensional force— simultaneously a sensor, a predictor,Vol.
01, No. 02, June 2025Page 1 International Journal of Artificial Intelligence for ScienceSaving the Planeta monitor, a modeler, and, crucially, an enabler of change [16], [17].Environmental systems—forests, oceans, wildlife populations, atmospheric conditions, hydrological net-works—generate enormous amounts of data daily [18], [19].
Satellites orbiting the Earth collect terabytesof imagery and spectral data every minute.
Remote sensors embedded in rivers, forests, and cities monitoreverything  from  soil  moisture  to  noise  pollution  [20].
Wildlife  conservationists  deploy  camera  traps  andbioacoustic devices in remote regions to track elusive species [21], [22].
Governments and NGOs generatereams  of  policy  data,  while  citizens  contribute  voluntarily  to  crowd-sourced  environmental  monitoringplatforms  [23],  [24].
Yet  much  of  this  data  remains  underutilized  due  to  the  limitations  of  traditionalanalysis techniques.AI bridges this gap by turning overwhelming information into practical intelligence.
Machine learningmodels can identify illegal mining activity from satellite imagery [25], [26].
Natural language processingcan  scan  thousands  of  environmental  reports  and  extract  critical  trends.
Deep  learning  algorithms  canidentify  a  bird’s  call  or  a  frog’s  croak  from  rainforest  soundscapes  [27].
Predictive  models  can  forecastdesertification zones years in advance, allowing for early mitigation strategies.
Reinforcement learning candynamically adjust conservation strategies based on ecological feedback [28].What makes AI particularly powerful in environmental applications is its interdisciplinary adaptability[29], [30].
AI systems can be integrated across sectors—agriculture, transportation, energy, urban planning,forestry, and marine management—to produce synergistic environmental outcomes [31].
AI can simultane-ously support precision agriculture to reduce land use, monitor traffic patterns to reduce urban emissions,manage smart grids for clean energy distribution, and track illegal fishing in marine reserves [32], [33].Moreover, AI’s role in environmental justice is becoming increasingly visible.
Historically marginalizedand vulnerable communities often bear the brunt of environmental damage [34].
AI can illuminate hiddenpollution hotspots in low-income neighborhoods, provide early warning systems for climate-induced dis-asters [35], [36], and help design inclusive conservation strategies that account for social, economic, andcultural dimensions [37].Despite  its  promise,  AI  also  presents  ethical  and  operational  challenges  in  conservation.
The  risk  ofalgorithmic  bias,  surveillance  overreach,  lack  of  transparency,  and  unequal  access  to  technology  canundermine the very sustainability goals AI aims to serve [38], [39].
There is an urgent need for ethical AIframeworks, inclusive data governance, and interdisciplinary partnerships that ensure AI serves ecologicaland societal well-being rather than corporate or geopolitical interests.This article presents a comprehensive exploration of how Artificial Intelligence is reshaping environmen-tal conservation in the real world [40].
Drawing from real-time case studies, crosscontinental technologies,research  projects,  and  policy  implementations,  we  analyze  how  AI  is  being  leveraged  to  fight  climatechange,  halt  biodiversity  loss,  optimize  natural  resource  use,  predict  ecological  trends,  and  support  theUnited Nations Sustainable Development Goals (SDGs).We  will  examine  AI’s  role  not  as  a  distant  technological  fantasy  but  as  an  active  agent  in  today’sconservation efforts—from using satellite-based analytics to detect illegal deforestation in the Amazon [25],[41], to deploying drones powered by AI for coral reef mapping in the Pacific [32], [42], to implementingAI-enhanced sensors for real-time air quality monitoring in African megacities [35], [43].By doing so, this article not only highlights the transformative potential of AI in environmental sciencebut also calls for critical engagement, interdisciplinary innovation, and ethical stewardship to ensure thatthis  powerful  technology  becomes  a  catalyst  for  planetary  restoration  and  not  an  amplifier  of  ecologicalinequality.2. Applications of AI in Environmental ConservationArtificial Intelligence has become a cornerstone technology in addressing complex, large-scale environmen-tal  issues.
Its  ability  to  process  diverse  and  voluminous  datasets  across  temporal  and  spatial  dimensionsenables  new  forms  of  ecological  insight,  prediction,  and  automation.
In  this  section,  we  examine  fivemajor  application  domains  where  AI  has  already  demonstrated  substantial  impact.
Figure  1  summarizesthe estimated effectiveness of AI in each area.Vol.
01, No. 02, June 2025Page 2 International Journal of Artificial Intelligence for ScienceSaving the Planet2.1. Biodiversity MonitoringTracking  animal  populations  over  vast  and  remote  landscapes  has  traditionally  required  labor-intensivefieldwork.
AI  has  transformed  this  process  by  enabling  automated  species  identification  and  behavioralanalysis.•Camera Trap Image Analysis:Convolutional neural networks (CNNs) trained on millions of labeledwildlife images can detect and classify species in camera trap footage with high accuracy.
This allowsfor continuous monitoring of biodiversity hotspots with minimal human intervention.•Bioacoustics:In  regions  like  the  Amazon  and  Southeast  Asia,  AI  models  now  analyze  rainforestsoundscapes in real time to identify species by their vocalizations.
This approach is especially usefulfor monitoring nocturnal, cryptic, or endangered species that are hard to observe visually.Notably,  Google’s  AI  for  Social  Good  initiative  has  supported  the  deployment  of  such  tools  to  detectillegal logging by recognizing acoustic patterns associated with chainsaws and human activity [23], [44].2.2. Climate Change ModelingTraditional  climate  models  are  computationally  expensive  and  often  limited  in  resolution  or  temporalfrequency.
AI models, particularly deep learning and physics-informed machine learning frameworks, arenow used to:•Generate short-term forecasts of sea-level rise and temperature anomalies.•Downscale global climate models to regional resolutions.•Integrate satellite, sensor, and historical data into cohesive simulations.Microsoft’s AI for Earth program has facilitated projects that use AI to map global land cover change,predict droughts, and identify areas at risk of heatwaves or flooding [45], [46].2.3. Deforestation and Land UseAI  has  proven  highly  effective  in  detecting  unauthorized  deforestation,  land  conversion,  and  habitatfragmentation.
High-resolution satellite imagery processed by deep learning models enables near-real-timemonitoring of land use changes.Global  Forest  Watch,  managed  by  the  World  Resources  Institute,  utilizes  AI  to  detect  tree  coverloss, providing timely alerts to governments and NGOs. These systems allow for rapid enforcement andconservation action, particularly in tropical forests such as the Amazon and Congo basins [25], [47].2.4. Ocean Health and Marine ConservationThe health of marine ecosystems is under threat from coral bleaching, overfishing, and plastic pollution.AI models help by:•Classifying coral reef conditions from underwater imagery.•Predicting fish migration routes and breeding seasons using historical and sensor data.•Identifying oceanic plastic patches using drone and satellite data.The  Allen  Coral  Atlas  uses  AI  to  generate  high-resolution  coral  maps,  aiding  restoration  efforts  inregions like the Great Barrier Reef and Micronesia [32], [48].2.5. Waste Management and Pollution ControlIn urban and industrial contexts, AI is used to enhance environmental sustainability through:•Smart waste routing based on real-time bin fill levels.•Automated waste sorting using computer vision and robotics.•AI-driven detection of pollution hotspots in water bodies or air using IoT sensors.In India, AI-based systems have been used to monitor pollution in the Ganges River, identifying sourcesof  illegal  dumping  and  measuring  chemical  discharge  levels  [35],  [49].
These  systems  not  only  improvepolicy enforcement but also raise public awareness through accessible visualizations.Vol.
01, No. 02, June 2025Page 3 International Journal of Artificial Intelligence for ScienceSaving the PlanetFig.
Estimated effectiveness of AI across five key environmental application domains.TABLE IOVERVIEW  OFAI APPLICATIONS INENVIRONMENTALCONSERVATIONDomainAI TechniquesRepresentative ProjectsEnvironmental ImpactBiodiversity MonitoringImage    classification,    SoundrecognitionGoogle  AI  for  Social  Good,Wildlife InsightsAutomated   species   tracking,Poaching preventionClimate Change ModelingDeep   learning,   Data   fusion,Spatiotemporal forecastingMicrosoft  AI  for  Earth,  Cli-mateNetHigh-resolution   climate   pre-dictions, Disaster planningDeforestation   and   LandUseSatellite  image  segmentation,Change detectionGlobal Forest WatchReal-time  deforestation  alerts,Enforcement optimizationOceanMarine    Conservation,    Coralimage    classification,    Plasticdetection via dronesAllen Coral AtlasCoral reef health maps, Marinedebris mitigationWaste  and  Pollution  Con-trolIoT sensors, Computer vision,Pattern recognitionGanges  River  Monitoring  (In-dia), Smart Bin SystemsIllegaldumpingdetection,Smart recycling3.
Case StudiesArtificial  Intelligence  has  moved  from  experimental  prototypes  to  real-world  deployments,  deliveringmeasurable improvements in conservation effectiveness.
This section highlights two representative appli-cations—monitoring deforestation in the Amazon and improving climate modeling in the Arctic—whereAI has demonstrably changed environmental management practices.3.1. AI in the Amazon RainforestRainforest Connection (RFCx), a California-based nonprofit, employs AI-powered acoustic monitoring todetect  illegal  logging  activities  in  protected  Amazonian  regions  [21],  [50].
Solar-powered  smartphonesequipped with microphones are hidden in forest canopies, capturing ambient sounds.
These audio streamsare  processed  in  real  time  by  machine  learning  models  trained  to  recognize  chainsaws,  trucks,  andhuman voices associated with unauthorized deforestation.
Authorities receive instant alerts, enabling rapidresponse.Field  reports  indicate  that  regions  using  RFCx  technology  have  seen  up  to  a  60%  reduction  in  illegallogging  incidents  within  a  year  of  deployment.
The  integration  of  real-time  data  and  AI  inference  hasshifted forest protection from reactive patrols to proactive intervention.3.2. AI and Arctic Ice Melt PredictionIn  polar  regions,  the  National  Snow  and  Ice  Data  Center  (NSIDC)  uses  AI  to  enhance  the  precision  ofsea  ice  modeling  [18],  [51].
Traditional  climate  models  struggle  with  long  processing  times  and  highVol.
01, No. 02, June 2025Page 4 International Journal of Artificial Intelligence for ScienceSaving the Planeterror rates due to data sparsity and complex atmospheric-oceanic interactions.
AI models ingest satelliteimagery,  ocean  salinity,  temperature  profiles,  and  historic  melt  patterns  to  generate  fast,  high-resolutionforecasts.The adoption of deep learning algorithms has reduced predictive error rates from over 20% to under 5%in  some  scenarios.
These  insights  support  policymakers  in  making  informed  decisions  on  infrastructureplanning and ecological protection in vulnerable Arctic regions.3.3. Comparative Results of AI ImpactTo illustrate the tangible impact of AI in these two domains, Figure 2 compares key indicators—deforestationevent frequency and Arctic model error rates—before and after AI integration.
The visualized data high-lights how AI enables earlier detection, improved accuracy, and accelerated environmental responses.Fig.
Impact of AI in monitoring deforestation in the Amazon and improving Arctic ice melt predictions.4. Challenges and Ethical ConsiderationsWhile the benefits of AI in conservation are clear, several ethical and operational challenges remain:•Data Bias and Gaps:Many  regions  lack  quality  data,  leading  to  biased  models  that  reflect  richer,well-studied ecosystems while ignoring marginalized or understudied regions [10], [52].•Algorithmic Transparency:Conservationists  and  policymakers  must  be  able  to  interpret  and  trustthe AI’s decisions.
Black-box models may undermine trust or lead to incorrect interventions.•Surveillance Risks:Technologies such as drones and remote sensors, though used for conservation,could potentially be repurposed for surveillance or misuse if not properly governed [38], [53].•Displacement of Local Knowledge:Over-reliance on AI could sideline indigenous or community-based conservation practices that have deep ecological relevance.5. Future DirectionsAs  AI  technologies  mature,  their  environmental  applications  will  become  more  autonomous,  integrated,and collaborative.
Some emerging frontiers include:•Swarm robotics for reforestation:Autonomous drones planting trees in degraded landscapes.Vol.
01, No. 02, June 2025Page 5 International Journal of Artificial Intelligence for ScienceSaving the PlanetTABLE IIETHICALCHALLENGES OFAIINENVIRONMENTALCONSERVATIONChallengeCauseImplications / RisksData BiasUneven data distribution across re-gionsExcludes vulnerable ecosystems, skews predictionsLack of TransparencyUse of black-box modelsDifficult to audit, erodes stakeholder trustSurveillance MisuseDual-use drone/sensor techViolates privacy rights, may suppress local commu-nitiesDisplacement of Local Knowl-edgeOverreliance on automated systemsMarginalizes indigenous ecological wisdom•AI-powered ecological policy modeling:Helping  governments  simulate  the  long-term  impact  ofconservation laws or infrastructure projects [54], [55].•Hybrid intelligence systems:Combining AI with human expertise, citizen science, and indigenousknowledge to form adaptive conservation ecosystems.The  development  of  open  environmental  AI  platforms,  similar  to  open-source  software,  could  democ-ratize access to tools and encourage cross-border cooperation [38], [56], [57].6.
Discussion6.1. AI as a Transformative Force for Environmental ProtectionArtificial  Intelligence  (AI)  is  no  longer  a  futuristic  concept  confined  to  academic  laboratories  or  exper-imental  domains—it  has  become  a  central  force  reshaping  how  humanity  understands,  interacts  with,and  ultimately  protects  the  natural  world.
As  the  planet  teeters  on  the  edge  of  ecological  collapse,  withecosystems  unraveling  and  biodiversity  vanishing  at  rates  unseen  in  recorded  history,  the  urgency  fortransformative  solutions  cannot  be  overstated.
Amidst  this  crisis,  AI  emerges  not  as  a  panacea,  but  as  adynamic, adaptive, and unprecedentedly powerful catalyst for environmental preservation and restoration.6.2. Expanding the Scale and Scope of ConservationAI’s  strength  lies  in  its  ability  to  reveal  the  unseen,  forecast  the  unpredictable,  and  manage  the  unman-ageable.
From detecting illegal deforestation in the Amazon using satellite imagery and deep learning, todecoding  whale  songs  through  acoustic  machine  learning  models  in  the  deep  sea,  to  guiding  water  con-servation strategies via AI-powered precision agriculture in drought-stricken regions—AI is fundamentallyaltering the scale and scope of what conservationists can accomplish.
What once took decades of manualfieldwork and extensive funding can now, through AI-driven automation and analysis, be achieved in daysor even hours, unlocking new realms of possibility in environmental science and action.6.3. Human-Centered Intelligence: Scaling Empathy and CollaborationYet, the true power of AI in conservation does not lie merely in its computational muscle or in the eleganceof its algorithms—it lies in its ability to amplify human intent and ecological consciousness.
At its best, AIis not a detached, clinical tool; it is a digital extension of our collective will to care, to repair, and to protect.It  enables  collaboration  between  indigenous  knowledge  and  cutting-edge  technology,  between  grassrootsactivism and global policy frameworks, between micro-level ecological feedback and macro-level planetarysystems thinking.
It can scale empathy into strategy and turn data into decisive action.6.4. Ethical Imperatives and Structural ConstraintsHowever, this transformative potential comes with a critical caveat: AI must be guided by ethics, inclusion,and  ecological  humility.
Technology,  however  powerful,  does  not  operate  in  a  vacuum.
Algorithms  areonly  as  equitable  as  the  data  they  are  trained  on,  and  insights  are  only  as  meaningful  as  the  actionsthey inform.
If left unregulated or used solely in service of profit, AI could deepen existing inequalities,reinforce biases, and be co-opted into systems of surveillance and ecological exploitation.
Conservation AImust therefore be embedded within a framework that prioritizes transparency, open access, justice, and theVol.
01, No. 02, June 2025Page 6 International Journal of Artificial Intelligence for ScienceSaving the Planetvoices  of  those  most  impacted  by  environmental  degradation—especially  Indigenous  communities,  ruralpopulations, and climate-vulnerable nations.6.5. The Irreplaceable Role of Human WillMoreover,  while  AI  can  monitor  species,  model  climate  trends,  and  optimize  conservation  logistics,  itcannot replace the moral imperative to act.
Political inertia, economic interests, and global inequity continueto  be  formidable  barriers  to  environmental  progress.
AI  cannot  manufacture  the  political  will  to  phaseout  fossil  fuels,  nor  can  it  legislate  protection  for  endangered  ecosystems.
It  cannot  instill  in  society  areverence  for  nature  or  a  commitment  to  long-term  ecological  balance.
These  are  fundamentally  humanresponsibilities, rooted in values, ethics, and collective decision-making.6.6. A Strategic Ally, Not a SubstituteThus, AI should not be viewed as a substitute for ecological stewardship, but as a strategic ally—a forcemultiplier  that  augments  our  capacity  to  protect  what  matters  most.
When  aligned  with  science,  policy,community  wisdom,  and  environmental  ethics,  AI  has  the  power  to  usher  in  a  new  era  of  planetarymanagement—one that is smarter, faster, and more responsive than any system we’ve previously had.
Thisalignment must be deliberate, inclusive, and future-focused.6.7. A Moral Compass for the Planetary FutureAs we enter a decisive decade for the planet, the stakes could not be higher.
The choices we make nowwill reverberate for generations to come.
In this moment of unprecedented risk and remarkable possibility,AI stands out not only as a tool of technological innovation but as a moral and strategic compass—guidingus toward regeneration rather than extraction, toward harmony rather than dominance, and toward a futurewhere humanity is no longer an adversary of nature, but its guardian and partner.If developed and deployed with conscience, compassion, and collaboration, Artificial Intelligence maywell become one of the most effective instruments in our existential quest to restore the Earth.
It has thepotential to serve not the ambition of control, but the vision of coexistence—one in which data, intelligence,and humanity converge to heal the only home we have.7. ConclusionArtificial  Intelligence  (AI)  has  emerged  as  a  transformative  force  in  addressing  pressing  environmentalchallenges.
From  monitoring  biodiversity  and  predicting  climate  trends  to  combating  deforestation  andmanaging  pollution,  AI  offers  scalable,  data-driven  solutions  that  enhance  conservation  efforts  acrossecosystems.
However, to fully realize its potential, AI must be developed and deployed with transparency,inclusivity, and ethical responsibility.
As we face an uncertain ecological future, the integration of AI intoenvironmental  science  presents  both  a  technological  opportunity  and  a  moral  imperative—empoweringhumanity to protect, restore, and coexist with nature more effectively than ever before.
 Corresponding author: Onyebuchi Nneamaka Chisom Copyright © 2024 Author(s) retain the copyright of this article.
This article is published under the terms of the Creative Commons Attribution Liscense 4.0. Reviewing the role of AI in environmental monitoring and conservation: A datadriven revolution for our planet Onyebuchi Nneamaka Chisom 1, *, Preye Winston Biu 2, Aniekan Akpan Umoh 3, Bartholomew Obehioye Obaedo 4, Abimbola Oluwatoyin Adegbite 5 and Ayodeji Abatan 6 1 National Examinations Council (NECO), Nigeria.
2 Independent National Electoral Commission (INEC) Nigeria.
3 Independent Researcher, Uyo Nigeria.
4 Department of Building, Ambrose Alli University, Ekpoma.
5 IHS Towers Nigeria Plc, Nigeria.
6 Saltwire Network, Halifax, Canada.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 Publication history: Received on 23 November 2023; revised on 30 December 2023; accepted on 01 January 2024 Article DOI: https://doi.org/10.30574/wjarr.2024.21.1.2720 Abstract The rapid increase in human activities is causing significant damage to our planet's ecosystems, necessitating innovative solutions to preserve biodiversity and counteract ecological threats.
Artificial Intelligence (AI) has emerged as a transformative force, providing unparalleled capabilities for environmental monitoring and conservation.
This research paper explores the applications of AI in ecosystem management, including wildlife tracking, habitat assessment, biodiversity analysis, and natural disaster prediction.
AI's role in environmental monitoring and conservation includes wildlife tracking, habitat assessment, resource conservation, biodiversity analysis, and species identification.
AI algorithms analyze camera trap footage, drone imagery, and GPS data to identify and estimate population sizes, leading to improved anti-poaching efforts and enhanced protection of diverse species.
Habitat assessment and resource conservation involve AI-powered image analysis, which aids in assessing forest health, detecting deforestation, and identifying areas in need of restoration.
Biodiversity analysis and species identification are achieved through AI algorithms that analyze acoustic recordings, environmental DNA (eDNA), and camera trap footage.
These innovations identify different species, assess biodiversity levels, and even discover new or endangered species.
AI-powered flood prediction systems provide early warnings, empowering communities with better preparedness and evacuation efforts.
Challenges, such as data quality and availability, algorithmic bias, and infrastructure limitations, are acknowledged as opportunities for growth and improvement.
In policy and regulation, the paper advocates for clear frameworks prioritizing data privacy and security, algorithmic transparency, and equitable access.
Responsible development and ethical use of AI are emphasized as foundational pillars, ensuring that the integration of AI into environmental conservation aligns with principles of fairness, transparency, and societal benefit.
Keywords: Artificial intelligence; Environmental monitoring; Conservation; Wildlife tracking; Habitat assessment; Biodiversity analysis; Natural disaster prediction; Case studies; Best practices; Challenges; Future directions.
Introduction In the 21st century, our planet stands at a critical juncture, grappling with an array of environmental challenges that threaten the delicate balance of ecosystems worldwide.
From the ominous specter of climate change to the insidious encroachment of habitat loss, the traditional tools of environmental monitoring and conservation find themselves strained and inadequate in the face of these formidable threats (Nelson, 2023; Lazard and Youngs, 2021).
In response  World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 162 to this pressing need, a technological savior emerges – Artificial Intelligence (AI).
This introduction endeavors to elucidate the profound implications of harnessing AI as a revolutionary toolset capable of not merely overcoming the limitations of traditional methods but transforming vast environmental datasets into actionable insights (Dwived et al., 2021).
The essence lies in empowering informed decision-making to protect and preserve our planet's biodiversity and ecological equilibrium.
As the human footprint on the Earth deepens, the symphony of environmental challenges crescendos.
Climate change, driven by anthropogenic activities, manifests through rising temperatures, erratic weather patterns, and the specter of sea-level rise.
Habitat loss, the silent but potent force, erodes the sanctuaries for countless species, pushing them to the brink of extinction (Goniewicz et al., 2023).
Pollution, in its myriad forms, poisons the air, soil, and water, leaving a toxic legacy for future generations.
Resource depletion exacerbates the strain on ecosystems, threatening the very foundations of biodiversity.
In the face of these challenges, the inadequacies of traditional monitoring methods become starkly evident.
Traditional methods of environmental monitoring, while valiant in their attempts, are often constrained by their scope, scale, and ability to process vast amounts of data.
Manual surveys and observational techniques struggle to keep pace with the rapid changes occurring in ecosystems.
Moreover, the sheer complexity of interconnected environmental systems eludes comprehensive understanding through conventional means.
In this context, the need for a paradigm shift in monitoring and conservation becomes imperative.
Artificial Intelligence emerges as a beacon of hope amid the environmental tumult.
With its capacity for advanced data processing, pattern recognition, and predictive analytics, AI holds the promise of revolutionizing the field of environmental monitoring and conservation.
It transforms the way we perceive, interpret, and act upon environmental data, providing a dynamic and responsive framework for addressing the challenges of the Anthropocene.
At the heart of AI's transformative potential lies its ability to convert vast and complex environmental datasets into actionable insights.
Through sophisticated algorithms and machine learning models, AI discerns patterns, trends, and anomalies that elude conventional methods (Fakiha, 2023, Al-Mansoori, and Salem, 2023, Adebukola et al., 2022).
This newfound capability empowers decision-makers with a depth of understanding previously unattainable, enabling them to formulate strategies that are not only effective but also adaptive to the evolving dynamics of the environment.
By scrutinizing its applications across various facets of ecosystem management, from wildlife tracking to habitat assessment, biodiversity analysis, and natural disaster prediction, this paper seeks to unravel the ways in which AI can be harnessed to confront and mitigate environmental challenges.
Through a nuanced exploration of case studies and best practices, the paper aims to not only highlight the tangible impact of AI but also to serve as a guide for the responsible and effective integration of AI into environmental conservation strategies (Kar, Choudhary, and Singh, 2022, Silvestro et al., 2022).
Each application, be it wildlife tracking, habitat assessment, biodiversity analysis, or natural disaster prediction, is scrutinized through the lens of real-world examples and best practices.
Case studies, such as the Microsoft AI for Earth program and the use of conservation drones, serve as illuminating exemplars of AI's transformative potential (Sun et al., 2022).
The subsequent section addresses challenges and envisions future directions, contemplating the integration of AI with cutting-edge technologies to create a holistic and interconnected system for environmental protection.
A dedicated section on policy and regulation emphasizes the need for a robust framework to ensure the responsible and ethical use of AI in environmental applications.
The paper culminates in a conclusion that synthesizes key insights, reiterates the transformative potential of AI, and underscores the imperative for responsible development and equitable access.
In essence, this introduction lays the foundation for a profound exploration into the confluence of AI and environmental conservation.
As we stand at the precipice of environmental uncertainty, AI emerges as a powerful ally, promising not just incremental advancements but a paradigm shift in our approach to safeguarding the planet's rich biodiversity and ecological harmony (Al-Mansoori, and Hamdan, 2023).
AI Applications in Environmental Monitoring and Conservation In the intricate dance of Earth's ecosystems, where every move and rhythm contributes to the harmonious balance of nature, the role of Artificial Intelligence (AI) emerges as a transformative force.
The clarity of elucidation is complemented by concrete examples that vividly demonstrate the tangible impact of AI in safeguarding ecosystems.
From tracking elephant poaching routes in Africa to identifying illegal logging activities in the Amazon rainforest, AI emerges as a guardian of biodiversity and a catalyst for sustainable environmental practices (Brickson et al., 2023, Dorfling et al., 2023).
Wildlife tracking is a crucial endeavor in understanding the intricate patterns that define the lives of diverse species.
Traditional methods, such as manual tracking and limited observational data, often fall short in capturing these richness (Hauenstein et al.
2022, Granli, and Poole, 2022).
However, the advent of Artificial Intelligence (AI) has revolutionized wildlife tracking by injecting unprecedented capabilities into monitoring and comprehending animal movements.
AI  World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 163 algorithms, fueled by machine learning, synthesize a rich amalgamation of data sources, including camera trap footage, drone imagery, and GPS data (Baldwin et al., 2023, Larsen et al., 2023).
Figure 1 Flowchart explaining methodolgy of anti-poaching system (Kuruppu, 2023) Figure 1 shows the implementation of camera and other alert ranger in fight against animal poaching.
This synergy of cutting-edge technologies facilitates a holistic and dynamic tracking of wildlife movement.
The depth of insight derived from AI-driven analysis surpasses traditional tracking methods, enabling conservationists to delve into the secret lives of animals with unparalleled precision.
The machine learning algorithms employed in wildlife tracking are trained on vast datasets, learning the distinctive features and behavioral patterns of various species.
This training equips them to process and interpret real-time data, allowing for a nuanced understanding of animal movements on a scale and level previously unattainable.
The result is a comprehensive, data-driven narrative of wildlife behavior, providing conservationists with a valuable tool to inform and shape conservation strategies.
One example of the tangible impact of AI in wildlife tracking is tracking elephant poaching routes in Africa.
The complexity of their migratory patterns and vast territories make traditional monitoring methods challenging.
However, AI emerges as a beacon of hope in the fight against elephant poaching.
By harnessing the analytical power of AI algorithms, conservationists can trace historical and current paths taken by these magnificent creatures and predict potential poaching hotspots with remarkable accuracy.
AI algorithms analyze a mosaic of data inputs, including historical movement patterns, habitat preferences, and external factors such as human activity and environmental changes.
Through iterative learning, these algorithms become adept at identifying subtle indicators that precede poaching incidents.
This foresight enables rapid response interventions, allowing conservation teams to deploy resources strategically and prevent poaching activities before they escalate.
2.1. Habitat Assessment and Resource Conservation Habitats, such as the towering canopies of lush forests and the intricate web of sprawling wetlands, represent the beating hearts of biodiversity.
The health of these ecosystems is paramount to the well-being of countless species and the delicate balance of nature.
Assessing the vitality of habitats and identifying areas in need of restoration demands a level of insight that transcends human capacity alone.
Artificial Intelligence (AI) offers an aerial lens that unravels the secrets of Earth's diverse ecosystems through its unparalleled image analysis capabilities, often propelled by sophisticated convolutional neural networks (CNNs) (Flück et al., 2022, Perry et al., 2022).
AI's ability to process enormous datasets swiftly and accurately is a game-changer in habitat assessment, transcending the limitations of manual surveys and traditional monitoring methods.
It offers a comprehensive view of ecosystems on regional and even global scales, providing a dynamic and real-time understanding of habitat health.
The impact of AI on habitat assessment is more vividly showcased in the heart of the Amazon rainforest, where the battle against illegal logging is fiercely waged.
Through the discerning eye of AI, satellite imagery becomes a treasure trove of information.
AI algorithms analyze this data with precision that goes beyond human capability, identifying subtle signs of illegal logging activities.
Changes in land cover, the appearance of unauthorized roads, and alterations in vegetation patterns become discernible patterns to AI, serving as telltale signs of ecological disruption.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 164 The intelligence provided by AI becomes a catalyst for targeted interventions, allowing conservationists and authorities to prioritize high-risk areas, deploy resources strategically, and enforce regulations with unprecedented effectiveness.
This proactive approach safeguards the delicate balance of the rainforest and sets a global precedent for leveraging technology to address environmental challenges.
2.2. Biodiversity Assessment and Species Identification Biodiversity is a complex interplay of species that contribute to the resilience and vibrancy of ecosystems.
Artificial Intelligence (AI) has emerged as a transformative force in biodiversity analysis, providing the means to identify and classify species while monitoring ecosystem dynamics in ways that were once inconceivable.
AI algorithms, trained on diverse datasets, orchestrate a harmonious integration of acoustic recordings, environmental DNA (eDNA), and camera trap footage (Galić et al., 2023, Habchi et al., 2023).
This multifaceted approach allows AI to unravel the rich tapestry of life, extending its reach from the depths of rivers to the canopies of rainforests.
Acoustic recordings allow AI algorithms to identify and classify species with remarkable accuracy, particularly in environments where visual observations may be challenging.
This capability is particularly valuable in dense forests or underwater ecosystems.
The symphony of nature becomes a readable score, allowing researchers to discern the presence, abundance, and even behaviors of diverse species.
Environmental DNA (eDNA), genetic material shed by organisms into their environment, represents a groundbreaking frontier in biodiversity analysis.
AI employs advanced algorithms to analyze eDNA samples, offering insights into population dynamics, genetic diversity, and interactions between different organisms.
AI-powered eDNA analysis unveils the hidden movements and relationships within ecosystems, from the smallest microbes to elusive aquatic species (Sabolić et al., 2023).
Camera traps capture images and videos of wildlife in their natural habitats, providing valuable visual data for analysis.
AI algorithms, trained on vast datasets of camera trap footage, can recognize and distinguish between various species, enabling efficient and accurate monitoring of wildlife populations, including the identification of rare or endangered species.
AI-powered eDNA analysis in rivers and oceans transcends the boundaries of traditional monitoring methods, offering a non-intrusive and comprehensive approach to studying aquatic ecosystems.
The real-time insights provided by AI-powered eDNA analysis empower conservationists and researchers to respond swiftly to emerging threats, facilitating targeted conservation interventions.
2.3. Natural Disaster Prediction and Early Warning Systems Artificial Intelligence (AI) has emerged as the oracle in natural disaster prediction, transforming our ability to anticipate and respond to environmental threats (Guha, Jana, and Sanyal, 2022).
By analyzing historical data and real-time environmental measurements, AI models and early warning systems provide unprecedented accuracy in predicting natural disasters.
These models, empowered by machine learning algorithms, lay the foundation for robust early warning systems that enable proactive responses to impending disasters.
AI's predictive prowess is dynamic, evolving through continuous learning from historical data and real-time inputs.
This adaptability ensures that predictions remain accurate even as environmental conditions change.
The orchestration of these AI models within early warning systems creates a comprehensive and timely prediction of impending natural disasters.
A shining example of AI's role as an oracle in natural disaster prediction unfolds in the implementation of flood prediction systems in coastal regions.
Coastal areas, prone to the devastating impact of floods, demand sophisticated solutions to mitigate risks and protect both human and ecological communities.
AI, with its analytical acumen, steps into this arena, revolutionizing the way we anticipate and respond to the looming threat of flooding.
The journey into flood prediction begins with a thorough analysis of historical data, examining past occurrences, the behavior of water bodies, and the dynamics of weather patterns.
This retrospective view provides valuable insights into the factors contributing to flooding events, laying the groundwork for predictive modeling.
AI's predictive capabilities extend beyond historical data, incorporating real-time weather conditions into its models.
By continuously monitoring meteorological variables such as rainfall, wind patterns, and atmospheric pressure, AI adapts its predictions in response to unfolding environmental dynamics, enhancing the accuracy of flood predictions.
AI's prowess in flood prediction is further amplified by its ability to consider topographical features (Hamitouche, and Molina, 2022, Uddin et al., 2022).
By analyzing the geography of coastal regions, including elevation, terrain, and water flow patterns, AI refines its predictions to account for the specific vulnerabilities of each area, offering a more nuanced and accurate forecast (Liu et al., 2022).
Challenges and Future Directions in AI-Powered Environmental Conservation As we embark on a journey into the realm of AI-powered environmental conservation, it becomes imperative to navigate the challenges that lie ahead while charting a visionary course for the future.
This section delves into the obstacles currently faced by AI applications in this domain and explores the exciting possibilities that emerge on the horizon.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 165 3.1. Data Quality and Availability At the core of AI's effectiveness in environmental monitoring and conservation is the quality and availability of data.
The success of AI applications relies on the capacity to access comprehensive and accurate environmental data.
However, this fundamental requirement poses a significant challenge in many regions worldwide.
The variability in data quality hampers the development and deployment of robust AI models, limiting their ability to provide accurate insights and predictions.
To tackle the challenge of inconsistent data quality, concerted efforts are needed to enhance data collection infrastructure.
This involves a strategic investment in advanced technologies such as sensor networks, satellite technology, and ground-based monitoring systems to gather real-time and high-resolution data.
Collaboration between governments, research institutions, and technology companies is crucial in establishing standardized data collection protocols (Whang et al., 2023).
This collaborative approach ensures the development of a robust foundation of quality data for AI applications.
An innovative and inclusive approach to overcoming data challenges is the integration of citizen science.
By actively involving the public in data collection through user-friendly apps and community-driven initiatives, a vast network of observers can contribute valuable information.
This participatory model not only enhances the quantity of available data but also promotes public engagement and awareness.
Harnessing citizen science fosters a sense of shared responsibility for environmental conservation, creating a more inclusive and sustainable approach to data collection.
3.2. Algorithmic Bias and Explainability As AI becomes deeply integrated into environmental monitoring, the ethical dimension gains prominence.
Algorithmic bias within AI models can perpetuate and exacerbate existing disparities in conservation efforts.
Addressing these biases is crucial to ensure fair and equitable outcomes and prevent unintended harm to certain species, ecosystems, or communities.
The ethical development and deployment of AI in environmental conservation demand a proactive commitment to identify and rectify biases in algorithms.
Building trust in AI systems necessitates prioritizing transparency and explainability.
Stakeholders, including conservationists, policymakers, and the public, need to comprehend how AI algorithms make decisions.
This transparency not only fosters accountability but also enables the identification and correction of biases.
Explaining the decision-making processes of AI models becomes a fundamental step in ensuring responsible and ethical use in environmental conservation.
Through clear communication and transparency, AI applications can garner support and collaboration from diverse stakeholders.
3.3. Infrastructure and Computational Resources Implementing AI solutions in environmental conservation often comes with a substantial cost associated with infrastructure, computational resources, and connectivity (Dauvergne, 2022).
This poses a considerable challenge, especially for smaller organizations or those operating in remote regions with limited access to technology.
The high costs related to hardware, software, and internet connectivity can act as barriers to entry for many conservation initiatives (Singh et al., 2022).
Addressing infrastructure challenges involves exploring ways to scale down technology without compromising its effectiveness.
Strategies such as leveraging cloud computing, edge computing, and developing low-cost, energy-efficient AI hardware become crucial in making AI more accessible.
Additionally, partnerships between technology companies and conservation organizations can facilitate access to computational resources, enabling a broader range of projects to harness the power of AI.
A sustainable approach to overcoming infrastructure challenges involves building local capacity.
This includes providing training and resources to conservation practitioners in the use of AI tools.
Empowering local communities to take ownership of monitoring initiatives not only addresses infrastructure limitations but also fosters a sense of stewardship for the environment (Danielsen et al., 2022, Chidolue and Iqbal, 2023).
Training programs tailored to local contexts and needs contribute to the long-term sustainability of AI applications in environmental conservation.
3.4. Integration with Other Technologies The future of AI in environmental conservation hinges on its seamless integration with other advanced technologies.
Synergies between AI, robotics, and the Internet of Things (IoT) hold immense potential for revolutionizing monitoring strategies and enhancing conservation outcomes (Bibri et al., 2024).
The combined power of these technologies can create a more holistic and effective approach to environmental protection.
Envisioning AI-powered robotic drones patrolling forests and protected areas introduces a new dimension to conservation efforts.
These drones, equipped with advanced sensors and AI algorithms, can autonomously collect data on wildlife populations, monitor illegal activities, and assess habitat health.
The real-time information they provide becomes a valuable resource for AI models, enabling continuous monitoring and predictive analysis.
The integration of AI-powered robotic drones amplifies the scope and efficiency of environmental monitoring.
The deployment of sensor networks embedded within ecosystems represents a paradigm shift in environmental monitoring.
These networks, comprising various environmental sensors, can transmit real-time data on air and water quality, soil health, and animal movement.
The integration of sensor data  World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 166 directly into AI models allows for continuous monitoring, facilitating timely interventions and adaptive conservation strategies.
The synergy between AI and sensor networks provides a comprehensive and dynamic understanding of ecosystems, enabling more effective conservation strategies.
In the envisioned future of conservation, AI-powered virtual assistants play a pivotal role.
These assistants, driven by sophisticated AI algorithms, analyze vast datasets to recommend optimal resource allocation, predict poaching hotspots, and guide on-the-ground conservation efforts.
The collaboration between AI-driven insights and human decision-making creates a powerful partnership, enhancing the efficiency and effectiveness of conservation strategies.
AI-powered virtual assistants serve as intelligent tools for decision support, contributing to more informed and adaptive conservation practices.
3.5. Ethical Considerations and Responsible Data Use As AI becomes more deeply integrated into environmental monitoring, upholding ethical standards becomes paramount.
Ensuring that data collection practices respect privacy concerns, adhere to ethical standards, and avoid harmful biases is crucial for the ethical deployment of AI in conservation (Rabbani et al., 2022).
The development and implementation of clear ethical guidelines serve as a foundation for responsible AI use in environmental conservation (Wang et al., 2023).
Conservation practitioners must be equipped with the knowledge and skills to make informed decisions about AI tools.
This involves comprehensive training programs that emphasize ethical considerations, responsible data use, and the potential impact of AI on ecosystems and communities.
By prioritizing ethical education, the conservation community can navigate the ethical complexities associated with AI implementation.
Informed decision-making ensures that AI is utilized responsibly and ethically to achieve conservation goals.
3.6. Training and Capacity Building The successful integration of AI into environmental conservation requires the empowerment of conservation practitioners.
Training programs should be thoughtfully designed to equip them with the necessary skills and knowledge to effectively utilize AI tools.
This includes understanding the capabilities and limitations of AI, interpreting model outputs, and integrating AI into existing conservation workflows.
Empowered conservation practitioners serve as catalysts for the effective implementation of AI in diverse conservation projects.
Collaboration between AI experts, conservation organizations, and government agencies is essential for skill transfer and capacity building (Madan, and Ashok, 2023, Ikwuagwu et al., 2020).
By fostering partnerships, knowledge can be shared, and joint development of AI solutions can occur.
This collaborative approach ensures that the benefits of AI are accessible to a wide range of conservation projects, regardless of their size or geographical location.
Skill transfer and capacity building contribute to the democratization of AI in environmental conservation, creating a more inclusive and impactful conservation community.
3.7. Vision for the Future 3.7.1. A Holistic and Interconnected System As we navigate through the environmental challenges of our time, a compelling vision for the future emerges—a vision of a holistic and interconnected system for environmental protection.
In this future, the integration of artificial intelligence (AI) with other advanced technologies creates a dynamic and responsive network that adapts to the evolving needs of conservation.
This interconnected system envisions a seamless collaboration between AI, robotics, sensor networks, and virtual assistants to form a comprehensive approach to environmental monitoring and conservation.
In the envisioned future, AI-powered robotic drones take center stage in patrolling and monitoring ecosystems.
These drones, equipped with advanced sensors and AI algorithms, autonomously collect data on wildlife populations, assess habitat health, and detect illegal activities.
The real-time information they provide becomes a critical input for AI models, enabling a continuous feedback loop for monitoring and analysis.
The integration of AI with robotic drones revolutionizes the way we conduct wildlife tracking and habitat assessment.
These AI-enhanced drones can navigate challenging terrains, reach remote locations, and gather data with unparalleled precision.
For example, in dense forests or vast expanses of protected areas, AI-powered drones can identify and monitor wildlife populations, providing crucial insights into migration patterns and assessing the overall health of ecosystems.
The predictive capabilities of AI further enhance the effectiveness of these drones (Kolluri et al., 2022, Ukoba and Jen, 2022).
By analyzing historical data and current environmental conditions, AI algorithms can predict potential threats, such as poaching activities or habitat degradation, allowing for proactive conservation measures (Shivaprakash et al., 2022, Isabelle, and Westerlund, 2022).
This collaborative effort between AI and robotic drones not only improves the efficiency of monitoring but also contributes to the protection of endangered species and the preservation of biodiversity.
Figure 2 compares two tools used for tracking animal motion using their architecture.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 167 Figure 2 General architecture of Animal Motion Tracking using YOLOv4 and Deep SORT (Borah, Saikia, and Das, 2022) 3.7.2. Sensor Networks for Continuous Monitoring The future of environmental monitoring is transformed by the deployment of sensor networks seamlessly integrated with AI.
This evolution turns monitoring into a continuous and adaptive process, offering real-time insights into the state of ecosystems.
Distributed across diverse ecosystems, these sensor networks transmit data on various parameters, including air and water quality, soil health, and animal behavior.
AI models process the continuous stream of data from these sensor networks, providing a comprehensive understanding of environmental changes.
For instance, sensors embedded in rivers can monitor water quality and detect changes in fish behavior, while soil sensors can assess the health of vegetation.
The integration of sensor data directly into AI models allows for timely interventions and adaptive conservation strategies.
This interconnected system, combining AI and sensor networks, creates a powerful tool for addressing environmental challenges.
Whether it's responding to pollution incidents, tracking the spread of invasive species, or predicting the impact of climate change, the continuous monitoring facilitated by these networks enables a proactive and informed approach to conservation.
3.7.3. AI-Powered Virtual Assistants AI-powered virtual assistants emerge as indispensable allies in shaping the future of conservation.
These assistants, driven by sophisticated AI algorithms, analyze vast datasets to recommend optimal resource allocation, predict emerging threats, and guide on-the-ground conservation efforts.
The collaboration between AI-driven insights and human decision-making enhances the efficiency and effectiveness of conservation strategies, ensuring a more informed and adaptive approach.
In this future scenario, AI-powered virtual assistants support conservation practitioners by providing real-time analysis and actionable recommendations.
For example, these virtual assistants can process data on wildlife populations, habitat conditions, and potential threats, offering insights that inform decision-making.
By harnessing the analytical power of AI, conservationists can prioritize conservation efforts, allocate resources efficiently, and respond swiftly to emerging challenges.
The synergy between human expertise and AI-driven insights results in a more dynamic and responsive conservation approach.
Virtual assistants contribute to the democratization of AI in conservation by providing accessible tools for a wide range of projects.
As these virtual assistants become integral to conservation workflows, they empower practitioners with the capabilities to address complex environmental issues effectively.
3.7.4. Ethical Considerations and Responsible Development The future of AI in environmental conservation is firmly grounded in ethical considerations and responsible development.
Clear policy frameworks and regulations are established to ensure the responsible and equitable use of AI in conservation efforts.
Data governance policies prioritize privacy and security, while measures are in place to ensure algorithmic transparency and accountability.
In this envisioned future, ethical standards guide the development and deployment of AI technologies.
The responsible use of AI in environmental monitoring involves transparent decision-making processes, addressing potential biases, and mitigating unintended consequences.
The establishment of ethical guidelines fosters trust among stakeholders, including conservationists, policymakers, and the public, ensuring that AI is a force for good in the realm of environmental conservation.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 168 3.7.5. Equitable Access and Capacity Building The tapestry of the future is woven with threads of equitable access and capacity building.
Platforms like EarthRanger and Wildbook, serving as models for inclusive collaboration, continue to democratize access to cutting-edge AI technology.
Training programs empower conservation practitioners globally, ensuring that the benefits of AI are harnessed by projects of varying scales and in diverse geographical locations.
In this future vision, equitable access to AI tools is a cornerstone of conservation efforts.
Platforms that provide AI resources, such as EarthRanger and Wildbook, contribute to the accessibility of advanced technologies.
These platforms serve as hubs for collaboration, allowing conservation organizations, researchers, and practitioners to access cutting-edge AI tools and share knowledge.
Training and capacity building play a pivotal role in ensuring that the potential of AI is realized across diverse conservation projects.
By providing education and resources, training programs empower conservation practitioners to integrate AI into their work effectively.
Collaboration between AI experts, conservation organizations, and government agencies becomes a catalyst for skill transfer, fostering a global community committed to leveraging AI for environmental protection.
Policy and Regulation The integration of artificial intelligence (AI) into environmental conservation presents both transformative possibilities and ethical challenges.
To ensure the responsible and equitable use of AI in environmental applications, a robust framework of policies and regulations is essential.
Key areas of focus within policy and regulation include data privacy, algorithmic transparency, and equitable use.
Data privacy and security are crucial for the responsible and ethical use of AI in environmental monitoring and conservation.
Policies must outline stringent guidelines for data collection, storage, and usage, adopting encryption protocols, secure storage systems, and access controls to prevent unauthorized use.
Clear consent mechanisms should be established for data collection from public and private sources, with an emphasis on transparency regarding the purposes and potential impacts of data usage.
Collaborative data governance is essential for establishing standardized data collection protocols, fostering a sense of shared responsibility for ethical data practices.
Engaging local communities in decision-making processes helps build trust and ensures that the benefits of AI-driven conservation efforts are equitably distributed.
Algorithmic transparency and accountability are essential for ensuring fair and equitable outcomes in AI algorithms.
Transparency in decisionmaking processes is fundamental for building trust in AI systems.
Developers, policymakers, and the public should have a clear understanding of how AI algorithms operate and make decisions.
Accountability measures for developers should be included in policies to uphold ethical standards.
This includes addressing biases, rectifying unintended consequences, and continuously improving algorithmic models.
Establishing frameworks for external audits and assessments can further ensure that AI applications adhere to ethical standards and contribute positively to environmental conservation.
Accessibility and equitable use are also essential for ensuring equitable access to AI tools for conservation efforts, particularly in resource-limited regions.
Policies should support the development and deployment of affordable and accessible solutions, incentivizing technology companies to provide cost-effective AI applications and fostering collaborations that promote the sharing of AI resources.
Disparities in technology access should be addressed by policies that promote inclusive collaboration and democratize access to cutting-edge technology.
Global collaboration is vital to ensuring that the benefits of AI in environmental conservation are equitably distributed.
Policies should encourage partnerships between AI experts, conservation organizations, and government agencies on a global scale, facilitating knowledge exchange, skill transfer, and the development of AI solutions that are adaptable to diverse conservation projects worldwide.
Ethical considerations and responsible data use are also crucial for the ethical use of AI in environmental conservation.
Policies should prioritize responsible data practices, uphold ethical standards in data collection, analysis, and decision-making processes, and enable informed decision-making.
Policies should also provide guidance on navigating ethical complexities associated with AI implementation, such as consent, data ownership, and potential unintended consequences.
Future-forward policies for emerging challenges in AI and environmental conservation should anticipate and address evolving threats, support research and innovation, and encourage international cooperation and standardization.
By establishing common frameworks for data governance, algorithmic transparency, and equitable use, policies not only safeguard against potential risks but also create an environment conducive to the positive and impactful use of AI in preserving biodiversity, monitoring ecosystems, and addressing complex environmental challenges.
World Journal of Advanced Research and Reviews, 2024, 21(01), 161–171 169 5.
Conclusion This research paper explores the transformative potential of artificial intelligence (AI) in environmental monitoring and conservation, focusing on wildlife tracking, habitat assessment, biodiversity analysis, and natural disaster prediction.
The paper highlights the importance of responsible development, ethical considerations, and equitable access in harnessing AI's true potential for the planet's well-being.
The research provides a comprehensive overview of the multifaceted role of AI in environmental monitoring and conservation, blending theoretical concepts with practical examples.
Theoretical concepts and practical examples demonstrate the depth and breadth of AI's capabilities in unraveling the intricate patterns of the natural world.
Practical examples, such as tracking elephant poaching routes in Africa and identifying illegal logging activities in the Amazon rainforest, serve as powerful illustrations of AI's tangible impact on conservation efforts.
Challenges, and future directions enhance the credibility and depth of the research.
Case studies, such as Microsoft AI for Earth and Conservation Drones, demonstrate real-world applications of AI in diverse conservation projects, from monitoring coral reef health to protecting endangered rhinos.
Best practices include collaboration and data sharing, focusing on specific conservation goals, ethical considerations, and training and capacity building.
Addressing challenges such as data quality and availability, algorithmic bias, infrastructure limitations, and the need for integration with other advanced technologies reflects a nuanced understanding of the complexities involved in the intersection of AI and environmental conservation.
The paper calls for the responsible integration of AI in environmental conservation efforts, emphasizing the responsibility to ensure its deployment aligns with ethical standards, respects privacy, and avoids harmful biases.
The paper acknowledges that the journey toward integrating AI into environmental conservation is not without challenges, but frames them as opportunities for growth and improvement.
Embracing future directions envisions a landscape where AI seamlessly integrates with other advanced technologies such as robotics and the Internet of Things (IoT).
The proposed synergies, including AI-powered robotic drones, sensor networks, and virtual assistants, paint a picture of a holistic and interconnected system for environmental protection.
In conclusion, this research paper serves as a testament to the potential of AI as a force for good in safeguarding the planet's ecosystems.
By providing a nuanced understanding of AI applications, highlighting best practices, addressing challenges, and outlining future directions, the paper contributes to a growing body of knowledge that can guide the responsible use of AI in environmental conservation.
Abstract Climate change is the most severe ecological challenge faced by the world today.
Forests, the dominant component of terrestrial ecosystems, play a critical role in mitigating climate change due to their powerful carbon sequestration capabilities.
Meanwhile, climate change has also become a major factor affecting the sustainable management of forest ecosystems.
Climate-Smart Forestry (CSF) is an emerging concept in sustainable forest management.
By utilizing advanced technologies, such as information technology and artificial intelligence, CSF aims to develop innovative and proactive forest management methods and decision-making systems to address the challenges of climate change.
CSF aims to enhance forest ecosystem resilience (i.e., maintain a condition where, even when the state of the ecosystem changes, the ecosystem functions do not deteriorate) through climate change adaptation, improve the mitigation capabilities of forest ecosystems to climate change, maintain high, stable, and sustainable forest productivity and ecosystem services, and ultimately achieve harmonious development between humans and nature.
This concept paper: (1) discusses the emergence and development of CSF, which integrates Ecological Forestry, Carbon Forestry, and Smart Forestry, and proposes the concept of CSF; (2) analyzes the goals of CSF in improving forest ecosystem stability, enhancing forest ecosystem carbon sequestration capacity, and advocating the application and development of new technologies in CSF, including artificial intelligence, robotics, Light Detection and Ranging, and forest digital twin; (3) presents the latest practices of CSF based on prior research on forest structure and function using new generation information technologies at Qingyuan Forest, China.
From these practices and reflections, we suggested the development direction of CSF, including the key research topics and technological advancement.
Similar content being viewed by others  Defining Climate-Smart Forestry Chapter © 2022  Remote Sensing Technologies for Assessing Climate-Smart Criteria in Mountain Forests Chapter © 2022  Identifying Future Research and Directions to Address Forest and Climate Change Challenges Chapter © 2024 Explore related subjects Discover the latest articles, books and news in related subjects, suggested using machine learning.
Computational Intelligence Ecosystem Services Forestry Forest Ecology Forestry Management Wood Science and Technology Introduction Forests provide a range of vital ecosystem services, including serving as a carbon sink to mitigate climate change.
However, contemporary, human-caused global warming and its derived extreme climate events and other disturbances have presented unprecedented challenges to global forests, threatening their stability and resilience.
To address these challenges, we need an innovative solution to sustainable forest management (i.e., Climate-Smart Forestry, CSF) to ensure climate change adaptation while optimizing climate change mitigation for the critical period through 2100 when the magnitude of global warming must be controlled below 1.5 °C (IPCC 2018).
CSF first appeared in peer-reviewed literature in 2017, which was defined as “a more specific (climate-oriented) form of the Sustainable Forest Management paradigm” (Nabuurs et al.
Previous research on the CSF concept has primarily addressed mitigation actions, with a focus on greenhouse gas emission reduction and carbon sequestration (e.g., Nabuurs et al.
2018; Verkerk et al.
Realizing the imminent threats from climate change, many studies have also concentrated on evaluating forest adaptation capacity, identifying critical environmental stressors, and developing optimal strategies to enhance forest ecosystem resilience (e.g., Lisella et al.
2022; Sterck et al.
Over the past few years, CSF has evolved to promote both adaptation and mitigation in forest management practices (e.g., Cooper and MacFarlane 2023; Luo et al.
2023; Shephard et al.
2022; Tognetti et al.
2022; Wang 2024; Zhu et al.
Coinciding with the emergence of CSF, artificial intelligence (AI) has progressed significantly and is capable of solving real-world data problems in virtually all areas of application domains (Holzinger et al.
As a result, forestry is also undergoing a digital transformation towards a “smart” forestry (Ehrlich-Sommer et al.
This new development has recently been integrated into CSF (Wang 2024; Zhu et al.
By leveraging the latest information technologies and AI, CSF seeks to develop innovative and proactive forest management methods and decision-making systems to tackle climate change challenges and thus holds great promise in addressing some unique challenges in forestry, such as the long lifecycle of forests, difficulties in field-controlled experiments, high trial-and-error costs, and the interdisciplinary nature of climate change (Zhu et al.
In this concept paper, we first discussed the evolution of forestry and the emergence of CSF, based on which we proposed a new definition for CSF.
We then analyzed the goals of CSF in improving forest ecosystem stability, enhancing forest ecosystem carbon sequestration capacity, and advocating the application and development of new technologies in CSF, including artificial intelligence, robotics, Light Detection and Ranging (LiDAR), and forest digital twin.
Using Qingyuan Forest as an example, we described the application of CSF in forest ecosystem studies.
Finally, we suggested the development direction of CSF, including the key research topics and technological advancement.
Concept of climate-smart forestry Forestry’s primary goal has always been meeting societal demands for forest resources, yet society’s perception of and need for forests continuously evolves.
Forestry development has undergone three major paradigm shifts: traditional forestry before the 1970s, ecological forestry from the 1980s to 2020, and the emergence of CSF in the post-2020 era (Zhu et al.
Traditional forestry was rooted in pragmatism and focused mainly on timber production, management, and utilization.
Following the unsustainable exploitation and utilization of forests, ecological forestry emerged.
Influenced by the modern environmental movement and the rapid advancement of ecology since the 1970s, this approach highlighted the ecological roles forests play as part of the Earth’s life-support systems.
Concepts such as close-to-nature silviculture, continuous cover forestry, and ecosystem management were introduced to ensure the health and integrity of forest ecosystems and sustainably supply societal needs for products and services.
CSF has recently emerged to address the challenges of climate change driven by human-caused greenhouse gas emissions.
Initially conceptualized in the European Union (Bowditch et al.
2020; Weatherall et al.
2021), CSF has rapidly progressed in the United States and elsewhere in recent years (Cooper and MacFarlane 2023; Luo et al.
2023; Shephard et al.
2022; Wang 2024; Zhu et al.
Building on the solid foundation of ecological forestry, CSF blends the latest developments in carbon forestry and smart forestry and emphasizes the application of new technologies (e.g., informatization and AI) in forestry.
Carbon forestry started by emphasizing carbon trading and by focusing on cultivating fast-growing monocultures or managing existing forests to maximize carbon storage (Mitchell et al.
It then developed into an evolved form of sustainable forest management (or climate forestry), which seeks to enhance forest resilience to climate change by adjusting and improving biochemical processes (such as photosynthesis, respiration, and decomposition) and biophysical processes (like water absorption and transpiration) to increase CO2 absorption, decrease greenhouse gas emissions, and promote sustainable forest resource use, balancing environmental, social, and economic benefits.
Thus, carbon forestry becomes a crucial part of nature-based climate solutions (NbCS), similar to the initial concept of CSF (Bowditch et al.
2020; Nabuurs et al.
Smart forestry applies advanced technologies such as the Internet of Things (IoT), artificial intelligence (AI), big data, and information technology in forestry.
By enabling real-time data collection and feedback, it creates a forest digital twin model—a virtual representation of real forest ecosystems—that simulates forest development, identifies disaster warning signals, optimizes decision precision, and enhances management efficiency for sustainable forest management (Cao et al.
2022; Zhao et al.
Smart forestry is an evolution of digital forestry, with AI and forest digital twin platforms at its core (Buonocore et al.
2022; Luo et al.
Based on recent advances in forestry research and practices, we define Climate-Smart Forestry as an emerging concept in sustainable forest management, which develops innovative forest management and decision-making systems through the latest technologies like information technology and AI to address climate change challenges, aiming to enhance the resilience of forest ecosystems, improve their capacity to mitigate climate change while maintaining forest productivity and other ecosystem services, and ultimately achieve harmonious development between humans and nature (Fig.
1 figure 1 Conceptual diagram of Climate-Smart Forestry (CSF), modified from Wang (2024)  Full size image Goals of climate-smart forestry (CSF) Overview of CSF Climate-Smart Forestry has three keywords: climate, smart, and forestry (Fig.
The “forestry” part has never changed, which still is to provide goods and services to society and the well-being of the environment.
However, our management objectives and priorities are changing, and we are now preoccupied with climate change mitigation and adaptation.
Consequently, "climate" is prominently featured in CSF.
With the inherent complexity of forest ecosystems and the uncertainty and novelty of climate change, advanced technologies must be applied to develop proactive management strategies and practices for CSF.
Therefore, CSF has to be "smart" as well.
Thus, the goals of CSF are to help forests adapt to climate change so that forests remain resilient and continue to provide ecosystem goods and services, especially neutralizing carbon emissions.
Adapting forest ecosystems to climate change to improve resilience Climate change has already begun or is in the process of weakening the resistance and recovery capabilities of forests against disturbances (Forzieri et al.
Therefore, CSF must develop a series of proactive management strategies and practices to adapt forest ecosystems to climate change and ensure their resilience.
These strategies include (1) maintaining the status quo, (2) restoring former stable states, and (3) guiding forests toward an ideal state suitable for future climates.
The choice of specific strategies and measures depends on factors such as forest type, species, structure, site conditions, management goals, and anticipated climate change scenarios.
When climate and disturbance factors remain within their historical range of variability, CSF focuses on maintaining the current state of forests or restoring them to their original stable states.
However, in the face of drastic climate changes and systemic alterations in disturbances, management strategies must focus on transitioning existing forests smoothly into an ideal future state to ensure the sustainability of ecosystem services (Fig.
Under novel climatic conditions and disturbances, forest ecosystems often struggle to maintain their current status (Millar and Stephens 2015).
Thus, it is crucial to utilize historical multi-source data and real-time survey data to develop forest digital twin models, simulate and forecast future climate and disturbance scenarios, identify suitable species compositions (local or introduced), and develop specific management plans to facilitate an ecosystem transition.
This ecosystem should have a structure and function similar to the existing forest, ensuring stable ecosystem service functions while achieving a smooth transition (Fig.
For instance, the chestnut blight in the early twentieth century led to the functional extinction of the American chestnut in its natural range.
However, forests dominated by the American chestnut transitioned naturally and smoothly to oak-dominated forests, maintaining similar forest structures and ensuring the stability of ecosystem service functions.
2 figure 2 Modified from Wang (2024)  Hypothetical responses of current forests to climate change-driven disturbances.
The stability of current forests leads to the maintenance of current forest conditions when climate change is within the historical range of variation, but the forest will transform to a new alternate stable status (transition) in response to new climate conditions or disturbance stage.
Full size image Enhancing carbon sequestration in forest ecosystems to mitigate climate change Terrestrial ecosystems absorb about 30% of carbon emissions, with over 80% of this absorption occurring in forests (Keenan and Williams 2018).
Thus, forests are crucial to nature-based climate solutions.
Among these solutions, forest-based approaches account for ~ 70% of the overall mitigation potential (Griscom et al.
To realize this potential, CSF must enhance the carbon storage capacity of forests.
Generally, three strategies can be employed to enhance carbon sequestration in forests (Verkerk et al.
2020): (1) Increase forest area: Expand afforestation area and avoid deforestation; (2) Enhance internal carbon storage: Promote forest restoration, improve forest quality, and reduce carbon emissions from disturbances, such as wildfires; (3) Develop climate-smart forest products for external carbon storage: Increase timber production, promote efficient utilization of wood products, and substitute non-wood products.
Due to historical overharvesting and other anthropogenic disturbances, many forests are recovering, displaying significant carbon sequestration potential (CSP).
Theoretically, the carbon sequestration potential of any specific forest can be determined by the difference between its carbon carrying capacity (CCC) and current carbon stock.
The CCC refers to the maximum carbon storage a forest ecosystem can achieve in dynamic equilibrium under specific environmental conditions and natural disturbance regimes (Gupta and Rao 1994).
Research exists on the CCC of forests in different regions and countries (Chen et al.
2022b; Liu et al.
2014), but further studies are needed to clarify the CCC for various forest types, especially concerning the carbon saturation threshold of forest soils (Keith et al.
In most countries, only a small portion of forests are actively managed.
It is crucial to prioritize forests with the greatest carbon sequestration potential to quickly realize their CSP with tailored carbon sequestration strategies.
For example, large-scale carbon sinks have mainly resulted from forest recovery following historical destruction in the United States.
It is estimated that between 1700 and 1935, U.S. forests released approximately 42,000 Tg C due to logging and land-use changes (e.g., agriculture, pasture, and development).
Still, they absorbed around 15,000 Tg C during recovery from 1935 to 2010 (Birdsey et al.
As forests approach their CCC, it remains unclear whether current carbon sequestration rates can remain stable and for how long.
Recent studies indicate that the future carbon sequestration potential of existing forests is limited (Roebroek et al.
Under climate change, forests may face more frequent or extreme disturbances, threatening to reverse carbon storage.
For instance, in 2023, extreme wildfires in Canada released over 1.5 billion tons of CO2 into the atmosphere, exceeding Canada’s total CO2 emissions from wildfires over the past 22 years (1.374 billion t) (Chinese Academy of Sciences 2023).
The carbon storage of any forest ecosystem will ultimately reach saturation, equivalent to its CCC, if not disturbed prematurely.
At this point, natural disturbances can lead to carbon losses, and forests gradually recover post-disturbance, maintaining a dynamic balance in carbon sequestration.
However, through judicious harvesting and timber utilization, we can manage forests as a constant carbon sink by maintaining their carbon stock well below CCC, which opens new opportunities for actively managed forests such as plantations.
To maximize this potential, we can take the following measures (Köhl and Martes 2023): (1) Develop CSF technologies: Employ silviculture methods that minimize carbon emissions to increase the yield of timber and other products; (2) Enhance development and utilization of wood and biomass products: Achieve long-term carbon storage; (3) Substitute wood for high-emission materials: Use wood to replace steel, concrete, and plastics, maintaining carbon storage capacity in wood while reducing greenhouse gas emissions from the production of substituted materials.
(2011) discussed achieving external carbon sequestration by increasing timber production, promoting timber product use, and substituting non-wood products.
They compared a 45-year-old rotation-aged plantation (carbon stock = 189 t ha−1) with a mature stand at CCC (carbon stock = 420 t ha−1).
Over the next 135 years (three rotation periods), the annually fixed carbon per unit area was found to be 4.2 to 9.7 t ha−1 a−1 higher in sustainably managed plantations (Fig.
3 figure 3 Modified from Wang (2024)  The impact of management and wood-use alternatives on total carbon mitigation.
Assuming the old-growth forest has a carbon carrying capacity (CCC) of 420 t ha−1 and the sustainably managed plantation has a carbon stock of 189 t ha−1 at the rotation age of 45.
The three scenarios are 1) conserving the old-growth forest, 2) sustainably managing the plantation with average substitution, and 3) sustainably managing the plantation with high substitution.
At 180 years after three harvests, in-situ C stock is 420, 189, and 189 t ha−1, ex-situ C stock is 0, 570, and 1314 t ha−1, and C sequestration rate is 0, 4.2, and 9.7 t ha−1 a−1.
This figure was produced with the data provided by Lippke et al.
Full size image Developing and applying cutting-edge technologies to make better decisions under climate change uncertainty To effectively address climate change and advance CSF, the application of emerging technologies is crucial (Zhu et al.
Artificial intelligence (AI) plays an important role in the complex process of forestry decision-making.
Compared to traditional modeling approaches, AI can effectively overcome challenges such as data limitations, incomplete knowledge, and uncertainties surrounding future climate changes, thus enhancing the accuracy of predictions regarding the future state of forests and optimizing management decisions.
Furthermore, CSF can also implement evidence-based practice (EBP), which is widely used in the medical field, by integrating the best research evidence, local management experiences, and human values and needs into real-world decision-making.
High-quality data is foundational for making informed forest management decisions.
Therefore, CSF must develop and utilize cutting-edge technologies to enhance data collection methods.
For example, utilizing AI and robotics, we can develop Forest Intelligent Data Acquisition System (FIDAS) to enable real-time data acquisition using LiDAR technology.
Drones equipped with various specialized cameras and sensors can collect data both above and below the forest canopy, providing real-time, precise, and efficient information that significantly compensates for the limitations of ground survey data (e.g., forest inventory data) and the resolution constraints of satellite data.
The application and development of FIDAS will fundamentally transform forest data collection methods and promote advancements in forest science and management.
To make more accurate predictions under uncertain climate conditions, CSF will actively explore the application of Forest Digital Twins.
A Forest Digital Twin consists of a set of virtual models that can simulate the structure, composition, and dynamics of a forest in real-time, built at various spatial scales (from stand scale to global scale).
By utilizing different climate scenarios and time resolutions, the Forest Digital Twin provides more accurate predictions of future forest states.
When combined with three-dimensional virtual reality, this platform can assist researchers and managers in visually forecasting future forest changes and identifying critical factors essential for formulating CSF policies, strategies, and practices.
Case study of CSF: forest structure and function using next-generation information technology Case area Qingyuan Forest CERN, a National Observation and Research Station, has established a comprehensive observation platform within a typical independent watershed spanning 536 ha.
This platform includes multiple 50-m-tall observation towers (Qingyuan Ker Towers), permanent sample plots, and a network of hydrological stations.
It primarily utilizes a flux tower system for carbon and water flux observations, along with multi-platform LiDAR as the main method for monitoring forest structure (Zhu et al.
Based on this framework, advanced information technologies such as the IoT, AI, and big data have been integrated into the study of forest ecosystem structure and function.
A three-dimensional, holographic forest ecosystem observation research methodology system centered around the Qingyuan Ker Towers, has been designed to achieve multi-scale, multi-factor, and full-process data acquisition, storage, computation, analysis, simulation, visualization, and scientific application in forest structure and function, thereby fostering knowledge innovation in forestry and ecology and providing pathways for exploring paradigm shifts in research and management (Gao et al.
2023; Zhu et al.
4 figure 4 Configuration of the Qingyuan Forest CERN  Full size image Data collection The development and application of a Forest Intelligent Data Acquisition System is crucial for realizing CSF.
The Qingyuan Forest CERN has established a three-dimensional structure collection informatization system centered on LiDAR, using near-surface remote sensing (ground-, tower-, and drone-based) as the main platforms.
This system enables dynamic monitoring across multiple scales and factors, including forest phenology, canopy structure (such as leaf area index), and greenness (Li et al.
The point cloud data and high-resolution visible/multispectral images have been collected (Chen et al.
2022a) and fine structural information on canopy has been obtained (Lu et al.
2020), facilitating the automated collection of key structural elements to support analyses of the relationships between forest structure and function and their responses to climate change (Gao et al.
IoT-based data transmission Real-time and efficient data transmission is a vital component of the Forest Intelligent Data Acquisition System.
The Qingyuan Forest CERN has achieved network coverage for observation plot arrays and constructed an IoT platform supporting comprehensive data access, intelligent gateways, and cloud-edge collaboration.
This platform allows for the connection of numerous sensors (Fig.
4), facilitating the uploading of collected data while providing remote control instructions from the server to the sensors.
Ultimately, this system aggregates heterogeneous and abundant data from the Qingyuan Ker Towers, field plot arrays, and carbon flux facilities.
By developing general hardware modules with multi-source and heterogeneous all-factor interfaces, stable and reliable access to carbon flux data in variable conditions in the field can be achieved (Gao et al.
Data analysis, management, and applications Analysis and application of forest three-dimensional structure and other information CSF requires the application of AI algorithms to analyze vast amounts of data, enabling real-time and accurate predictions of climate change impacts, thereby developing and implementing effective forest management measures.
The Qingyuan Forest CERN has integrated three-dimensional structural information of forests for data storage and analysis, creating a one-stop intelligent forest management platform.
This platform will develop into a "holographic perception + AI + decision support" system for monitoring and displaying three-dimensional forest structure and carbon sink.
Important functionalities include (Gao et al.
2023): (1) Displaying three-dimensional scenes of virtual terrain, incorporating digital elevation model data acquisition, terrain texture selection, and local terrain texture modification; (2) Realizing three-dimensional environmental expressions, incorporating memory optimization, large terrain chunk loading, and multi-threading strategies to enhance system responsiveness; (3) Enabling queries of individual tree information within the watershed; (4) Embedding growth prediction models into ecological environment virtual simulations for dynamic modeling of tree growth; (5) Supporting the import and export of vector and raster data for forest vegetation condition analysis; (6) Reconstructing three-dimensional stand using ground-based LiDAR and tree growth models, employing Digital Twin technology to preliminarily simulate various thinning schemes for larch plantations, thereby facilitating intelligent management decisions in forestry.
Analysis and management of forest ecosystem carbon–water flux data With the support of IoT and data centers, intelligent management has been achieved for major plots and equipment.
The system integrates monitoring data from the atmosphere, hydrology, biology, and soil for storage, analysis, management, and sharing (Gao et al.
The main carbon flux instruments can perform intelligent control measurements and automatic calibration operations, completing data correction calculations, quality assessments, and estimation of characteristic quantities (Fig.
Through thematic maps and user-defined options, calculations of forest carbon flux are conducted, displaying key variables in real time, such as forest carbon flux and automatically diagnosing the operational status of main carbon flux instruments at the Qingyuan Ker Tower platform (Gao et al.
The “hydrological automatic observation station network” and IoT, structured in a three-level arrangement, transmitting and displaying hydrological monitoring indicators in real time.
By combining forest structure and carbon flux observations, scientific questions related to carbon–water cycling, hydrological processes, and regulation mechanisms in forest ecosystems are being researched (Gao et al.
Conclusions and prospects With anthropogenic climate change as the “defining issue of our time” (United Nations 2020), the emergence of CSF is inevitable, and it will undergo further development and gain wide acceptance and applications.
CSF aims to enhance the resilience of forest ecosystems under a changing and uncertain climate, ensuring that ecosystem functions do not deteriorate despite possible changes in ecosystem states.
This resilience can be accomplished by resistance, recovery, and positive transformation.
CSF aims to improve the capacity of forest ecosystems to mitigate climate change, a critical part of achieving the “carbon neutrality” goal.
The carbon sequestration potential of forest ecosystems is immense, making them a central component of nature-based climate solutions.
Understanding the interaction mechanisms between forest ecosystems and climate change is crucial for achieving efficient, stable, and sustainable forest ecosystem functions, ultimately realizing the harmonious relationship between humans and nature.
Given the urgency of enhancing the carbon storage capacity of forests and the complexity of ensuring the resilience of forest ecosystems through climate change adaptation, CSF must deliver forest management methods and decision-making systems using the latest technologies, such as AI and digital transformation, to address the challenges posed by climate change.
In the future, CSF should focus on the following research areas: (1) Understanding mechanisms of resilience and carbon storage: Clarify the mechanisms for forming and maintaining the resilience and carbon sink capabilities of forest ecosystems and develop multi-faceted management methods to enhance forest resilience and carbon storage in response to climate change and natural disturbances.
(2) Exploring new paths for emission reduction and carbon sequestration: Investigate methods to reduce carbon emissions caused by natural disturbances, develop “carbon-based” industries, and achieve ex-situ carbon storage through timber production, utilization, and material substitution.
(3) Conducting comprehensive assessments of forest climate change mitigation effects: Evaluate the comprehensive effects of forests on mitigating climate change to balance the singular emphasis on carbon sink functionality.
Additionally, CSF should prioritize the development of the following key technologies: (1) Smart sensing technologies: Develop low-cost, multifunctional micro-sensors and associated platforms suitable for diverse environments to enhance the ability to acquire massive amounts of multi-source data (high precision, high frequency, and wide coverage), thereby transforming the paradigms of forestry data acquisition.
(2) Data analysis methodologies: Create a methodological framework based on AI and digital twins for data processing, scenario analysis, and predictive simulation, aimed at reducing uncertainties in modeling simulations caused by the high heterogeneity of existing forestry data sets, numerous interfering factors, and uneven distributions, thus revolutionizing traditional forestry research paradigms.
(3) Intelligent decision support systems: Develop a forest management system that promotes “harmonious coexistence between humans and nature” in the context of climate change, incorporating AI decision-making modules into this system and establishing a visual decision-making platform to transform the forestry management paradigm.
Abstract: Forest and urban fires have been and still are serious problem for many countries in the world.
Currently, there are many different solutions to fight forest fires.
These solutions mainly aim to mitigate the damage caused by the fires, using methods for their early detection.
In this paper, we discuss a new approach for fire detection and control, in which modern technologies are used.
In particular, we propose a platform that uses Unmanned Aerial Vehicles (UAVs), which constantly patrol over potentially threatened by fire areas.
The UAVs also utilize the benefits from Artificial Intelligence (AI) and are equipped with on-board processing capabilities.
This allows them to use computer vision methods for recognition and detection of smoke or fire, based on the still images or the video input from the drone cameras.
Several different scenarios for the possible use of the UAVs for forest fire detection are presented and analyse in the paper, including a solution with the use of a combination between a fixed and rotary-wing drones.
Published in: 2019 42nd International Convention on Information and Communication Technology, Electronics and Microelectronics (MIPRO) Date of Conference: 20-24 May 2019 Date Added to IEEE Xplore: 11 July 2019 ISBN Information: Electronic ISSN: 2623-8764 DOI: 10.23919/MIPRO.2019.8756696 Publisher: IEEE Conference Location: Opatija, Croatia SECTION I.Introduction The most up to date information on the current fire season in Europe and in the Mediterranean area is provided by the European Forest Fire Information System EFFIS [1].
Each year this institution provides annual report on the forest fires in Europe, the Middle East and North Africa.
According to the latest report, which they provided for 2017 [2], the dramatic effects of wildfires have caused damages of over 1.2 million hectares burnt natural lands in the EU and killed 127 people, including fire fighters and civilians.
Over 25% of the total burnt area was in the Natura 2000 network, which destroyed much on the efforts of the EU countries to preserve key natural habitats and to save the biodiversity of Europe for the future generations.
The same report says that these fires caused estimated losses of around 10 billion euros.
Despite these large numbers, EFFIS informs also that the report is showing a decrease in the number of fires, compared to the number of fires, which occurred annually during the last decade.
This decrease can be explained with the more severe actions and sanctions to the people that caused the wildfires and with the introduction of more advanced technical solutions for early detection of fires.
Obviously, the fight against fires can mitigate the damages, but the numbers, which represent the burnt area and the human lives, are still huge.
This reason presents the necessity to constantly develop, implement and upgrade the solutions and systems for fire detection.
The most important factors in the fight against forest fires include the earliest possible detection of the fire event, the proper categorization of the fire and fast response from the firefighting departments.
The aim of the proposed platform is not only to use modern technologies, but also to improve the abovementioned factors by reducing the fire detection time, by minimizing the false alarms and by issuing of timely responses and notifications to the fire services in case of real forest fires.
In the paper, we discuss the proposed platform for early forest fire detection, which involves two types of UAVs – a fixed-wing drone and a rotary-wing drone.
Both UAVs will be equipped with cameras, which will be optical, thermal or both.
The fixed-wing drone will constantly patrol the monitored area and will observe the territory below.
Since this drone will fly at medium altitude (350 m to 5500 m), it might report false alarms because of the altitude or the lack of clear visibility.
If the fixed-wing UAV detects a fire, it will trigger an alarm, which will activate the rotary-wing drone.
The rotary-wing drone will then closely inspect the area, where the fire is suspected to have occurred, by using the GPS coordinates provided by the patrol drone.
The role of the second drone is to either confirm or reject the alarm bases on its close observation of the area and will then go back to its base station.
It will not permanently monitor the targeted area.
The reason to use a second drone is to reduce the number of false-positive alarms as the rotary-wing drone will fly at much lower altitude (10 m to 350 m) compared to fixed-wing UAV and will have better and more detailed visibility of the area.
If the fire is confirmed, another alarm will be triggered by the rotary-wing drone and the ground level teams and the fire protection departments will be informed.
The platform is completely automated since both drones have on-board computers and processing capabilities.
They can detect fires based on the data captured by their thermal cameras and they can process this data without the need for centralized computing engine.
In addition and to further improve the platform, we have planned to implement artificial intelligence by allowing the drones to make fire predictions based on computer vision techniques.
In order to implement this artificial intelligence solution we will rely on and use neural networks.
The neural networks are currently a very hot topic in the computing systems, because of their ability to “learn” how to perform tasks by considering examples, without being programmed or instructed to follow specific rules.
The neural networks are inspired by the biological neural networks that constitute human brains.
SECTION II.Conceptual Model of A Platform For Early Forest Fire Detection This section describes the conceptual model of a platform for early forest fire detection that is going to be implemented under an international project entitled  “Forest Monitoring System for Early Fire Detection and Assessment in the Balkan-Med Area” SFEDA.
The project was designed with the intention to create a transnational cooperation among the countries in the Balkan-Mediterranean Area and more specifically between Bulgaria, Greece and Cyprus.
The goal of the project is to achieve the proof of the effectiveness of the technology and the implementation of a system for early detection and prevention of wildfires targeting a positive environmental impact and climate change resiliency.
The purpose of the project is to apply and demonstrate three differently implemented platforms for wildfire detection in three forests in the different countries (Bulgaria, Greece and Cyprus) and by sharing experiences and expertise to promote and strengthen the cooperation of the cross-border partners and improve the infrastructure for fire surveillance.
All of the three developed platforms will be part of one system under the name THEASIS.
The focus of this paper is to investigated the possibilities and development stages of the platform for early forest fire detection, which is going to be implemented by the University of Ruse on the territory of National Park “Rusenski Lom” near Ruse, Bulgaria.
Model of the platform for early forest fire detection Fire detection systems for outdoor environment could be implemented by using specialized cameras, which are able to capture multispectral images.
The biggest challenge that arises in these setups is where to place the camera(s) in order to have the best view on the observed territory.
Since these systems have their limitations, since they provide stationary point of view, we have decided to investigate a new approach.
The platform that is proposed in this paper will use unmanned aerial vehicles, which are going to patrol above the desired territory and will constantly observe for fire-related events.
The drones will be equipped with specialized optical and thermal cameras and will be able to capture video or still images.
In addition, the drones will also have constant bidirectional connection to the base station and they will be able to provide a feedback about their observations (Fig.
- The main part of the platform for early forest fire detection with use of fixed wing and rotatry wing UAVs  Figure 1.
The main part of the platform for early forest fire detection with use of fixed wing and rotatry wing UAVs  Show All  The platform will consists of two types of UAVs, which will fly at different altitudes as shown in Fig.
The terrain of National Park Rusenski Lom involves a steep canyon along the river covered by very dense forest vegetation.
The altitude variates from the ground level (0 meters) at reverbed to 150-170 meters at the highest points of the canyon.
This makes the location very difficult for observation.
To provide an overall overview of the park and to observe the difficult terrain we have decided to use a fixed-wing UAV with vertical take-off and landing.
The drone will fly at medium altitude and will provide long-term observations of the forest area of the national park.
The fixed-wing UAV will patrol, following a specific pattern, above the forest area and if it detects increased temperature levels by its thermal camera sensor it will immediately raise an alarm and will send the GPS coordinates of the area to its base station.
In order to reduce the false alarms we are planning to use second drone that will confirm the detection of the fire.
For that purpose, smaller drone with rotary wings will be used.
It will fly to the location of the potential forest fire by using the GPS coordinates provided by the fixed-wing drone and it will provide close inspection.
To have a better view of the observed territory the rotary-wing drone will fly at lower altitude in the range from 10 meters to 350 m.
- Flowchart of the operating principle of the early forest fire detection platform  Figure 2.
Flowchart of the operating principle of the early forest fire detection platform  Show All  The flowchart of the operating principle is provided in Fig.
As it can be noticed, the system implements three stages for fire detection.
The first stage (coloured in blue) presents the role of fixed-wing UAV.
To have a wide-angle view this drone will fly at an altitude from 350 meters up to 5500 meters.
If a fire is detected, the rotary wing drone starts its operation (green colour) by inspecting the suspected area from low altitude.
Its role is to confirm the fire.
If the fire is real then the drone informs the ground level firefighting services (orange colour) and continues its function to assist ground level services.
The second drone can be used also for post fire assessment.
Since both drones are going to be equipped with specialized multispectral cameras, a thorough analysis could be made.
Images captured by multispectral cameras can be processed and used for generating the NDVI (normalized difference vegetation index) maps of the terrain.
NDVI is a simple graphical indicator that can be used for fire damage assessments.
Planned equipment During the last decades, unmanned aerial vehicles have been widely used in different areas – military, agriculture, photography, fire service and many others.
These aircrafts are mainly classified into two types - fixed-wing UAVs and rotary-wing UAVs with both types having their advantages and disadvantages.
Since the developed platform is going to use both types of UAVs, it will also take advantage of their benefits.
The fixed-wing UAVs have several advantages, such as higher cruising speed and higher flight altitude, high flight efficiency, long endurance and range.
Rotary-wing UAVs on the other hand are more flexible, since they can take-off and landing vertically no matter of the type of environment.
Nowadays there are hybrid drones that combine the benefits of both.
After making a thorough analysis, we have decided to use ALTi Transition-F vertical take-off and landing (VTOL) fixed-wing UAV [11], which together with its ground control station are shown in Figure 3.
The ALTi Transition-F is class leading VTOL fixed-wing unmanned aircraft, developed as an ultra-compact, efficient and affordable system with the ability to take-off and land vertically almost anywhere with endurance of up to 12 hours and unmatched real world performance, according to its manufacturer [11].
The dimensions of the aircraft are 3000 mm wingspan, 2300 mm length and 525 mm height and its maximum take-off weight is 16 kg.
The main wings are removable, which significantly reduces the size and allows for rapid deployment, transport and storage.
Depending on the payload, the endurance of the UAV varies, for example with 2.8 kg payload the endurance time is about 10 hours.
The high endurance is due to the enhanced aerodynamic design with ultra-lightweight carbon fuselage.
- ALTi Transition VTOL aircraft and its ground station [11]  Figure 3.
ALTi Transition VTOL aircraft and its ground station [11]  Show All  The telemetry and control links between the drone and its ground station are completed using two channels for data communication.
One of the channels is duplex for simultaneous bidirectional control and data transfer, while the other is used as radio channel for high definition real time video streaming.
The second channel is set to work in simplex mode for downstream video transfer.
That video is going to be used for analysis of the observed area.
- The NightHawk 2 camera and its parameters [12]  Figure 4.
The NightHawk 2 camera and its parameters [12]  Show All  The high altitude drone will be equipped with NightHawk 2 EO/IR camera with 20x zoom and thermal resolution of 640x480 as shown in Fig.4. This camera is able to capture different temperature levels, and once the UAV detects increased or abnormal temperature levels it will immediately raise an alarm and will send the GPS coordinates of the problematic area to its base station.
The camera weighs only 250 grams, which will not cause significant downgrade in the drone performance and will not reduce its endurance.
Since the drone will fly at higher altitude, the view distance from the camera to the ground surface could be significant and this could lead the reporting of many false alarms.
In order to minimize their number a second drone with rotary-wings will be used.
The use of a rotary-wing UAV will provide the possibility for close inspection.
It will be equipped with higher quality camera and it fly at lower altitude for better visibility.
To confirm the detection of the fire we have planned to use as rotary-wing UAV the DJI Matrice 210 RTK drone, which is shown in Fig.
The advantage of the Matrice 200 series of drones it the fact that they are IP 43 certified, which means that they can withstand humidity and can fly in foggy or rainy conditions.
- DJI Matrice 210 RTK with dual gimbal [13]  Figure 5.
DJI Matrice 210 RTK with dual gimbal [13]  Show All  The reason to choose this drone is its dual downward gimbal, which allows it to carry two cameras.
The drone can be equipped with one IR and one standard/zoom camera.
We are planning to use the Zenmuse X4S 4K optical camera, which comes with a 20-megapixel 1-inch sensor, with maximum ISO of 12800 and increased dynamic range.
The second camera on the drone will be Zenmuse XT2 thermal camera, which integrates a high-resolution FLIR thermal sensor and a 4K visual camera with good stabilization and processing technology for quick transformation of aerial data into powerful insights.
As further improvement of the platform, we have planned to implement artificial intelligence by allowing the drones to make fire predictions based on computer vision techniques.
In order to implement image recognition a computing engine is required.
Another benefit of the drones is the fact that they can be equipped with high performance on-board computers, which enables their developers to transform these aerial platforms into truly intelligent flying robots that can perform complex computing tasks and advanced on-board image processing.
Example of one such high-performance embedded computer, specially designed for the DJI series of drones is the DJI Manifold [14].
The Manifold has the processing power of a graphics card for PCs and supports DirectX 11 and Open GL 4.4. It also supports NVDIA CUDA, which allows it to be used for processing in many AI applications, including for computer vision and deep learning.
This means that the developed aerial platform will perform on-board image recognition and could raise an alarm if it detects smoke or fire in the images, which it captures and processes.
This will lead to decreased fire detection and reporting times.
Development stages There are three main development stages for bringing the platform for early forest detection in action.
They include the planning, the designing and the building of the system.
In the implementation process, most of the project team will be involved with distributed tasks.
The planning stage involves meetings of the team, discussions and building of a conceptual model, as well as defining the specifications of the equipment that is going to be purchased.
The designing stage involves prebuilding tasks, which include clarification of the conceptual model, purchasing of the equipment and additional discussion and talks.
The last and most difficult stage from the development process is the actual building of the system.
This stage involves actions that are separated in two main tasks: preparation of the system components and laboratory testing of components.
These actions must be implemented before the actual use of the system.
The preparation of the system components involves tasks as components testing, assembling of the components, camera testing, DSP module testing, GPS module tests and also troubleshooting of the system, while the laboratory testing involves practical tests of the UAVs and their components and laboratory testing of the fire detection system.
In addition, the system could be improved by implementing computer vision (CV) techniques [3], [4], [5] and [6].
For this purpose, we have used artificial intelligence concepts for training a neural network to recognize smoke in images taken from the drone.
Before providing more details about our CV implementation, we have included some basic information about artificial intelligence, neural networks, deep learning and the connection between them.
Smoke detection using images can be defined as binary classification problem, in which we have as input an image, which has to be classified as containing smoke or not.
If it is classified as image, which contains smoke, the reported output value is one.
Otherwise, the output value is zero.
SECTION III.Artificial Intelligence, Neural Networks and Deep Learning Artificial intelligence has become extremely popular in the recent years as it has the ability to perform tasks, which are inherent to a human mind.
Artificial intelligence, sometime referred to as machine intelligence, is implemented by using neural networks.
The neural networks are specialized computer models, which can be trained to perform different tasks.
They are used for classification of images, speech recognition, translation of texts and more complex tasks, like control of autonomous vehicles, etc.
There are several types of neural networks, but the most widely used for image detection and computer vision are the convolutional neural networks [7], [8].
They consists of input layer, hidden layers and output layer of interconnected neurons, as shown in Fig.6. Depending on the number of hidden layers, we have machine learning methods (with just one hidden layer) and deep learning methods (with more than one hidden layers), in terms of methods for training the neural networks.
For example, Fig.
6 presents a deep neural network, since it has two hidden layers.
- Example of neural network with two hidden layer  Figure 6.
Example of neural network with two hidden layer  Show All  Input neurons represent the data, which is going to be used for training.
For example, if an input is an image the input neurons might represents the values for each pixel.
Neurons hidden in the middle layers usually perform mathematical computations.
The links between neurons are parameterized with weights, which dictate the importance of the input value.
- Image detection principle performed by neural network model  Figure 7.
Image detection principle performed by neural network model  Show All  All of the weight are randomly set, but during the learning process, they can change in order to fine-tune the loss function.
Each neuron in the network has activation function, which is extremely important for the final result.
The image detection principle is shown on Fig.7. This example reveals how neural network can recognize a digit from a given image with resolution of eight pixels by eight pixels (the low resolution is given for simplicity).
All of the image pixels are passed to the model as input neurons.
Depending on the weights assigned to the links, different sets of hidden layers might be activated.
The uniqueness of the activated neuron defines the output.
Before performing such complex tasks, each neural network must be trained.
The training can be describes as a process of finding the weights of the links between the neurons, where the loss function is minimized.
The training could be supervised and unsupervised.
Machine learning systems learn how to combine inputs to produce useful predictions on never-before-seen data.
In the supervised learning approach, the machine learning algorithms construct models by examining many examples and attempting to find a model that minimizes the loss.
The loss is defined as the difference between the actual value and the predicted output.
The loss function is minimized by changing the values of the weight of the links between the neurons.
Supervised learning can be used on both structured and unstructured data.
Simple machine learning algorithms work well with structured data, but when it comes to unstructured data, their performance tends to be low.
This is where neural networks have proven to be so effective and useful.
They perform exceptionally well on unstructured data.
Structured data is well defined input that has meaningful values, while the unstructured data refers to things like audio and images, where the goal is to recognize what is in the image or what the text is (like object detection).
Here the features might be the pixel values in an image and it is not clear what each pixel of the image represents by itself in the image and therefore this falls under the unstructured data.
- Comparison between image classification, object-detection and instance segmentation  Figure 8.
Comparison between image classification, object-detection and instance segmentation  Show All  Based on the discussion from above, the system for early forest fire detection can be categorized as binary classification problem.
The image classification models classify images into a single category, usually corresponding to the most salient object.
In the forest, the most salient object could be a tree, a river, a bush or even the forest itself.
For this reason, the image classification as a particular solution could not be effective.
Assigning a label with image classification models can become tricky and uncertain.
Object detection models are therefore more appropriate to identify multiple relevant objects in a single image or in our case just one the smoke.
There is one more advantage of object detection and that is the ability to localize the object in the image.
Comparison between image classification, object detection and instance segmentation is provided in Fig.8.  SECTION IV.Building of A Computer Vision Neural Network For Detection of Smoke In Images In order to improve the platform and to implement the smoke detection functionality from still images it is first necessary to train a network to learn how to recognize the smoke.
There are several steps to do that.
To utilize the object detection algorithms we first need to define the input data.
The input data, also known as dataset is a set of images, in which smoke is present, marked and labelled.
The dataset must be separated in two parts – for training and for testing.
This is the main requirement to avoid the so-called overfitting.
Sometimes after training, neural networks are performing very well with the training data (or very similar images) and not so well on new images.
This is called overfitting the model and it is illustrated in Fig.
Actually, there are two things to do with the data.
The first one is to estimate the parameters for the machine learning methods and the second one is to evaluate how well the machine learning methods work.
A bad approach would be to use all of the data to estimate the parameters (i.e. train the algorithm) because then there would not be any data left for testing the method and in that case, the model might become overfitted.
Reusing the same data for both training and testing is also not a good idea, because in order to evaluate the model it is needed to know how the method will work on data, which was not used for its training.
A good separation of the dataset is about 75% of the images for training and 25% for testing.
- Fine-tuning against overfitting of the model  Figure 9.
Fine-tuning against overfitting of the model  Show All  Fig.
9 reveals the fine-tuning against the overfitting of the model.
Assuming that the blue crosses are training data, if the model is trained only on that data, it might become overfitted, meaning that if new data is passed to the model (green crosses) there will be a high loss function.
After collecting many images for the dataset, it is necessary to annotate them all.
Annotation includes specification of the object coordinates and a corresponding label.
For the smoke detection model, we have collected about 300 images, which include smoke.
For their labelling, we have used the LabelImg tool [10], which is a graphical image annotation tool written in Python and uses Qt for its graphical interface.
After the labelling of the images, we have used a ready script to convert the XML files to a.csv and then to create the TFRecords.
The TFRecord input data is needed because we have used Tensorflow [9] as a training platform.
We have separated the input data to be 80% (240 images) for training and 20% (60 images) for testing.
After the creation of the required input files for the Tensorflow Object-Detection API, the model can be trained.
For the training, an object-detection training pipeline is needed.
Training an object detector from scratch can take days, even when using multiple GPUs. To speed up the training we can take an object detector trained on a different dataset and reuse some of its parameters to initialize the new model.
For that purpose, we have downloaded a model named ssd_mobilenet_v1_coco [15].
The model comes with preconfigured pipeline configurations.
It is only necessary to adjust the num_classesto one (because we only have one class - smoke) and to set the path for the model checkpoints, the training and test data files as well as the label map.
In terms of other configuration parameters, like learning rate, batch size and others the default settings would probably be ok.
Training can be done either locally or on the cloud.
GPU processing unit with at least 2GB memory is acceptable for local computing.
We have started training on a computer with 4GB GPU.
At every 10,000 steps of the training, the process is saved as a checkpoint.
It is recommended to evaluate the checkpoints from time to time in order to avoid overfitting the model.
After finishing with the training, the model has to be exported to a single file (Tensorflow graph proto), so it can be used for inference.
If more images are used for the input dataset, the model could become more accurate, but in that case, there is a tradeoff between the model speed and the model accuracy that one must consider.
SECTION V.Conclusions The system for early forest fire detection is still in its development stage.
We are still waiting for some equipment to be purchased, but we have planned and discussed the actual implementation.
We have performed a thorough research and some simulation experiments and we believe that we follow the right way to achieve the goal.
We also believe that we apply adequate approach that is also up-to-date.
We think that the system could enhance the available platforms for fire detection and we hope that such improvement could significantly reduce the damages caused by untimely or late fire detection.
first_pageDownload PDFsettingsOrder Article Reprints Open AccessEditor’s ChoiceArticle Digital Transformation in Smart Farm and Forest Operations Needs Human-Centered AI: Challenges and Future Directions by Andreas Holzinger 1,2,*ORCID,Anna Saranti 1ORCID,Alessa Angerschmid 1ORCID,Carl Orge Retzlaff 1,3ORCID,Andreas Gronauer 4ORCID,Vladimir Pejakovic 4ORCID,Francisco Medel-Jimenez 4ORCID,Theresa Krexner 4ORCID,Christoph Gollob 5ORCID andKarl Stampfer 6ORCID 1 Human-Centered AI Lab, Institute of Forest Engineering, Department of Forest and Soil Sciences, University of Natural Resources and Life Sciences Vienna, 1190 Wien, Austria 2 xAI Lab, Alberta Machine Intelligence Institute, University of Alberta, Edmonton, AB T5J 3B1, Canada 3 DAI Lab, Technical University Berlin, 10623 Berlin, Germany 4 Institute of Agricultural Engineering, Department of Sustainable Agricultural Systems, University of Natural Resources and Life Sciences Vienna, 1180 Wien, Austria 5 Institute of Forest Growth, Department of Forest and Soil Sciences, University of Natural Resources and Life Sciences Vienna, 1180 Wien, Austria 6 Institute of Forest Engineering, Department of Forest and Soil Sciences, University of Natural Resources and Life Sciences Vienna, 1180 Wien, Austria * Author to whom correspondence should be addressed.
Sensors 2022, 22(8), 3043; https://doi.org/10.3390/s22083043 Submission received: 16 March 2022 / Revised: 6 April 2022 / Accepted: 13 April 2022 / Published: 15 April 2022 (This article belongs to the Special Issue Cyber-Physical Systems for Automated Decision Making and Trusted Autonomy) Downloadkeyboard_arrow_down Browse Figures Versions Notes Abstract The main impetus for the global efforts toward the current digital transformation in almost all areas of our daily lives is due to the great successes of artificial intelligence (AI), and in particular, the workhorse of AI, statistical machine learning (ML).
The intelligent analysis, modeling, and management of agricultural and forest ecosystems, and of the use and protection of soils, already play important roles in securing our planet for future generations and will become irreplaceable in the future.
Technical solutions must encompass the entire agricultural and forestry value chain.
The process of digital transformation is supported by cyber-physical systems enabled by advances in ML, the availability of big data and increasing computing power.
For certain tasks, algorithms today achieve performances that exceed human levels.
The challenge is to use multimodal information fusion, i.e., to integrate data from different sources (sensor data, images, *omics), and explain to an expert why a certain result was achieved.
However, ML models often react to even small changes, and disturbances can have dramatic effects on their results.
Therefore, the use of AI in areas that matter to human life (agriculture, forestry, climate, health, etc.) has led to an increased need for trustworthy AI with two main components: explainability and robustness.
One step toward making AI more robust is to leverage expert knowledge.
For example, a farmer/forester in the loop can often bring in experience and conceptual understanding to the AI pipeline—no AI can do this.
Consequently, human-centered AI (HCAI) is a combination of “artificial intelligence” and “natural intelligence” to empower, amplify, and augment human performance, rather than replace people.
To achieve practical success of HCAI in agriculture and forestry, this article identifies three important frontier research areas: (1) intelligent information fusion; (2) robotics and embodied intelligence; and (3) augmentation, explanation, and verification for trusted decision support.
This goal will also require an agile, human-centered design approach for three generations (G).
G1: Enabling easily realizable applications through immediate deployment of existing technology.
G2: Medium-term modification of existing technology.
G3: Advanced adaptation and evolution beyond state-of-the-art.
Keywords: sensors; cyber-physical systems; machine learning; artificial intelligence; human-centered AI; smart farming; smart forestry; precision farming; precision forestry; AI for good  Graphical Abstract 1.
Introduction Cyber-physical systems (CPS), robotics, sensors, data management in general, and artificial intelligence (AI) and machine learning (ML) methods in particular, will significantly change process chains in agriculture and forestry.
Digital transformation in future smart agriculture and forestry requires a human-centered AI approach that incorporates sociological, ethical, and legal issues.
Natural intelligence should be augmented—not replaced—by artificial intelligence, like “power steering for the brain”.
This is where the human-in-the-loop approach comes in, because this approach incorporates the human experience, prior knowledge, and conceptual understanding of human experts to augment, enhance, and strengthen human capabilities with AI—rather than replacing humans.
In this paper, we first justify why agriculture and forestry are among the most important application areas for all humanity.
We then provide definitions of AI and HCAI to facilitate a common understanding, and describe the three main paradigms of ML (supervised learning, unsupervised learning, reinforcement learning) to provide a good introduction for the interested layperson.
We then describe the state-of-the-art in autonomous, automated, assisted, and augmented AI systems, giving examples from agriculture and forestry for each classification.
Then, in the main body, we introduce three pioneering research areas, namely, (1) intelligent sensor information fusion, (2) robotics and embodied intelligence, and (3) augmentation, explanation, and verification.
Finally, we summarize the core ideas of human-centered AI and present two examples: the farmer-in-the-loop and the forester-in-the-loop.
1.1. Why Both Agriculture and Forestry Are Important When you eat, it is about farming; when you breathe, it is about forestry.
Both agriculture and forestry are vital to everyone on our planet.
Both sectors have long and complex business process chains, and in no other sector could new AI technologies contribute more in the future to achieving the Sustainable Development Goals [1] (see Figure 1).
Sensors 22 03043 g001 550 Figure 1.
The United Nation’s seventeen Sustainable Development Goals (SDGs) [2].
Sustainable development can be seen as the intersection of the goals assigned to the ecological, economic, and social systems.
In this context, the systems are interrelated, and simply maximizing the goals for one system does not lead to sustainability; i.e., the impacts of all systems in their entirety must be considered to achieve sustainability.
Barbier and Burgess (2017) [3] note that focusing only on the goals of one system can have consequences for the other systems.
Furthermore, they describe sustainable development as a process of tradeoffs between systems.
For example, maximizing profits may be efficient for the economic system but threaten biological productivity and biodiversity through environmental degradation.
Moreover, the digital transformation process involves many more aspects than just the above systems and their goals.
The interactions between systems and actors must always be taken into account.
The European Union (EU) has therefore set out strategies to improve sustainability and meet the Sustainable Development Goals (SDGs).
One of the main objectives in this regard is to fully connect farmers and rural areas to the digital economy EC:2017:FoodFarming.
With this in mind, the European Commission overhauled the existing Common Agricultural Policy (CAP) to achieve a smarter, modern, and sustainable future for food and agriculture.
This resulted in the Green Deal, which is part of the Commission’s strategy to implement the Sustainable Development Goals.
The Green Deal also introduced the Farm to Fork strategy, which aims to transform the way food is produced and consumed in the EU.
It aims to make the food system healthy, fair, and environmentally friendly.
In addition, recital 22 of Regulation (EU) 2021/1119 [4] and the fact sheet [5] state that the Commission will promote new green business models to reward land managers for reducing gas emissions in general and cutting carbon emissions in particular.
This provides positive reinforcement for all land managers regarding the shift to green business models.
Last but not least, the vast amounts of data collected through “smart agriculture” will help farmers farm more efficiently and conserve natural resources [6].
As a result, food will be produced in a more sustainable and environmentally friendly way.
The same principle applies to forestry.
If the forest can be used in a more sustainable way, allowing not only the trees but also the soil and vegetation itself to regenerate, carbon reduction can be maximized.
The analysis, evaluation, and optimization of sustainable and resource-conserving production processes in agriculture require suitable methods that map the diversity of processes, represent the temporal and spatial variability, and make processes technically controllable.
Life cycle assessment (LCA) methods are already available for this purpose.
In the future, these methods will also be supported by AI, but let us first take a look at what AI actually is.
1.2. Artificial Intelligence Artificial intelligence is one of the oldest fields of computer science and was extremely popular in its early days in the 1950s.
However, the requirements quickly reached the limits of the computing power of digital computer systems at the time.
This made AI interesting in theory but a failure practically and especially economically, which inevitably led to a decline in interest in AI in the 1980s.
AI only became very popular again a decade ago, driven by the tremendous successes of data-driven statistical machine learning.
Artificial neural networks have their origins in the artificial neurons [7] developed by McCulloch and Pitts (1943).
Today’s neural networks consist of very many layers and have an enormous number of connections, and use a special form of compositionality in which features in one layer are combined in many different ways to produce more abstract features in the next layer [8].
The success of such AI, referred to as “deep learning”, has only been made possible by the computing power available today.
The increasing complexity of such deep learning models has naturally led to drawbacks and new problems in the comprehensibility of results.
This lack of comprehensibility can be very important, especially when using such AI systems in areas that affect human life [9].
Many fundamental AI concepts date back to the middle of the last century.
Their current success is actually based on a combination of three factors: (1) powerful, low-cost, and available digital computing technology, (2) scalable statistical machine learning methods (e.g., deep learning), and (3) the explosive growth of available datasets.
To date, AI has reached levels of popularity and maturity that have let it permeate nearly all industries and application areas, and it is the main driver of the current digital transformation—due to its undeniable potential to benefit humanity and the environment.
AI can definitely help find new solutions to our society’s most pressing challenges in virtually all areas of life: from agriculture and forest ecosystems, which affect our entire planet, to the health of every individual.
For all its benefits, the large-scale adoption of AI technologies also holds enormous and unimagined potential for new, unforeseen threats.
Therefore, all stakeholders—governments, policymakers, and industry—along with academia, must ensure that AI is developed with knowledge and consideration of these potential threats.
The security, traceability, transparency, explainability, validity, and verifiability of AI applications must always be ensured at all times [9].
However, how is AI actually defined now, what is trustworthy AI, and what is human-centered AI?
AI is difficult to define because the term “intelligence” itself is difficult to define [10].
We therefore follow a very general and widely accepted definition in this paper, namely, the one that describes AI simply as “automation of intelligent behavior”.
For more details, refer to Russel and Norvig (2020) [11].
For trustworthy AI, it is imperative to include ethical and legal aspects, which is a cross-disciplinary goal, because all trusted AI solutions must be not only ethically responsible but also legally compliant [12].
Dimensions of trustworthiness for AI include: security, safety, fairness, accountability (traceability, replicability), auditability (verifiability, checkability), and most importantly, robustness and explainability; see [13].
Human-centered AI we define as a synergistic approach to align AI solutions with human values, ethical principles, and legal requirements to ensure safety and security, enabling trustworthy AI.
This HCAI concept is now widely supported by renowned institutions (Stanford Human-Centered AI Institute, Berkeley Center for Human-Compatible AI, Cambridge Leverhulme Center for the Future of Intelligence, Chicago Human AI Lab, Utrecht Human-centered AI, Sydney Human-Centered AI Lab) and world-leading experts, such as Ben Shneiderman, Fei Fei Li, Joseph A.
Konstan, Stephen Yang, and Christopher Manning, to name a few [14].
The inclusion of a human-in-the-loop in interactive machine learning [15] is thereby not only helpful to increase the performances of AI algorithms, but also highly desirable to counter the earlier fears and anxieties that artificial intelligence automates everything, replaces and displaces humans, and pushes them into passive roles [16].
In addition, integrating a human-in-the-loop (expert-in-the-loop) has many other advantages: Human experts excel at certain tasks by thinking multimodally and embedding new information in a conceptual knowledge space shaped by individual experience and prior knowledge.
Farmers and foresters can build on an enormous amount of prior knowledge.
Our guiding principle, therefore, is that using conceptual knowledge as a guiding model of reality can help develop more robust, interpretable, and less biased AI models [17].
This can (a) provide advanced contributions to the international research community, (b) find new applications in various AI solutions, and (c) help add value to real-world applications, especially in areas that impact human life (agriculture, forestry, climate, health).
For all these approaches, machine learning is the “workhorse”, and here we are in the fortunate position that the term machine learning is very definable, unlike the term AI.
Since a basic understanding is very important here, we will discuss it in more detail in the following chapter.
1.3. Machine Learning—The Workhorse of AI It is important to note that the historical origin of the current successful statistical machine learning lies in the foundations described by Pierre Simon de Laplace (1781) [18], inspired by the work of Thomas Bayes (1763) [19].
Let us consider n data contained in a set 𝒟=𝑥1:𝑛={𝑥1,𝑥2,…,𝑥𝑛} .
Let be the likelihood 𝑝(𝒟|𝜃) , and specify a prior 𝑝(𝜃) .
Consequently, we can compute the posterior: 𝑝(𝜃|𝒟)=𝑝(𝒟|𝜃)∗𝑝(𝜃)𝑝(𝒟) The inverse probability allows us to learn from data, infer unknowns, and make predictions [20].
Here is the entry point where a human-in-the-loop can already help: in defining the prior.
A human-in-the-loop is therefore invaluable, because an expert with many years of experience has this “Bayesian estimate” ready in a fraction of a second in certain situations [21,22,23].
The question of “where the prior comes from” and the mere assumption of the same has been a point of attack for frequentist (or classical) statisticians, the opponents of the Bayesian approach [24].
This skepticism enormously delayed the development of “Bayesian” machine learning.
It was only through convincing performances in practical applications, particularly in the area of deep learning, that statistical machine learning was finally not only accepted, but gained popularity as the workhorse of AI today [25,26,27].
The field of machine learning began seven decades ago with the idea of developing algorithms that could automatically learn from data to gain knowledge from experience and incrementally improve their learning behavior.
It is one of the fastest growing fields at the nexus of computer science and statistics, and at the center of artificial intelligence and data science.
Today, the best practical implementations are autonomous vehicles, recommendation systems, and natural language understanding [28].
Ultimately, to reach a level of “usable intelligence”, we need (1) to learn from data, (2) to extract knowledge and new insights, (3) to generalize ideally from a small number of examples (4), to fight the curse of dimensionality, and (5) to disentangle underlying explanatory factors of the data, the causal factors—i.e., to make sense of the data in the context of an application domain [29].
Machine learning algorithms are typically divided into three main categories: (1) supervised, (2) unsupervised, and (3) reinforcement learning: Supervised learning includes algorithms that learn from human-labeled data, e.g., support vector machines (SVM), logistic regression, naive Bayes, random forests, and decision trees [30].
A typical example is a model that receives as input a set of images of crops and a set of images of weeds.
Each image is labeled by a human, and the neural network’s task is to learn the features that help distinguish between these two classes [31], which is nowadays performed by neural networks (deep learning approaches) using semi-supervised learning [32].
Typically, modern neural networks decompose inputs into lower-level image concepts, such as lines and curves, and then assemble them into larger structures to internally represent what distinguishes the two (or more) types of images they encounter during their learning process [33].
A trained network that has performed well on one classification task is expected to classify similar inputs (new images of cats and cars) with acceptable success; on the other hand, it is not expected to perform well on other tasks, so the generalization problem mentioned above shows the limits of the capacities of the algorithm.
Unsupervised learning includes algorithms that do not require human labels.
However, of course, some assumptions are always made about the structure of the data, typically after a visualization process [34,35].
Clustering algorithms that categorize data based on their intrinsic features were the first examples of unsupervised machine learning algorithms.
More recent neural network architectures, called autoencoders, compute more compact representations of the input data in a space of lower dimensions than that to which the input belongs.
These models can be easily used as generative models after the convergence of the learning process, thereby demonstrating their generalization ability in a constructive way.
Even if the human has no direct influence on these algorithms, there is interference in the form of configuration of some meta-parameters; even the choice of the appropriate unsupervised algorithm is made by the designer.
Some basic knowledge of the data is required, and techniques such as cross-validation are used to find good parameters and avoid over-fitting problems.
Reinforcement learning follows a very different paradigm.
The RL algorithm (often called agent here) bases its decisions on both the data and the human input, but the human input is not as direct as labeling [36,37].
To better understand this, it is important to remember that the tasks performed by reinforcement learning algorithms are not about categorizing the input data and learning the meaning of each feature, but rather about learning how to efficiently navigate to a goal.
What the algorithm needs to learn is a strategy for reaching the desired state from a starting point, guided not by a predefined plan but by a reward it will receive if it completes either the end goal or key subtasks.
The learning process includes several iterations (episodes) in which a so-called agent explores an environment randomly at the beginning and learns from its mistakes, and it eventually finds itself in unprofitable states (from the point of view of the reward).
Over time, the agent gathers knowledge about which states are more successful and exploits them to obtain the greatest possible reward.
Current state-of-the-art reinforcement learning algorithms are able to find strategies in complex games unknown to humans [38] and also use multiple agents communicating with each other to enable even more efficient strategy discovery [39].
The international ML community aimed from the very beginning to develop algorithms that automatically learn from datasets and improve their performances over time—without a human being involved [40].
This fully automated machine learning (aML)—“press the button and wait for the results”—works well when computational capacity is sufficient and, most importantly, large amounts of training data are available [41], and full autonomy is needed (e.g., in autonomous driving, or in scenarios where humans are absent).
The buzzword “big data” is in no way negative, but rather necessary for such automatic learning approaches.
However, in some situations we do not have the necessary big data and/or we are faced with complex problems, and in certain applications the use of fully automated approaches is very difficult to realize, e.g., for ethical reasons [42] or legal reasons [43].
Therefore, interactive machine learning (iML) approaches that integrate a human into the loop (e.g., a human kernel [44]), or incorporate a human directly into the machine learning algorithm [45], thereby leveraging human cognitive abilities, are promising approaches.
Sometimes (not always, of course) this human-in-the-loop can then bring in human experience, expertise, and conceptual understanding to solve problems that would not be solvable automatically alone, or improve algorithms stuck in suboptimal solutions, not knowing how to improve [46].
State-of-the-Art AI Technologies 2.1. Classification of AI Technologies If we want to give an overview of AI technologies, it is reasonable to classify them according to degree of autonomy: Autonomous AI systems that automate decisions without any human intervention, e.g., fully autonomous self driving cars [47] and autonomous drones [48].
Automated AI systems that perform labor-intensive tasks requiring certain intelligence and complete them automatically within a certain domain.
These have clear goals and tasks.
Examples are industrial robotic process automatization [49] and automated forest management [50].
Assisted AI systems that help humans perform repetitive routine tasks faster and both quantitatively and qualitatively better, e.g., ambient assisted smart living [51] and weather forecasting.
Augmenting AI systems that put a human in the loop or at least enable a human to be in control in order to augment human intelligence with machine intelligence and the opposite.
Examples range from simple, low-cost augmented reality applications [52] to augmented AI in agriculture [53] and interactive machine teaching concepts [54].
Today, AI can be successfully applied in virtually all application areas [55].
Due to resource conservation and the demand for sustainability, precision concepts, similar to precision medicine, are gaining more attention.
These include a very wide range of different information technologies that are already used in many agricultural and forestry operations worldwide [56,57,58,59].
In this context, satellite technology, geographic information systems (GIS), and remote sensing are also very important to improve all functions and services of the agricultural and forestry sectors [60].
Available tools include mobile applications [61], a variety of smart sensors [62], drones (unmanned aerial vehicles, UAVs) [63], cloud computing [64], Internet of Things (IoT) [65], and blockchain technologies [66].
An increasingly important and often underappreciated area is the provision of energy, making alternative low-energy approaches imperative [67].
All of these technologies make it possible to process information about the state of the soil, plants, weather, or animals in a shared network in quasi-real time and make it available for further processes regardless of location.
This means that today’s agricultural and forestry systems are being expanded to include other relevant processes/services, and additional datasets are being created for quantitative and qualitative information along the entire value chain for plant production and animal husbandry products and food safety (“from farm to fork”).
Let us now show a concrete application example for each type of our four AI classes.
2.2. Autonomous AI Systems “Full automation is one of the hottest topics in AI and could lead to fully driverless cars in less than a decade”, stated a 2015 Nature article [68].
Fully autonomous vehicles are indeed the popular example of AI and are also readily representable, as the Society of Automotive Engineers (SAE) has provided very descriptive definitions for levels of automation in its standards.
Levels of automation emerged as a way to represent gradations or categories of autonomy and to distinguish between tasks for machines and tasks for humans.
In a very recent paper, however, Hopkins and Schwanen (2021) [69] argued that the current discourse on automated vehicles is underpinned by a technology-centered logic dominated by AI proponents, and point to the benefits of a stronger human-centered perspective.
However, compared to car driving, the complexity of processes in agriculture and forestry is disproportionately higher.
Agricultural and forestry systems include virtually all processes for the production of f5 (food, feed, fiber, fire, fuel).
In this context, the production processes take place both indoors (buildings and facilities for people, livestock, post-harvest, and machinery) and outdoors, and face much diversity in terms of soil, plants, animals, and people.
The temporal resolution of process phenomena varies over an extremely wide range (from milliseconds, e.g., moving machinery, to many years, e.g., growth of trees and changes in soil).
2.2.1. Examples from Agriculture A major problem in agriculture has always been weed control.
In their daily life cycle, plants and weeds compete with each other for soil nutrients, water from the soil, and sunlight.
If weeds are left untouched, increased weed growth can affect both crop yields and crop quality.
Several studies have already shown that these effects can be significant, ranging from 48 to 71%, depending on the crop [70].
Moreover, in certain cases, crop damage can be so high that the entire yield is not suitable for the market [71].
To prevent this, weed control has emerged as a necessity.
Furthermore, with the ever-increasing trends in crop yield production, the demand for process optimization, i.e., reduction of energy losses, herbicide use, and manual labor, is becoming more and more urgent.
To meet the above requirements, traditional methods of weed control need to be changed.
One of the possible ways to achieve this is to introduce systems that significantly reduce the presence of human labor, the use of herbicides, and mechanical treatment of the soil by focusing only on specific areas where and when intervention is needed.
The novel approach based on the above principles is called smart farming or Agriculture 4.0. Moreover, this type of system should involve the performance of agricultural tasks autonomously, i.e., without human intervention, relying entirely on its own systems to collect the data, navigate through the field, detect the plants/weeds, and perform the required operation based on the results of the collected data [72].
These types of systems are known as autonomous agricultural robot systems.
Each autonomous agricultural robotic system, e.g., an autonomous robot for weed control, consists of four main systems, i.e., steering/machine vision, weed detection, mapping, and precision weed control [72].
Most agricultural robots are developed for outdoor use, though some of them can operate indoors [73].
Precise navigation of these devices is provided throughout the global navigation satellite systems (GNSS) and real-time kinematics (RTK) [74,75].
However, under certain conditions, localization accuracy may fall below the required thresholds, and then autonomous robotic systems must rely on machine vision and indoor positioning systems, such as adaptive Monte Carlo localization and laser scanners [76].
The above two technologies are widely used and commercially available.
Weed control in the row is mainly done by the four conventional weed control methods, i.e., electric, chemical, thermal, and mechanical weed control methods.
Currently, weed detection and identification is the most challenging issue.
Several studies have addressed this issue, with detection accuracy varying from 60 to 90% under ideal test conditions [72].
Thanks to extensive remote sensing technologies and data processing software, the development of weed maps has become a reality, and together with machine vision, a powerful tool for weed detection.
Some of the most representative autonomous agricultural robotic systems are: The robotic system for weed control in sugar beets developed by Astrand et al.
The robot consisted of two vision systems used for crop guidance and detection, and a hoe for weed removal.
A front camera with two-row detection at 5-meter range and near-infrared filter was used for row detection and navigation, while a second color camera mounted inside the robot was used for weed detection.
Initial trials showed that color-based plant detection was feasible and that the robot’s subsystems could functionally work together.
The BoniRob autonomous multipurpose robotic platform (see Figure 2) with wavelength-matched illumination system for capturing high-resolution image data was used for weed detection and precision spraying [78], and for ground intervention measurements [79].
Autonomous navigation along crop rows was achieved using 3D laser scans or by using global navigation satellite systems (GNSS).
(2002) developed a robotic system for weed control in cotton fields that is able to distinguish weeds from cotton plants and precisely apply herbicides.
A machine vision algorithm was used to determine the diameter of the inscribed leaf circle to identify the plant species.
Field tests showed a spray efficiency of 88.8 percent [80].
Sensors 22 03043 g002 550 Figure 2.
Field robot BoniRob [78].
Similarly to Astrand et al.
(2002) [77], Blasco et al.
(2002) [81] developed two machine vision system robots for weed control.
The machine vision systems are used separately, one for in row navigation and the second one for the weed detection.
Precise target weeding was done with an end-effector which emitted electrical charge [81].
(2017) [82] have developed an autonomous robot platform with a heterogeneous weeding array.
The weeding mechanism is based on machine vision for weed detection and classification, together with weeding array which combines precise spraying and hoeing methods for weed destruction [82].
As can be seen, robotic technologies are changing current practices in agricultural technology, particularly in autonomous weed control.
The steady increase in research and development in this area will inevitably have a significant impact on traditional agricultural practices.
2.2.2. Examples from Forestry Timber harvesting is physically demanding and risky, as forest workers often work manually and are exposed to heavy and fast-moving objects such as trees, logs, and dangerous machinery.
Over time, timber harvesting has become more mechanized to increase worker safety, productivity, and environmental sustainability.
In the context of increasing productivity through machine use, Ringdahl (2011) [83] found that human operators can become a bottleneck because it is not possible to work as fast as the potential capacity of machines.
In trafficable terrain, harvesters and forwarders represent the highest level of mechanization, and they are basically manually controlled by human using joysticks.
One way to overcome this human limitation of machine capacity is to change forest working methods in such a way that human activities are reduced to a minimum or are no longer required, like in autonomous vehicles [84].
While autonomous robotic systems are already being used in controlled workspaces such as factories or in simple agricultural environments, the use of autonomous machines in more complex environments, such as forests, is still in the research and development stage.
One of the biggest challenges is on-the-fly navigation in the forest.
The most common approach for autonomous navigation in open terrain such as agriculture is based on global navigation satellite systems (GNSS).
However, the GNSS signal absorption by the forest canopy leads to position errors of up to 50 m and more, which requires other solutions independent of the GNSS signal [85].
In addition to localization of the forest machine’s own position, the complex terrain and obstacles such as understory, and above all, trees, must also be taken into account when navigating autonomously in forests.
In recent years, methods in the field of remote sensing have increasingly been developed to generate digital twins of forests based of terrestrial, airborne, or spaceborne sensor technologies.
(2020) [86] showed that personal laser scanning (PLS) is able to capture and automatically map terrain information, individual tree parameters and entire stands in a highly efficient way.
This data can serve as a navigation basis for autonomous forest machines and the optimized operational harvest planning [85].
Rossmann (2010) [85] showed that an initial guess of the forest machine position can be made using an “imprecise” GNSS sensor.
2D laser scanners or stereo cameras on the forest machine (e.g., [87,88,89]) can detect tree positions in the near neighborhood of the machine (local tree pattern).
The position of the forest machine can be determined efficiently and precisely by means of tree pattern matching between the stand map (global tree pattern from, e.g., PLS) and the local tree pattern [85].
The initial guess of the machine position with GNSS helps to make the pattern matching more time efficient.
Regardless of the challenging navigation, research is also being done on the type of locomotion of autonomous forest machines.
Machines that seemed futuristic just a few years ago are already in use or available as prototypes.
For example, the concept of animals moving slowly from branch-to-branch was used by New Zealand scientists and engineers to build a tree-to-tree locomotion machine (swinging machine) [84] (see Figure 3).
To date, the swinging harvester has been radio-controlled—but with the challenges shown in terms of navigation and sensor fusion, the path to an autonomous, soil-conserving forestry machine is mapped out.
Sensors 22 03043 g003 550 Figure 3.
Tree to tree robot (image taken by SCION NZ Forest Research Institute, used with permission from Richard Parker).
2.3. Automated AI Systems 2.3.1. Example from Agriculture As previously mentioned, autonomous AI systems are relatively advanced and are constantly being developed.
These developments and upgrades lead to higher efficiency of the machines.
In addition, more and more systems in modern tractors and harvesters are becoming fully automated to minimize the operator’s workload.
The two most important domains of automation are situation awareness and process monitoring.
For example, machine vision guidance systems are already widely used in modern tractors and harvesters, allowing the machine to automatically align itself with the harvest line without the operator’s help, so that humans can focus on other processes while they do so [90].
Infrared 3D camera systems on harvesters continuously monitor and control bin placement while allowing the operator to focus on the harvesting process [91].
Process monitoring is particularly pronounced in harvesting operations, where speed must be constantly controlled and adjusted according to the operation being performed [92].
The precise application of fertilizers and herbicides is also usually monitored and controlled automatically throughout the process.
For this purpose, data from a global navigation satellite system (GNSS) as a guidance system with real-time sensor technology (e.g., Claas Crop Sensor [93]) are communicated among the tractor, the application device, and the task controller via the terminal, which has been done for some time [94].
2.3.2. Examples from Forestry Cable-yarding technologies are the basis for efficient and safe timber harvesting on steep slopes.
To guarantee low harvesting costs and low environmental impacts on remaining trees and soil, the machine position and cable road must be carefully planned.
For this planning, usually only imprecise information about the terrain and the forest stands is available.
If stand and terrain information were collected with traditional measuring devices such as calipers, hypsometers, and theodolites, these measurements would be labor intensive, time consuming, prone to various errors, and thus limited in their spatial and temporal extent [95].
Thus, the cable road layout is still determined by experts based on rules of thumb and empirical knowledge [96].
Rules for this are formulated, for example, in Heinimann (2003) [97].
Automatic methods (optimization methods) to solve this problem have already been formulated in countries such as the USA and Chile [98,99,100].
However, these optimization or planning methods are largely based on the assumption of clear-cutting and do not use modern sensor technology to capture individual tree and terrain data.
For example, high-resolution 3D data in form of a digital twin of the forest combined with well-known optimization functions and expert knowledge is a key factor to optimizing planning of timber harvesting.
In this way, automatically optimized cable road planning can help to minimize the environmental impact and the costs for cable yarding (e.g., [96,101]).
In terms of cable yarding, there are also other examples for automation that are already being used in practice: Most cable yarding systems follow a typical scheme (work phases) of unloaded out, accumulate load, loaded in, and drop load on landing.
Two of these phases, unloaded and loaded travel, have been automated; thus, the operator can work in the meantime with an integrated processor [88].
Pierzchała et al.
(2018) [102] developed a method for automatic recognition of cable yarding work phases by using multiple sensors on the carriage and tower yarder.
Further automation steps in cable yarding would be conceivable in the future; for example, the carriage could be equipped with additional orientation sensors, such as laser scanners or stereo cameras, for orientation.
2.4. Assisted AI Systems 2.4.1. Example from Agriculture Assisted AI systems in agriculture are tightly overlapped with automated AI systems.
In agricultural applications, machines can independently perform certain repetitive tasks without the human intervention.
However, in the decision-making loop, humans are those one who make final decisions [103].
For example, implementation of a wide variety of non-invasive sensors in fruit and vegetable processing, e.g., drying processes, merged together with AI technologies, can be used to control drying processes and changes in shape of vegetables and fruits, and to predict optimum drying process parameters [104].
Several systems, e.g., situation awareness systems such as machine vision guidance systems, though performing their work automatically, can be still manually overridden by an operator [105].
An example is the precision application of fertilizer and pesticides: sprayers can work in fully manual mode [90].
In modern tractors, advanced steering control systems can adjust steering performance in order to suit current conditions, etc.
Furthermore, fuel consumption efficiency can be improved with the above-mentioned technologies [107].
2.4.2. Examples from Forestry Operating with forestry cranes requires a lot of knowledge and experience to be productive with a low impact on the environment.
Furthermore, trained forestry machine operators are essential for efficient timber production, in particular to reduce harvesting damage to the remaining trees and reduce machine downtime.
Ovaskainen et al.
(2004) [108] has shown that the productivity of trained harvester (Cut-to-length (CTL)) operators varies by about 40% under similar forest stand conditions.
The study hypothesizes that efficiency differences are related to aspects of operator crane experience based on deliberate practice of motor skills, situational awareness, and visual perception.
The state-of-the-art in crane control is the use of two analog joysticks, which are controlled by the two hands and/or the fingers.
The joysticks provide electrical or hydraulic signals that control the flow rate of the hydraulic system and thus enable precise movement of the individual hydraulic cylinders.
Motor learning is the key to smooth crane movements and harvester head control.
Forest machinery machinists make approximately 4000 control inputs/h, many of which are repeated again and again but always have to be applied in a targeted manner [109].
Purfürst (2010) [110] found that learning to operate a harvester took on average 9 months.
Furthermore, the operator must also master decision making and planning in order to achieve an appropriate level of performance.
In summary, it can be stated that harvester/forwarder operation, especially crane operation, is ergonomically, motorically, and cognitively very demanding.
To improve this, existing forestry machines are constantly being improved.
Modern sensors (e.g., diameter and length measurement) combined with intelligent data processing can help to assist certain operations, such as processing stems into logs by automatically moving the harvester head to predetermined positions depending on the stem shape and log quality.
On the one hand, this reduces the workload of the harvester operator, and on the other hand, optimizes the profit on the timber.
Other good examples of how intelligent assistance can make work easier and also more efficient for the machine operator are the intelligent crane control systems from John Deere Forestry Oy (IBC: Intelligent Boom Control [111], see Figure 4), Komatsu (Smart Crane [112]), and Palfinger (Smart Control [113]).
In such systems, the crane is controlled via the crane tip (harvester head or grapple), and the crane’s movement is automatically done via algorithms.
Therefore, the operator is not controlling individual rams, but only needs to concentrate on the crane tip and control it with the joysticks.
The system also dampens the movements of the cylinders and stops jerky load thrusts in the end positions, which enables jerk-free operation.
The smart control results in less fatigue for the machinist, making them more productive overall.
Results from Manner et al.
(2019) [114] showed that if the crane is controlled with IBC compared to conventional crane control, the machine working time for the forwarder is 5.2% shorter during loading and 7.9% shorter during unloading.
It has already been shown that the use of such a smart crane control system makes it much easier to learn how to operate harvester or forwarder machines [88,115].
Sensors 22 03043 g004 550 Figure 4.
Principles of the IBC system [116].
2.5. Augmenting AI Systems 2.5.1. Example from Agriculture A good systematic for AR applications is given by Hurst et al.
(2021) [117] (see Figure 5 and Figure 6), which has subdivisions into (1) marker-based, (2) markerless (location-based), (3) dynamic augmentation, and (4) complex augmentation, subdivided by AR type.
Based on the four classifications, there are a lot of potential applications of AR in agriculture.
Sensors 22 03043 g005 550 Figure 5.
Types of AR deployment within crop and livestock management.
Please refer to the excellent overview by Hurst et al.
Sensors 22 03043 g006 550 Figure 6.
Analysis of technologies coupled with AR in Farming.
Dark blue refers to crop-bases articles, whereas light green is for livestock, adapted.
For details, please refer to the original paper by Hurst et al.
Augmented reality (AR) enables the combination of a real environment and an interactive experience, e.g., synthetically generated information.
It is necessary to clearly distinguish augmented reality (AR) from virtual reality (VR).
Virtual reality uses a synthetically generated environment to replace the real environment, whereas augmented reality enhances the real environment with synthetically generated data [118].
Both technologies have found many applications in a wide variety of domains [119,120,121].
However, agricultural applications require the technology to be even more user-friendly, for example, by replacing smartphones and tablets with smart glasses [122].
This would provide operators with hands-free capabilities and a less constrained user interface.
Although there are still some technical and technological drawbacks, smart glasses have emerged as promising potential candidates for the main platform for AR.
Meanwhile, head-mounted AR displays, for example, are being used to help farmers detect plant diseases [123].
Through the head-mounted display camera that observes the plants, images of the plant leaves are captured in real time and sent to the cloud server for analysis, which also provides a lot of room for detecting defects/anomalies.
After post-processing the data in the cloud, the results are transmitted back to the head-mounted display.
In this way, a augmented reality head-mounted display allows less experienced farmers to inspect the field more efficiently and quickly in search of infected plants.
In addition, such technology can also help train and educate the farmer directly in the field.
The farmer’s knowledge remains invaluable, as the expert can contribute their domain knowledge to future machine teaching AI solutions.
AR smart glasses are already used for scanning QR codes during characteristic livestock activities such as feeding and milking [124].
The initial results show that the above-mentioned glasses can provide significant help to farmers by enabling real-time consultation, data collection, data sharing, etc., and proved to be a useful tool for herd management and feeding, where many more applications will bring benefits to farmers in the future, especially through AI.
AR smart glasses (see Figure 7) [125] have already been implemented to create a system that assists the operator during field operations such as plowing and fertilizing.
This can minimize the strain on the operator caused by constantly tracking maps, light bars, etc., which can be especially pronounced in large, irregularly shaped fields.
With the help of AR glasses, the operator thus obtains data on their trajectory, speed, etc., which is superimposed on the data of the treated surfaces and largely simplifies the operator’s work.
It should be mentioned that this system can be used both inside the machine and outside it.
This system has proven to be very useful in fertilizing, spraying, and plowing operations.
Sensors 22 03043 g007 550 Figure 7.
AR-based positioning assist system: (a) tractor mounted, (b) manual mounted [125].
Besides the above-mentioned examples, augmented reality-related research is on the rise, mainly focusing on greenhouse management [126], weed management [127], and farmer management support [128].
2.5.2. Examples from Forestry Automated and assisting systems combined with a variety of modern sensors increase the productivity and quality of forest work.
Even if we are far from using the full potential of smart technology in forest machines, the operator is already receiving a large amount of information compared to traditional machines.
In addition, forestry machines are also increasingly networked with each other (e.g., harvesters and forwarders) and also have possibilities to retrieve or exchange information from the Internet.
On the one hand, this abundance of data helps to train autonomous, automatic, or assisting processes; but on the other hand, it leads to a challenge in mediating the information to the operator.
However, in addition to many of the benefits of “big data”, negative effects can also occur in the form of divided attention, information overload, and operator stress.
A further increase in the information burden on the operator can potentially lead to higher chances of human errors that could harm not only the operator, but also people, machines, and objects in the neighborhood of the machine [129,130,131].
Augmented reality can help to provide the information better and more efficiently to the machine operator.
Augmented reality, which matches data generated by sensors and algorithms with the user’s actual perception of the environment, can improve the operator’s awareness of the machine, the environment, and the specific work progress.
Sitompul and Wallmyr (2019) [129] defined for forest applications that augmented information could be provided for two types of operation: in-cabin operation and remote operation.
Traditionally, heavy machines, such as forestry machines, are operated in the cab.
In recent years, there have been repeated efforts and studies to move the operator from working in the cab to working in a remote control station, which is called teleoperation.
With regard to cab work, Kymäläinen et al.
(2017) [132] and Aromaa et al.
(2020) [133] have proposed to show technically related visual obstacles of the forestry machine (e.g., crane) transparently on a display.
The hidden areas (behind the crane) could be seen with the help of cameras.
This increases safety for the surrounding area.
In addition to classic screens, there is also the option of projecting information directly into the operator’s field of view via a heads-up display.
For example, the operator can be provided directly with information about the bucking optimization of the harvester without having to look at a separate monitor [134].
Teleworking mainly leads to hazard minimization for the operator.
The biggest challenge in teleworking is sufficient visibility, as the fields of view of the cameras attached to the machine are limited [135].
Furthermore, depth vision is lost due to the most commonly used 2D displays, which makes it difficult to position the crane exactly and grip logs.
For timber loading onto trucks, Hiab (HiVision [136], see Figure 8) and Palfinger (Virtual Drive [137]) each offer a control system for forestry cranes.
It allows the operator to control the crane from the truck cab while monitoring the environment with the help of a camera and VR goggles.
The advantages of the system are that the truck driver no longer has to leave the cab, thereby avoiding hazards, and the operator is ergonomically positioned.
Sensors 22 03043 g008 550 Figure 8.
Hiab HiVision VR system [136].
Due to the high cost of machinery and the dangerous nature of the work, great importance must be placed on the training of forestry machine operators.
Thus, in addition to supporting operational work, augmented reality also offers advantages in education and training.
With realistic simulations of forestry machines [138] and forest [139], a student can be trained in a safe environment in all work processes that occur in real operations.
AI Branches of Future Interest: Frontier Research Areas To achieve practical success in agriculture and forestry, we identify three important AI frontier research areas (see Figure 9: (1) intelligent sensor information fusion, (2) robotics and embodied intelligence, and (3) augmentation, explanation, and verification technologies for trusted decision support.
Such developments need novel, agile, human-centered design approaches with three generations (HCD-3G): Sensors 22 03043 g009 550 Figure 9.
3 × 3: The three frontier research areas with agile human-centered design in three generations.
G1: testing existing technology, G2: adapting existing technology, G3: advanced adaptation going beyond state-of-the-art.
Generation 1: Enabling an easily realizable application through immediate deployment of existing technology which can be solved at the “bachelor level”.
Generation 2: Medium-term modification of existing technology, which can be solved at “master level”.
Generation 3: Advanced adaptation and evolution going beyond state-of-the-art at “doctoral level and beyond”.
In the following chapter we describe some open challenges and future research issues from which we expect three forms of added value to arise: (1) contributions to the international research community, (2) theoretical contributions beyond the state-of-the-art, and (3) practically useful contributions that ultimately add value for users in agriculture and forestry.
3.1. Intelligent Sensor Information Fusion Smart applications in agriculture are characterized by the gathering of different types of data with the use of adequate sensors: soil, plant, animal, and environment sensors are used together for farm monitoring and management purposes [140].
There are a plethora of possibilities with the use of sensors that monitor physical and chemical signals, such as temperature, moisture, pH, and pollutants in real-time.
One definition of multi-sensor fusion can be found in [141]; the same phenomenon or entity that is described by an unknown random variable is observed by different types of sensors.
Through comparison, aggregation, and combination of several types of sensor data that are error-prone in general, the uncertainty about the random variable is decreased.
The sensors, particularly in agricultural and forestry applications, are exposed to hard environmental conditions that greatly vary, and therefore, cannot deliver error-free measurements as the ones in a protected laboratory environment.
In every step of the pipeline, including sensor data gathering, transfer, and storage, different types of faults can occur [142,143].
Adequate quality management (QM) measures [144] need to be implemented—both human-supervised and automated—to ensure a reliable outlier analysis and fault detection (FD) [145] as early as possible.
Sensor fusion can help not only error detection but also help the discovery of new insights with a variety of algorithms that basically compare the information content of several types of sensor data [146].
Data are typically combined under particular constraints, and at the same time, several conditions of consistency between them can help artificial intelligence systems to automate data preprocessing to a certain extent.
In the work of Lee et al.
(2010) [147] both thermal and RGB images were fused on the basis of similarity measures.
Beyond raw data fusion, features that characterize the input data can be extracted, fused, and processed by individual AI algorithms, parallel to the ones processing the raw data [148].
The insights from both systems can be then combined in a weighted or voting fashion, which generally provides a better resulting performance, since each part grasps different aspects of the data [149,150].
Clustering methods and hierarchical self-organizing maps (SOM) are also used to detect intercorrelations between the data to enable an even more effective fusion process [151].
In conjunction with novel wearable sensors [152], these can provide tremendous benefits for smart farming and smart forestry, providing important information to optimize plant growth, combat biotic and abiotic stressors, and increase crop yields.
Beyond sensors, there are also other sources where data can be gathered, such as robots, handheld devices, drones, airborne laser scan data, and weather satellite data; we see enormous added value for a wide range of applications.
Machine learning is an excellent way to achieve sensor fusion effectively.
A detailed review of state-of-the-art methods can be found in [153].
Least squares support vector machine (SVM) classifiers [34] (see also Section 1.3 about supervised learning) were some of the first that dealt with different types of agricultural data that might have different ranges and be sampled at completely different timepoints.
Open Challenge G1: “Garbage in-garbage out”—this motto of data scientists is there to always reminds us of the fundamental property of information entropy, as defined by Claude Shannon [154,155].
Since the information that is lost can never be fully and perfectly reconstructed—in the best case only approximated—one of the first and foremost goals is to make sure that the sensor information is gathered with as few problems as possible.
The sensor’s data gathering capability in difficult environmental conditions, and the continuous, (near-)real-time operation thereof and for the servers, need to be ensured.
The quality and the sensitivity of the sensor are defined by production but need to be verified in practice.
Together with human experts, the gathered data (both sensors and satellite) need to be analyzed, and the individual characteristics thereof need to be specified.
Open Challenge G2: Human experts have the capability to recognize abnormal behavior in sensor data by adequate visualizations and statistics.
Fault detection software, on the other hand, has to rely on anomalies in the data, which means that (1) the outliers need to be “rare” (relative) and (2) the values of different sensors need to be compared with each other.
What the vast majority of the sensors will track, will be roughly decisive for describing the whole data gathering, preprocessing, transferring, and detecting a fault either in a few of the sensors, all of them, or even the whole data transfer process.
Open Challenge G3: A reliable real-time data fusion system that has the intelligence to know when it is advisable to fuse different sensor data.
If data from the majority of different sensor sources are inconsistent, then the data fusion process should rather be discarded, since this is an indication of a fault in the data pipeline.
Ensuring that the gathered data lie in an acceptable range, are consistent with each other, and obey roughly some expected physical rules (radiance, humidity with respect to temperature) can open the path for successful and insightful information fusion.
3.2. Robotics and Embodied Intelligence Pieter Abbeel puts it in a nutshell in his presentations, e.g., at CVPR 2021: The hardware in robotics is there, it is capable and usable.
The real challenge is that the robots lack intelligence-which is defined by the underlying software.
This motivates why we do not focus on hardware aspects, but take existing hardware and work on “bringing the intelligence into it”.
Combining human capabilities with robotics and embodied intelligence is a promising approach, which is still largely unexplored and has enormous potential.
The team-ups of robots and humans could lead to exceeding their individual performances by combining the robot’s motor, vision, and computation capabilities with the perceptiveness and deep understanding of humans.
To achieve this goal, several current approaches have to be built upon and combined.
For one, it is essential to bring RL agents up to a certain base performance level before their human interaction should begin, in order to allow efficient use of humans’ time and to avoid frustrations.
Agents can be trained with synthesized or already gathered data under simulated conditions.
Of course, deviations from real conditions need to be expected, but nevertheless, the simulations can provide an upper limit in expectations and also help define some minimal requirements for the on-site operation.
To recognize if the agent has reached this acceptable base level, and since many RL problems are currently solved by deep RL techniques [37,156,157], performance metrics and explainable AI (XAI) techniques can be used [158].
These techniques can demonstrate the underlying reasons for the decision-making process of a deep RL agent and help humans understand which parts of the current state were most relevant for the action.
Furthermore, they help humans to understand the agent’s overall strategy and answer “what if” questions [17].
Then, the robot can efficiently learn through interaction with a human either by human demonstrations or preference-based learning [159].
Ultimately, the ongoing team-up can benefit from active learning approaches were edge cases are caught and solved by the human—also with the use of XAI methods—helping the robot to learn from those unknowns and generalize better in the future.
In order to enable a successful and efficient interaction between humans and RL agents, models need to have sufficient cognitive capacities for judging and further improving their behavior.
A good example for this requirement is preference-based learning [159].
In preference-based learning, a robot presents two options (such as movement policies) to a human operator, who selects a preference and with that facilitates the challenging reward-selection process.
In order for this to be effective, it is beneficial if the robot presents two “meaningful”, coherent movement policies, instead of the jittery behavior seen in newly instantiated models [160].
This exemplifies a more general statement: it is easier to judge the consistency of an already trained model, because it has already developed past the initial noise of random initialization.
One approach is pre-training, where models learn to reconstruct images in mostly self-supervised fashion from masked inputs.
A drawback on this approach is that the model inevitable learns on the bias and noise of the given samples, which hampers the goal of learning noise-invariant concepts [161].
Contrastive pre-training extends this approach by masking or modifying (cropped, rotated, colored etc.) the samples and then reconstructing them, adding noise in the training process and leading to a more robust generalization.
A concrete example for this application is the combination of contrastive pre-training and data-augmented RL, as proposed by Srinivas et al.
To ensure that agents can benefit from this pre-training, the exploration–exploitation dilemma has to be tackled.
Especially when training in an unsupervised fashion, the agent can get stuck in the exploitation phase without having sufficiently explored the available states.
Liu and Abbeel [163] proposed a state-entropy reward to ensure a better state-coverage with unsupervised pre-training.
A second approach is to transfer knowledge between networks, before fine-tuning them for a certain task.
[164] showed this approach by quickly learning knowledge (offline) from task-specific teachers, before continuing with an online-learning approach to further improve results.
This also exemplifies how a network is brought up to speed, before being further trained in a continuous, online fashion.
A central challenge in reinforcement learning is finding a good goal function, which can be extremely laborious and still fail to consistently capture the intended goal [160].
To work around the task of explicitly stating the goal function, demonstration learning leverages the demonstrations of an exemplary solution for a task by a human to teach the RL agent.
The agent can then extract behavioral priorities (capabilities) by fitting generative models to a large offline dataset of demonstrations.
This, however, often requires a large dataset of samples to achieve good results.
This approach was improved upon by Lin et al.
[165], who used sample-efficient demonstrations to help agents to better explore during training and derive the rewards from the given demonstration.
However, a drawback to demonstration-based generative models is that they inherit perturbations in the raw data, and therefore can gain unusable skills.
To better match skill extraction to human intentions, Pieter Abbeel’s group recently introduced the so-called skill preferences (SkiP) approach, an algorithm that learns a model about human preferences.
After extracting human-preferred skills, SkiP also uses human feedback to solve downstream tasks with reinforcement learning.
This has recently been used to solve complex, multi-step manipulation tasks [166]; see Figure 10.
Sensors 22 03043 g010 550 Figure 10.
Skill preferences (SkiP) [166] consists of two phases.
During the skill extraction phase, human feedback is used to learn skills.
During the skill execution phase, human feedback is used to finetune the skills to solve various downstream tasks.
First, skills are extracted from a noisy offline dataset with human feedback to denoise behavioral priors.
Second, skills are executed with RL in the environment with task-specific human feedback.
The general idea of “learning behavioral priors with human feedback” (skill extraction; see (a) in Figure 10) is to use human preferences in order to fit a weighted behavioral prior over an offline dataset of (potentially noisy) demonstrations.
SkiP builds on prior work for behavioral extraction from offline data via an expected maximum likelihood latent variable, e.g., as done in the OPAL approach [167].
They considered a parametric generative model 𝑝𝑎𝑙𝑝ℎ𝑎(𝑎𝑐𝑡𝑖𝑜𝑛𝑠𝑒𝑞𝑡|𝑠𝑡)  over action sequences where: 𝑎𝑐𝑡𝑖𝑜𝑛𝑠𝑒𝑞𝑡=(𝑎𝑡,…,𝑎𝑡+𝐻−1), which represents a behavioral prior, which was trained to replicate the transition statistics in the offline dataset: 𝑝𝛼∈argmax𝛼𝔼𝜏∼𝒟⎡⎣⎢∑𝑡=0log(𝑝𝛼(𝐚𝑡|𝑠𝑡))⎤⎦⎥.
(1) A third approach we want to highlight is active learning, where the agent actively queries the user for unknown data points, and is often guided by heuristics to determine uncertainty for sample selection.
This has proven to be an efficient method for training semi-supervised models that has far lower costs.
[168] showed an example for such an active learning approach for deep learning where they frame the sample selection process as an RL problem and with that generate a transferable heuristic.
[169] showed how the active learning approach can also be used for fine-tuning by quickly personalizing classifiers on multi-modal user data.
There are many farm management and information systems (FMIS) available on the market.
What they virtually all have in common is not mapping an entire farm, although terms such as “digital shadow” or “digital twin” can increasingly be found in the literature (e.g., [170,171]).
To date, only so-called isolated solutions can be assumed.
Future challenge lies in the complete mapping of entire farm systems, including the merging of all data streams in order to obtain information for the optimization of individual processes and entire farm systems.
In addition, it must be made possible for the farmer to incorporate their expert knowledge into these systems in order to make the individualization of a virtual farm operating system a reality, as is shown by Groeneveld et al.
(2021) [172] (see Figure 11).
One of the research questions is how to include the expert-in-the-loop in the most efficient way.
Sensors 22 03043 g011 550 Figure 11.
A feature model for precision agriculture farm management [172].
Throughout the last decades, a wide variety of autonomous agricultural vehicles have been developed, based on different platforms, control units, sensor sets, operational algorithms, etc.
Throughout the careful observation of all of these autonomous agricultural robots, several conclusions which can be used as a guidance for the designers can be derived.
First of all, the most practical transmission system for the wide variety of agricultural autonomous vehicles is automatic transmission.
Automatic transmission allows us precise control of performed operations, e.g., harvesting and fertilizing [73].
In order to control processes performed by autonomous agricultural vehicles, each vehicle has to have access to the engine controlling unit.
Furthermore, each autonomous vehicle must have a computer which receives and sends commands from/to the sensor set, and send commands to actuators.
Navigation is mainly performed by GNSS-based systems.
Last, but not the least, controlling algorithms should be as simple as possible [174].
We propose several research directions that are beneficial for successful human–machine interaction in the scope of human-centered AI in embodied intelligence.
A fundamental aspect that has to be taken into account is that generating trust in the system is essential for a fruitful interaction between the end-user and the robot.
This trust is built by making the end-user understand the perception and decision-making process of the robot agent, which necessitates a focus on explainability.
Current explainability research, however, focuses mostly on explanations for experts and system developers, less on the end user [175].
We suggest that further research is required into what human (and end-user)-centered AI systems could look like, focusing on aspects such as real-time computation, understandability, explanations for lay persons, and predictability of robot behavior in general.
First-generation tasks can focus on evaluating how current xAI approaches work and generating requirements for explainability from an end-user perspective.
Second-generation tasks could then focus on testing and evaluating different approaches, which provide better explainability within the given constraints.
The high-level, third-generation approach is developing a coherent framework for requirements and solutions providing explainability for embodied intelligence, collecting and exposing the developed xAI solutions.
This approach also encompasses guiding the development of approaches in the second generation, ensuring an even coverage of this multi-faceted explainability challenge.
Such a process eventually allows us to provide a comprehensive set of tools that developers of robotic systems could easily use for facilitating their human–robot interactions with strong explainability approaches.
Open Challenge G1: Before even starting on-site operations, several experiments with synthetic data under simulated conditions must be completed.
The scope of the challenges needs to be documented, along with the basic elements of the RL problems that will be faced down the line.
Basic thoughts about the state and action space of the problems at hand, the reward strategy, the obstacles, and the limitations need to be examined.
The feasibility of the solution, its scope, computational resources, and time resources need to be defined.
The first simple prototypes in the laboratory that use deep RL need to work efficiently.
Open Challenge G2: The next level must incorporate stronger modeling testing, where both the agent and the environment’s characteristics will be represented by state-of-the-art AI software.
The robot’s behavior has to take into account that noisy data and edge cases are things that will be encountered.
Gradually, it has to move on from the more idealized case of Challenge G1 to real-world data that contain faults, have drifts, and are representative of an environment that is much more complex.
This is planned to be an incremental process that will step-wise make the agent capable of dealing with real, on-site situations.
The decision-making process of the robot, while confronted with newer, more complex situations, must also be highlighted through XAI methods.
By that means, human experts can control if the robot is following plausible principles or relies on Clever–Hans correlations [176].
Open Challenge G3: The milestone goal of embodied intelligence for agricultural applications will be for the robots being able to perform the required tasks in real conditions that are far more complex than the ones encountered in the simulations of Challenge G1.
At this level, the robot is well capable of recognizing when it can act autonomously, providing an understandable explanation for its decisions to the human with the help of XAI, learning from human feedback, and also enhancing the human’s expert knowledge—since the robot might discover a new solution to the encountered problems, as in the game of Go [38].
3.3. Augmentation, Explanation, and Verification Technologies Visualization methods and augmented reality (AR) are also becoming more sophisticated thanks to advances in AI.
What is essential, however, is that these technologies are now very widespread and affordable, and are therefore used in a wide variety of application situations as tools for decision support [177].
Domain experts can be provided with contextual and relevant information in an unobtrusive way (AR glasses for forestry technology).
In this context, a new technology trend is very important: situated visualization (SV), which can be seen as the presentation of information in its semantic context [178].
However, the presented data need to be filtered, to not overwhelm the user.
In order to archive the best possible visualization for a user, Julier et al.
(2000) [179] proposed an approach of information filtering whereby the information is prioritized according to the user’s needs.
In addition, the user should be able to interact with the presented data.
The full potential of this interaction can be exploited with the use of AR.
For example, the data could be automatically filtered using the user’s context [180].
Moreover, the AR experience could be enhanced by drawing the user’s context from certain objects the user interacts with in the physical world.
AR technologies are very affordable and widespread, due to the fact that smartphones and tablets can be used as mobile displays.
Head-mounted see-through displays, such as the Microsoft HoloLens and Google Glass, provide direct observation of the physical world while displaying virtual objects.
They are easy to use, lightweight, and even allow the user to operate with both hands.
Google Glass is based on Android, and therefore allows the user to install applications from the Google Play Store [181].
The new Google Glass Enterprise Edition 2 allows the wearer to communicate through video with other people and let them experience the viewpoint of the wearer [182].
Furthermore, AR can be used as a tool for SV, whereby the information is visualized close to the location of the physical object [183].
Another effective way to approach information filtering is to use AI software for real-time anomaly and fault detection [145].
Farmers and foresters are mostly interested in being informed about abnormalities in their everyday working process so that they can intervene as soon as possible.
This can be gradually done with the use of intelligent AI software that uses the knowledge of the domain expert and the available data to define the characteristics of normal operation vs.
faulty case [184,185].
Information fusion is going to be incredibly beneficial, since a faulty state is usually characterized by anomalous behavior on several data sources almost at the same time.
After a period where such a fault detection (FD) system has proven its reliability and correctness, concentrating on prioritizing data leading up to and indicating the fault will enormously help information filtering.
Open Challenge G1: Create the first visualizations for multi-modal data gathered from the sensors.
Concentrate only on the adequate presentation of the data to domain experts and consider some usability aspects, without consideration or software development of data filtering in mind.
Incorporate principles from graphical design and use all the facilities that one can ideally have, such as big monitors, Google Glass, and augmented reality systems (AR).
Open Challenge G2: Work in collaboration with human experts (forester and farmer) and see what are their principal needs, requirements, and expectations from an AI solution.
Define with their help what their priorities are and what characteristics of the data differentiate between normal vs.
abnormal behavior.
Use the results from Challenge G1 to show them static visualizations from particular situations, and let them pinpoint, choose, and enhance those visualizations.
Define with them use-cases that take into account which information is mist important for their decision-making process and how to prioritize and present it so that they are informed precisely, as fast as possible, but without being overwhelmed.
Open Challenge G3: Develop a real-time fault detection AI solution that encompasses all parts of the pipeline: (1) Data gathering, preprocessing, and fusion, (2) adequate visualization as implemented for Challenge G2 but now real-time, and (3) real-time fault detection with the use of efficient and explainable AI solutions.
This pipeline is not static, since neither the human nor the AI software is perfect, nor can either prepare itself for every possible fault and condition that might occur.
The components adapt to new anomalies, user requirements, domain-expert knowledge, and challenges that will arise from the use of more data, more sophisticated XAI methods, and quality management techniques.
Human-Centered AI and the Human in the Loop A human-centered AI approach seeks to promote the robustness of AI algorithms by incorporating a human in the loop, and advocates a synergistic approach to allow humans to control AI and to align AI with human values, ethics, and legal requirements to ensure privacy, security, and safety [12].
4.1. Interactive Machine Learning with the “Human in the Loop” The central challenges of real-world AI applications are in the uncertainty of the data—data can be missing, noisy, dirty, unwanted, etc.—and most of all, many problems in the real world are computationally hard, which makes the application of fully automated approaches difficult or even impossible, or at least the quality of results from automatic approaches might be questionable.
Most of all, the complexity of sophisticated machine learning algorithms has detained non-experts from the application of such solutions.
The integration of the knowledge of a domain expert can sometimes be indispensable, and the interaction of a domain expert with the data would greatly enhance the whole machine learning process pipeline.
A human expert can (sometimes—not always, of course) bring experience, knowledge, and contextual understanding into the machine learning pipeline, which is invaluable to understanding and solving problems from our everyday world.
This is what our best AI algorithms lack to date.
Hence, interactive machine learning (iML) puts the “human in the loop” to enable what neither a human nor a computer could do on their own.
This idea is supported by a synergistic combination of methodologies of two areas that offer ideal conditions towards unraveling such problems, human–computer interaction (HCI) and knowledge discovery/data mining (KDD), with the goal of supporting human intelligence with machine intelligence to discover novel, previously unknown insights into data (HCI-KDD approach [186]).
The human-in-the-loop approach is defined as algorithms that can interact with both computational agents and human agents and can optimize their learning behavior through these interactions.
4.2. Human-Centered Design Human tasks change from time to time, and so do their requirements.
In order to compromise on the vast demand for AI while providing users with the best possible experience, the design of AI technologies and interfaces is crucial.
Holzinger et al.
(2022) [187] showed the continuous changes in users’ profiles and requirements.
The use of AI technologies illustrated that some users might want to try new technologies, whereas others might not.
Several different reasons can influence the users’ trust, and therefore the possible usage of certain systems.
Hence, it is necessary to get to know the potential users and keep their knowledge, experience, and goals in mind when designing systems.
For example, a farmer will most certainly be interested in different data than a machine learning expert.
They might use technology based on the same model, but they pursue different goals, and therefore desire different information or visualizations.
Agile software development methods, particularly agile user centered design methods [188], are increasingly being used in industry, and are ideally suited for our outlined research and development approaches.
However, these methods still lack usability awareness in their development lifecycles, and the integration of extreme usability methods into agile methods is necessary [189], which can help to fulfill the approaches of the “augmented farmer” or the “augmented forester”, which is similar to the “augmented pathologist” [190] or the “augmented radiologist” [191].
4.3. Farmer-in-the-Loop The evaluation of the sustainability of a new technology is becoming of vital importance these days.
A sustainability assessment (LCSA) includes a life cycle assessment (LCA) for estimating environmental impacts [192]; life cycle costing (LCC) for assessing economic issues [193]; and finally, a social life cycle assessment (SLCA) [194].
With this holistic assessment, processes can be evaluated over their entire life-spans (e.g., production of raw materials, manufacturing, use, end-of life treatment, and recycling and disposal of the product).
In addition, based on the results, recommendations regarding support for sustainable development can be provided [195].
In the last few decades, assessments of systems have mostly focused on economic and environmental issues, as methods assessing social sustainability are still under development.
Hence, the following paragraph will focus on environmental and economic issues regarding assessing sustainability of AI, specifically the implementation of sensors.
The use of sensors is a common practice in AI applications and robotics alike.
Precision agriculture relies on sensors to gather the necessary data to respond to the temporal and spatial variability of crop production.
Remote and proximal sensors are the two most common techniques to gather temporal and spatial crop information.
Proximal sensor readings to determine crop input requirements started in the 90s [196].
In 1998, the first normalized difference vegetation index (NDV) sensor reading was used to determine the nitrogen requirements in a Bermuda grass field in Oklahoma [197].
Remote sensing, especially the use of satellites to determine spatial nutrients in soil and plants, started in the early 90s [198].
The use of sensors leads to varying the rates of crop input requirements, having positive environmental and economic impacts on crop production.
Hotspots such as soil acidification, water eutrophication, and global warming potential (GWP) may be reduced.
Profits can be also be achieved by using sensor-based technologies.
Several studies have demonstrated the sustainability of using sensors for variable-rate-input applications in different crops.
(2016) [199], for example, utilized a Crop Circle 210 crop reflectance sensor for variable rate nitrogen application (VRNA) in a corn field in Missouri.
The amount of fertilizer used decreased 11% without affecting grain yield.
The GWP, soil acidification, and freshwater eutrophication were reduced by 7, 10, 22, and 16%, respectively.
In another study, Ehlert et at.
(2004) [200] utilized a mechanical sensor for VRNA in a winter wheat field; the results showed a fertilizer reduction of 10–12% without compromising yield and grain quality.
Some studies ([201,202]) have demonstrated that profits coming from the use of sensors for VRNA range from 10 €/ha to 25 €/ha, depending on the sensor and the size of the farm; more benefits come to farms bigger than 250 ha.
The use of sensors for AI and machine learning applications can bring environmental and economic benefits, as illustrated by precision agriculture technologies.
It will be relevant to have decision support tools such as LCA to assess the sustainability of such technologies in the future but at the same time make use of such technologies to collect the data needed to perform such assessments.
In the long run, AI will most certainly lead to a transformation of entire business practices and industries toward a more sustainable path, by simultaneously fostering and facilitating environmental governance [203].
Despite the strong media interest in the digital transformation in agriculture, implementation in practice in the alpine region is not far advanced yet.
Limiting factors are high investment requirements, a lack of integration into existing agricultural systems, and the lack of training of stakeholders in the sector [204,205].
The technologies available on the market allow precise intervention in agricultural processes, but usually use only single parameters in online transactional processes (OLTP), which are based on simple linear models [206].
However, agriculture is governed by naturally complex processes, which usually need to be represented using a large number of parameters with nonlinear relationships [207].
With the transition from precision agriculture, where only variability on land is considered, to smart farming, which emphasizes the use of complex structured and dynamic information and communication processes in farm management, new technologies, such as computer vision, big data, Internet of Things (IoT), cloud computing, robotics, and artificial intelligence (AI), are entering agriculture.
Based on these technologies, digital transformation requires solutions according to online transactional processes (OLAP), which can make decisions based on a wide range of parameters [206,208,209].
Sensor development and information acquisition provide the essential foundation for this.
Building on this, precision agriculture faces the challenge of requiring ever higher application precision.
Technological developments in automation over the past few decades in agriculture have significantly increased the productivity of agricultural machinery by increasing efficiency, reliability, and precision; and reducing the cost of production and manual, strenuous field labor [173].
Robotics offers the opportunity to further increase both precision and efficiency [210].
Human–machine interaction always faces safety issues in the context of any type of autonomous navigation.
The safety of humans, animals, and objects is a key requirement in the automation of agriculture and forestry.
While for some industrial robots, it is sufficient to delineate the workspace, in the agricultural sector, a higher level of safety is required due to the more direct physical interaction [211].
Computer vision, i.e., imaging sensors and methods for analyzing images, is already being used in various areas of agriculture and food production [212,213].
On the one hand, this concerns applications in environment-dependent/dynamic navigation (including safety aspects), and on the other hand, information retrieval for process control and process evaluation.
Machine or deep learning algorithms are mainly used at first for classification, localization, and detection of different plants in the form of artificial neural networks [214,215].
This requires sufficiently annotated and high-quality training data, which can be immensely costly to produce and has been very limited in (free) availability in the field of precision agriculture [78,216].
Therefore, research is also being conducted on solutions using non-annotated data and semi-supervised learning [217].
In addition, hyperspectral imaging has gained importance in recent years.
However, since cost-effective applications are not yet available, research continues on systems with only one measurement point for plant characterization [218].
All of those systems generate large amounts of data.
In addition, data from sensors are becoming increasingly available in machines and devices in the context of stationary data (IoT), which could provide additional process/system parameters.
Big data technologies, where large amounts of data with great variety are collected and analyzed, provide access to explicit information, and can therefore contribute greatly to decision-making processes through modeling and optimization.
By combining big data with other external data sources, such as weather or market data, the benefits can be significantly increased.
However, gaining knowledge from big data usually requires novel methods and special techniques that are often diverse and complex [219,220].
(2017) showed that information technologies in agricultural engineering are generally still at an early stage of development.
The large amounts of data, however, not meeting i.i.d. requirements, pose a particular challenge [221].
It is expected that through access to real-time data and real-time forecasts, and through combination with IoT developments and especially AI, technologization will advance.
While this prospect is promising, challenges such as data quality, privacy, and security issues cannot be neglected, arguing for a synergistic approach of human-centered AI to reconcile new technologies in agricultural technology with human values, ethics, and legal requirements to ensure privacy, security, and safety.
Future developments will increasingly provide data and information along the entire value chain in real time (challenge to the capacity of telecommunications-6G [222]) and with location accuracy (challenge to the precision of telemetry, [223]).
In the context of sensor developments (increases in diversity, sensitivity, robustness, and precision, while decreasing prices), a basis will be created that allows agricultural processes to be recorded in a more differentiated way based on data.
By using the experiential knowledge of humans via human–machine–human communication (human-in-the-loop, AI-in-the-loop), technical processes can be much more finely adapted to natural processes, which will contribute to increasing the resource efficiency of production processes (“feed the world”), and to improving the quality of products, both internally (human health) and externally (e.g., life cycle impact, animal welfare, environmental protection, and climate protection).
In this context, networking all stakeholders through appropriate technology can increase the transparency of food production, improve documentation, and ultimately improve traceability—these are general goals of human-centered AI, and here we are again speaking of explainability.
To achieve these benefits, AI tools that are appropriate, and above all, developed in a human-centered way (see Section 4.2), will play a crucial role in linking technologies and using domain knowledge, for natural agricultural systems, increasing their global and local diversity, and helping their sustainable management.
Therefore, data-driven AI applications can help to overcome the sectoral fragmentation of IT applications in agriculture and create links between agriculture, food processing, and consumers on the one hand, and the industry supplying agriculture on the other (e.g., predictive maintenance of machinery).
Open Challenge G1: Identify a requirements map and technology overview.
Create a toolbox of existing technologies for inexperienced farmers with easy-to-use methods and cost-effective applications to create benefits in everyday life according to the concept of human-centered design (see Section 4.2).
Open Challenge G2: Making online available data accessible and integrate the structure and computational operations of the above toolset into AI solutions.
Networking, fusion, integration, presentation, and visualization of information from different sources and locations, following the information visualization mantra “overview first, zoom and filter, then details on demand” [224] to provide a respective snapshot across the entire value chain, thereby identifying insight and opportunities for further analysis of key indicators across the entire value chain (“from seed to the consumer’s stomach”).
Open Challenge G3: A key challenge is to gradually refine the tools of LCA, LCC, and SLCA.
4.4. Forester-in-the-Loop Forest education in Austria is based on the general Austrian education system and includes various forestry professions.
The theoretical and practical education, imparted through school, university, an apprenticeship, or specialized courses, ensures the competence of the forestry personnel of tomorrow and forms the foundation of Austrian forestry.
After a three-year apprenticeship, secondary courses, or an exam following agricultural and forestry colleges, forest workers are optimally trained for motor-manual forest activities in reforestation, cultivation, maintenance, and harvesting.
Since 2016, it has been possible to learn the profession of forestry technician, where the main focus is on the handling of equipment and machinery for timber harvesting.
This solid education in combination with the theoretically and practically acquired expertise is very well suited to be integrated into forestry AI processes.
In this way, the expertise and practical experience of the forester/forestry worker/operator acquired in school can contribute to the training of AI systems, and conversely, the human can be supported and relieved of their decisions and activities.
In steep terrain, especially in Austrian forests, timber harvesting will always be a challenge in terms of economic viability, safety, and environmental performance.
The state-of-the-art harvesting method in steep terrain is motor-manual felling in combination with logging via cable yarders.
Even though new technologies and innovations are modernizing timber harvesting in steep terrain, there will always be operations where forest workers need to enter the forest due to the difficult topological conditions.
In these cases, it is the task of human-centered AI to intelligently integrate workers on the site into already autonomous or semi-autonomous timber harvesting operations.
For example, potentially autonomous cable yarders must interact appropriately with workers on the site, and both parties must be considerate of and learn from each other.
All forestry machines, whether harvesters, forwarders, cable yarders, or simply chainsaws, and whether autonomous, automated, remote, or traditionally controlled by a human in the cab, have certain maintenance and repair needs.
Some repairs also occur randomly and suddenly, such as chain breakage on a harvester head or replacement of a hydraulic hose.
These repairs are then usually carried out by the operator on site.
In future AI-supported autonomous or automatic processes, humans must also be involved in this topic with their expertise in all aspects of the repair.
Real-time anomaly and fault detection (see Section 3.1) is faster, more reliable, and needs less visualization capabilities [145].
This is going to be of great benefit to the user, since this will tackle efficiently the problem of filtering out information (see Section 3.3), while at the same time detecting the faults efficiently and needing the domain expert only for the definition of normal vs.
abnormal behavior and potential repair on-site.
Information about AI in forest operations can also be found on websites and in popular science journals.
However, science has basically been dealing with developments of robotics in forestry since the 1980s (as in [225]).
Over the years and with increasing sensor technology and computer power, a number of forest operations research groups are experimenting with digitization in forest operation.
Visser and Obi (2021) [88] stated that there is often much speculation on future benefits, and there is almost a complete absence of information on actual productivity improvements of any of the prototypes developed.
For forestry practice, it can be stated that there is a lot of R&D in the field, but the developments have not actually found their way into the real forest yet.
The next steps to successfully establish new technologies and AI in timber harvesting are to use existing technologies, which are already well equipped with sensors and computing power, to link them with AI and to integrate the forest worker as an integral control, steering, and assistance organ.
Open Challenge G1: Due to the small-scale forestry in Austria, many forest owners work in their own forests.
Therefore, most of the work is done manually with a chainsaw.
The future task of the forester-in-the-loop approach is to develop digital and smart tools in this area as well.
For example, individual tree information could be shown to the forest owners via heads-up displays in their helmets or VR glasses.
Furthermore, it would also be conceivable to provide assistance with regard to value-optimized bucking in order to increase efficiency and revenue.
Conversely, the AI can always learn from the forestry worker’s expertise and concrete actions during the work process.
Open Challenge G2: In principle, a good first step into autonomous practice would be to decouple the acquisition of the environment data of a forest machine and its AI-controlled features in terms of time.
For example, digital twins of the forest can be created with 3D scanners (often takes place as part of forest inventory anyway); and autonomous, automated, or even augmented processes can be integrated into the forest machine on the basis of these.
This saves time-consuming on-the-fly environment mapping and navigation.
Robots (e.g., [226]) offer a good opportunity to test such a process.
During the entire process, the forester should be specifically involved and make decisions.
Open Challenge G3: Based on Open Challenge G2, a direct navigation system for forestry machines should be developed, enabling on-the-fly navigation.
This concerns not only the pure driving with the machine but also the autonomous control of attachments and aggregates (e.g., crane and harvester head).
This not only applies to simply driving the machine, but also to the autonomous control of attachments and aggregates (crane, harvester head, etc.).
In this further development step, it is also necessary to integrate further sensors and to process their data intelligently (GNSS sensor, 3D laser scanners, 2D laser scanners, stereo cameras, hydraulic sensors).
Furthermore, the methods and approaches should also be transferred from the small robot to a real forest machine.
The expertise of the previous operators should be incorporated in order to avoid environmental impacts and to work in a value-optimized manner.
This step towards a large forestry will be done in close cooperation with machine manufacturers.
Furthermore, large-scale practical studies will be carried out in the forest in order to test and continuously develop the systems.
Conclusions Advanced technologies—from sensors to sophisticated augmented reality visualization methods—are nowadays already so inexpensive that they are very widely used.
As a result, they are already being used as decision support tools in a wide range of application situations.
The hardware is available; what needs to be worked on now is bringing intelligence into the hardware.
This is where human-centered AI comes in—namely, not only providing the domain experts with contextual and relevant information, but also involving them directly in the decision-making process.
A human expert often has a lot of experiential knowledge, and it can be useful to combine this natural intelligence with artificial intelligence.
In our paper, we first justified why agriculture and forestry are among the most important application areas for all humankind.
Then, we facilitated a common understanding by providing definitions of artificial intelligence and human-centered AI, and introduced the three main approaches to machine learning (supervised, unsupervised, reinforcement).
This should help the non-expert reader to get started with this important and forward-looking topic.
We then presented the current state-of-the-art in autonomous, automated, assisted, and augmented AI systems.
The special feature here is that we gave one example from agricultural technology and one example from forestry technology, thereby helping to understand the connection between these two areas.
In this paper, we described three pioneer research areas that we identified as the most important and promising research areas for the next 7 years based on our experience: (1) intelligent sensor information fusion, (2) robotics and embodied intelligence, and (3) augmentation, explanation, and verification.
Finally, we summarized again the core ideas of human-centered AI and gave two examples of farmer-in-the-loop and forester-in-the-Loop.
We are convinced that the next 7 years will be internationally dominated by these topics, and that with their help, practical progress can be made in the entire process chains of future agriculture and forestry.
""".strip()

documents = [line for line in RAW_DOCS.split("\n") if line.strip()]


# start chromadb
client = chromadb.PersistentClient(path="./eco_advisor_db/")
collection = client.get_or_create_collection(name="eco_docs")

# embed and add collections if empty
if collection.count() == 0:
    st.info(f"Indexing {len(documents)} documents…")
    progress = st.progress(0)
    for i, doc in enumerate(documents):
        emb = ollama.embed(model="nomic-embed-text", input=doc)["embeddings"]
        collection.add(
            ids=[str(i)],
            embeddings=emb,
            documents=[doc]
        )
        progress.progress(int((i + 1) / len(documents) * 100))
    st.success("Document indexing complete!")

# retrieval helper
def get_relevant_context(prompt: str) -> str:
    emb = ollama.embed(model="nomic-embed-text", input=prompt)["embeddings"]
    res = collection.query(query_embeddings=emb, n_results=1)
    docs = res.get("documents", [])
    return docs[0][0] if docs else ""

# user interface
st.set_page_config(page_title="Eco Advisor AI", layout="wide")
st.title("🌱 Eco Advisor AI")

st.write("""
Ask any question about ecology, sustainability or green technology—  
I'll find the most relevant snippet from your documents and answer as an expert.
""")

user_q = st.text_area("Your question:", height=150)

if st.button("Ask Eco Advisor"):
    if not user_q.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Retrieving relevant context…"):
            ctx = get_relevant_context(user_q)
        if ctx:
            st.subheader("🔍 Retrieved Context")
            st.write(ctx)

            with st.spinner("Generating answer…"):
                reply = ollama.generate(
                    model="llama2",
                    prompt=(
                        f"Background:\n{ctx}\n\n"
                        f"Question:\n{user_q}\n\n"
                        "Answer as an expert eco‐advisor:"
                    )
                ).get("response", "")
            st.subheader("💡 Eco Advisor’s Answer")
            st.write(reply or "No answer generated.")
        else:
            st.error("No relevant context found.")
