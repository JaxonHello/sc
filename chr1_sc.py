import time
from sc_spectrum.scml import sparse_spectral
from sc_spectrum.scml import spectral_clustering
import numpy as np
from scipy.sparse import csr_matrix

time_start = time.time()

n_clust = 265


hic_KR = np.loadtxt("chr1_KR.csv")
KR = csr_matrix(hic_KR)
L, w, v = sparse_spectral(KR, n_clust=n_clust + 30)
label = spectral_clustering(v, n_clust=n_clust)


time_end = time.time()
print("程序运行时间：", time_end-time_start//60, "min")
np.savetxt('chr1_sc_KR.csv', label)
