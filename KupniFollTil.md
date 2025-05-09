<h1>Samantekt á föllum fyrir kúpnifræði</h1>

Samantekt á föllum sem eru til í Python fyrir kúpnifræði.

<h2>SciPy.spatial-pakkinn</h2>

https://docs.scipy.org/doc/scipy/reference/spatial.html#

<h3>ConvexHull</h3>

ConvexHull er klasi sem hægt er að nota til að finna kúpta hjúpinn fyrir mengi af punktum sem eru í *N* víddum. Klasinn vinnur með hnit punktanna sem á að búa til kúptan hjúp um. Hnitin eru geymd í gagnategundinni ndarray af float en ndarray er gagnategund í NumPy pakkanum. Kúpti hjúpurinn er reiknaður með því að nota safnið (e. library) <a href="http://www.qhull.org">Qhull</a>. Það eru auk þess tveir valkvæðir stikar, annars vegar `incremental` sem er af taginu bool og leyfir punktum að vera bætt við í áföngum og hins vegar `qhull_options` sem er hægt að nota til að bæta við fleiri stillingum.

ConvexHull hlutir hafa nokkra eiginleika eins og `points` sem geymir hnitin á punktunum sem finna á kúptan hjúp um og `vertices` sem er ndarray af int og inniheldur vísana á punktunum í `points` sem mynda kúpta hjúpinn. Ef vigrarnir eru í tveimur víddum eru vísar punktanna í rangsælis röð en annars í þeirri röð sem þeir voru settir inn upprunalega.

SciPy.spatial-pakkinn hefur auk þess fallið convex_hull_plot_2d sem tekur inn hlut af klasanum ConvexHull sem hefur tvívíða punkta og teiknar 2-D mynd en þetta fall notar Matplotlib.

<h3>Annað</h3>

Eftirfarandi klasar tengjast einnig kúpnifræði:

- Delaunay
- Voronoi
- SphericalVoronoi
- HalfspaceIntersection

Delaunay, Voronoi og SphericalVoronoi nota ndarray af float til að tákna punktana sem unnið er með og þeir geta verið í *N* víddum. HalfspaceIntersection tekur inn hálfrúm (e. halfspaces) sem ndarray af floats og innri punkta (e. interior points) sem ndarray af floats.

<h2>SymPy-pakkinn</h2>

https://docs.sympy.org/latest/modules/geometry/utils.html

<h3>convex_hull</h3>
  
convex_hull er fall sem hægt er að nota til að finna kúpta hjúpinn fyrir hluti í tveimur víddum. Fallið tekur inn safn af Points, Segments og/eða Polygons en þessar gagnategundir eru klasar í SymPy. Báðar gagnategundirnar, Segments og Polygons, taka inn Points og getur Segments almennt verið í *N* víddum en Polygons bara í tveimur víddum.

Setja má inn aukastika í fallið convex_hull, `polygon`, sem hefur tagið bool til að tilgreina hvort punktarnir myndi Polygon. Ef `polygon` er True skilar fallið kúpta hjúpnum sem hlut af klasanum Polygon. Annars verður skilagildið samstæða (e. tuple) sem inniheldur efri kúpta hjúpinn (e. upper hull) og neðri hjúpinn (e. lower hull). Ef ekkert er sett inn fyrir stikann `polygon` er hann hafður sem True.

<h2>pycvxset-pakkinn</h2>

https://github.com/merlresearch/pycvxset
<br> https://arxiv.org/pdf/2410.11430

Hægt er að nota pycvxset-pakkann til að vinna með kúpt mengi, teikna þau og framkvæma aðgerðir á þau. Það eru þrír klasar sem er hægt að nota til að tákna kúpt mengi í pakkanum og heita þeir Polytope, ConstrainedZonotope og Ellipsoid.

Polytope og ConstrainedZonotope hafa hvor um sig margar mögulegar samsetningar af stikum sem hægt er að setja inn til að fá hlut. Flestir stikanna eru array_like í NumPy og því er hægt að nota gagnategundina ndarray sem er líka í NumPy.

Ellipsoid tekur inn miðjuna á sporvölunni sem er á formi vigurs með vídd *N*. Ellipsoid tekur einnig inn *N*$\times$*N* ferningsfylki og gagnategund fylkisins er fylki í NumPy eins og diag.

<h2>cvxpy</h2>

https://github.com/cvxpy/cvxpy/

Hægt er að nota cvxpy til að leysa verkefni tengdum kúptri bestun (e. convex optimization) en cvxpy er líkanamál tengt Python. Verkefnin eru sett fram þannig að kóðinn líkist meira stærðfræðilegu táknmáli.