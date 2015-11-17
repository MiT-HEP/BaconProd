from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'data7'
config.General.workArea =  '2015Dv4'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'makingBaconPuppiMVAMets_MC.py'
#config.JobType.psetName = 'makingGenBacon.py'
config.JobType.psetName = 'makingBaconPuppiMVAMets_DATA.py'
config.JobType.outputFiles = ['Output.root']
config.section_("Data")
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/AODSIM'
#config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v2/AODSIM'
#config.Data.inputDataset = '/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDataset = '/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDataset = '/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/AODSIM'
#config.Data.inputDataset = '/WWTo2L2Nu_13TeV-powheg/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDataset = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM'
#config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v3/AOD'
config.Data.inputDataset = '/SingleMuon/Run2015D-PromptReco-v4/AOD'
#config.Data.inputDataset = '/SingleElectron/Run2015D-PromptReco-v3/AOD'
#config.Data.inputDataset = '/SingleElectron/Run2015D-PromptReco-v4/AOD'
#config.Data.inputDataset = '/SingleMuon/Run2015C-PromptReco-v1/AOD'
#config.Data.inputDataset = '/SingleMuon/Run2015C-PromptReco-v1/AOD'
config.JobType.inputFiles  = ['Summer15_25nsV6_DATA.db']
#config.JobType.inputFiles  = ['Summer15_25nsV6_MC.db']
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5 
config.Data.outLFNDirBase = '/store/user/arapyan/Run2' # or '/store/group/<subdir>'
config.Data.publication = False
config.Data.outputDatasetTag = 'Samples'
#config.Data.publishDataName = 'Samples'

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'
