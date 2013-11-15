import matplotlib as mpl
gpBlue='#00aeef'
gpLightGray='#96999b'
gpDarkBlue='#00447c'
gpRed='#cf5c42'
gpBrown='#e1d8ad'
gpPink='#f4d5e3'
gpLightBlue='#e1f4fd'

def setStyle():
  mpl.rcParams['axes.edgecolor'] = gpLightGray
  mpl.rcParams['axes.linewidth'] = 0
  mpl.rcParams['lines.linewidth'] = 2
  mpl.rcParams['lines.color'] = gpBlue
  mpl.rcParams['text.color'] = gpLightGray
  mpl.rcParams['axes.labelcolor'] = '#96999b'
  mpl.rcParams['axes.titlesize'] = 14
  mpl.rcParams['axes.labelsize'] = 12
  mpl.rcParams['legend.fontsize'] = 10
  mpl.rcParams['xtick.color'] = '#96999b'
  mpl.rcParams['xtick.major.size'] = 0
  mpl.rcParams['xtick.labelsize'] = 10
  mpl.rcParams['ytick.color'] = '#96999b'
  mpl.rcParams['ytick.major.size'] = 0
  mpl.rcParams['ytick.labelsize'] = 10
  mpl.rcParams['axes.grid'] = True
  mpl.rcParams['legend.fancybox'] = True
  mpl.rcParams['legend.frameon'] = False
  mpl.rcParams['grid.color'] = '#cccccc'
  mpl.rcParams['lines.solid_joinstyle'] = 'round'

  print 'SETTING GP STYLE'
