## Data Format

The HDF5 files contain two datasets named `jets` and `tracks`:
```bash
$ h5ls test.h5
jets                     Dataset {44420/Inf}
tracks                   Dataset {44420/Inf, 60}
```
where 44420, in this case, is the number of jets in this sample, and 60 is the maximum number of tracks in each jet.

To open one of these files in python:
```python
import h5py
d = h5py.File('test.h5', 'r')
```
You can now use your python skills to investigate the structure of these data archives.

To extract each dataset in the form of `numpy.ndarray`, use, for example, `d['jets'][:]`.
This structured array will have 44420 rows, each corresponding to one jet. When asked for the shape, this returns (44420, ) instead of (44420, vars) :(

If you try accessing the first jet using `d['jets'][0]` you will notice that it'll return an object of type `numpy.void`, which you can then wrap in a `numpy.array` using `np.array(d['jets'][0])`.

The `jets` dataset contains variables that directly describe the individual jets. You can find their name and order using `d['jets'][:].dtype.names`:
```python
('pt',                 # transverse momentum
 'eta',                # pseudorapidity
 'ip3d_ntrk',          # number of tracks in the jet that pass the ip3d selection
 'ip2d_pu',            # probability(light) output from ip2d
 'ip2d_pc',            # probability(charm) output from ip2d
 'ip2d_pb',            # probability(bottom) output from ip2d
 'ip3d_pu',            # probability(light) output from ip3d
 'ip3d_pc',            # probability(charm) output from ip3d
 'ip3d_pb',            # probability(bottom) output from ip3d
 'rnnip_pu',           # probability(light) output from rnnip
 'rnnip_pc',           # probability(charm) output from rnnip
 'rnnip_pb',           # probability(bottom) output from rnnip
 'rnnip_ptau',         # probability(tau) output from rnnip
 'mu_dR',              #
 'mu_mombalsignif',    #
 'mu_d0',              #
 'mu_pTrel',           #
 'mu_qOverPratio',     #
 'mu_scatneighsignif', #
 'mv2c10',             # mv2c10 tagger output
 'jf_dr',              #
 'jf_efc',             #
 'jf_m',               #
 'jf_n2t',             #
 'jf_ntrkAtVx',        #
 'jf_nvtx',            #
 'jf_nvtx1t',          #   
 'jf_sig3d',           #
 'jf_deta',            #
 'jf_dphi',            #
 'sv1_dR',             #
 'sv1_efc',            #
 'sv1_Lxyz',           #
 'sv1_Lxy',            #
 'sv1_m',              #
 'sv1_n2t',            #
 'sv1_ntrkv',          #
 'sv1_normdist',       #
 'truthflav',          # true particle flavor
 'LabDr_HadF')         # true particle flavor (same as above or thru different method?)
```
To select the first 10 jets, for example, you can just slice the array as such: `d['jets'][:10]`.

The `tracks` dataset has shape (44420, 60) [ideally this should be (44420, vars, 60)] :(

The variables used to describe each track in a jet are:
```python
('pt',                                     # transverse momentum
 'deta',                                   # delta eta between the track and the jet
 'dphi',                                   # delta phi between the track and the jet
 'charge',                                 # track charge {-1, +1}
 'dr',                                     # radial distance between the track and the jet
 'ptfrac',                                 # ratio of track to jet transverse momentum
 'grade',                                  # track quality category
 'd0',  
 'z0',
 'd0sig',
 'z0sig',
 'd0_ls',
 'z0_ls',
 'd0sig_ls',
 'z0sig_ls',
 'chi2',
 'ndf',
 'numberOfInnermostPixelLayerHits',
 'numberOfNextToInnermostPixelLayerHits',
 'numberOfBLayerHits',
 'numberOfBLayerSharedHits',
 'numberOfBLayerSplitHits',
 'numberOfPixelHits',
 'numberOfPixelHoles',
 'numberOfPixelSharedHits',
 'numberOfPixelSplitHits',
 'numberOfSCTHits',
 'numberOfSCTHoles',
 'numberOfSCTSharedHits',
 'expectBLayerHit',
 'expectInnermostPixelLayerHit',
 'expectNextToInnermostPixelLayerHit',
 'mask')
```
