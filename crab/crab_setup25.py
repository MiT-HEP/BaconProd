from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'data7'
config.General.workArea =  'zeepowheg2'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'makingBaconPuppiMVAMets_MC.py'
#config.JobType.psetName = 'makingGenBacon.py'
#config.JobType.psetName = 'makingBaconPuppiMVAMets_DATA.py'
config.JobType.outputFiles = ['Output.root']
config.section_("Data")
#config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/AODSIM'
#config.Data.inputDataset = '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/AODSIM'
#config.Data.inputDataset = '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/SingleMuon/Run2015D-16Dec2015-v1/AOD'
#config.Data.inputDataset = '/SingleMuon/Run2015C_25ns-16Dec2015-v1/AOD'
#config.Data.inputDataset = '/SingleElectron/Run2015D-16Dec2015-v1/AOD'
#config.Data.inputDataset = '/SingleElectron/Run2015C_25ns-16Dec2015-v1/AOD'
#config.Data.inputDataset  = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/ZToMuMu_NNPDF30_13TeV-powheg_M_50_120/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/ZToMuMu_NNPDF30_13TeV-powheg_M_120_200/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/SingleMuon/Run2015B-PromptReco-v1/AOD'
#onfig.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_Zpt-150toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'

#config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsPoisson50_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsPoisson50_76X_mcRun2_asymptotic_v12_ext1-v1/AODSIM'
#config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76Premix-premixPU50_nondeterministic_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76Premix-premixPU50_nondeterministic_76X_mcRun2_asymptotic_v12_ext1-v1/AODSIM'
#config.Data.inputDataset = '/TTJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76-PU25nsPoisson50_76X_mcRun2_asymptotic_v12-v1/AODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15DR76Premix-premixPU50_deterministic_76X_mcRun2_asymptotic_v12_ext1-v2/AODSIM'
#config.Data.inputDataset = '/ZToEE_NNPDF30_13TeV-powheg_M_50_120/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'
config.Data.inputDataset = '/ZToEE_NNPDF30_13TeV-powheg_M_120_200/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/AODSIM'


#config.JobType.inputFiles  = ['Summer15_25nsV6_DATA.db']
config.JobType.inputFiles  = ['Summer15_25nsV6_MC.db']
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 7
config.Data.outLFNDirBase = '/store/user/arapyan/Run2' # or '/store/group/<subdir>'
config.Data.publication = False
config.Data.outputDatasetTag = 'Samples'
#config.Data.publishDataName = 'Samples'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
