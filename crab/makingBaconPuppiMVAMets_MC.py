import FWCore.ParameterSet.Config as cms

process = cms.Process('MakingBacon')

# import of standard configurations
process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/GeometryDB_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
#process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration/EventContent/EventContent_cff')
process.load('TrackingTools/TransientTrack/TransientTrackBuilder_cfi')

process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'

#process.load("RecoTauTag/Configuration/RecoPFTauTag_cff")

# import custom configurations
#process.load('BaconProd/Ntupler/myJetExtras04_cff')    # include gen jets and b-tagging

process.load('BaconProd/Ntupler/myMETFilters_cff')        # apply MET filters set to tagging mode
#process.load('RecoMET.METPUSubtraction.mvaPFMET30_cff')     # MVA MET from Stephanie
process.load("BaconProd/Ntupler/myPFMETCorrections_cff")  # PF MET corrections
#process.pfJetMETcorr.jetCorrLabel = cms.string("ak5PFL1FastL2L3")

# trigger filter
import os
cmssw_base = os.environ['CMSSW_BASE']
hlt_filename = "BaconAna/DataFormats/data/HLT_50nsGRun"
process.load('HLTrigger/HLTfilters/hltHighLevel_cfi')
process.hltHighLevel.throw = cms.bool(False)
process.hltHighLevel.HLTPaths = cms.vstring()

#process.pfMVAMEt.isTestSample = cms.bool(False)
from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
from RecoMET.METProducers.PFMET_cfi import pfMet

process.load("CondCore.DBCommon.CondDBCommon_cfi")
from CondCore.DBCommon.CondDBSetup_cfi import *
## load Puppi stuff
#PUPPI JEC
process.load('CommonTools/PileupAlgos/Puppi_cff') 
process.load('BaconProd/Ntupler/myPUPPICorrections_cff')
process.pfCandNoLep = cms.EDFilter("CandPtrSelector", src = cms.InputTag("particleFlow"), cut = cms.string("abs(pdgId) != 13 && abs(pdgId) != 11 && abs(pdgId) != 15"))
process.pfCandLep = cms.EDFilter("CandPtrSelector", src = cms.InputTag("particleFlow"), cut = cms.string("abs(pdgId) == 13 || abs(pdgId) == 11 || abs(pdgId) == 15"))
process.puppinolep = process.puppi.clone()
process.puppinolep.candName = 'pfCandNoLep'
process.puppimetinput = cms.EDProducer("CandViewMerger",
                                       src = cms.VInputTag( "pfCandLep","puppinolep")
                                       )

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_PHYS14_PU20bx25_V2_cff']
switchOnVIDPhotonIdProducer(process, DataFormat.AOD)
for idmod in my_id_modules:
  setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)

process.load('CommonTools/PileupAlgos/PhotonPuppi_cff')
process.puppiPhoton.puppiCandName = 'puppimetinput'
process.puppiPhoton.candName = 'particleFlow'
process.puppiPhoton.photonName = 'gedPhotons'

# Include the stuff for Puppi MET
process.pfMetPuppi = pfMet.clone();
process.pfMetPuppi.src = cms.InputTag('puppiPhoton')
process.pfMetPuppi.calculateSignificance = False

process.ak4PFJetsPuppi   = ak4PFJets.clone(src = cms.InputTag("puppinolep"))

hlt_file = open(cmssw_base + "/src/" + hlt_filename, "r")
for line in hlt_file.readlines():
  line = line.strip()              # strip preceding and trailing whitespaces
  if (line[0:3] == 'HLT'):         # assumes typical lines begin with HLT path name (e.g. HLT_Mu15_v1)
    hlt_path = line.split()[0]
    process.hltHighLevel.HLTPaths.extend(cms.untracked.vstring(hlt_path))

    process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
    process.source = cms.Source("PoolSource",
                                  fileNames = cms.untracked.vstring('/store/mc/RunIIFall15DR76/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/00000/004FE350-19BD-E511-9F01-00238BBD7672.root'
                                  #fileNames = cms.untracked.vstring('/store/user/arapyan/mc/VBFHpmToWlnuZll_M800_13TeV-madgraph-pythia8/RunIIFall15DR76-PU25nsData2015v1_76X_mcRun2_asymptotic_v12/AODSIM/AOD_96001.root'
                                  )
                                )
    process.source.inputCommands = cms.untracked.vstring("keep *",
                                                         "drop *_MEtoEDMConverter_*_*")
    
process.options = cms.untracked.PSet(
  wantSummary = cms.untracked.bool(False),
  Rethrow     = cms.untracked.vstring('ProductNotFound'),
  fileMode    = cms.untracked.string('NOMERGE')
  )

is_data_flag = False 
do_hlt_filter = False
process.ntupler = cms.EDAnalyzer('NtuplerMod',
                                 skipOnHLTFail = cms.untracked.bool(do_hlt_filter),
                                 outputName    = cms.untracked.string('Output.root'),
                                 TriggerFile   = cms.untracked.string(hlt_filename),
                                 edmPVName     = cms.untracked.string('offlinePrimaryVertices'),
                                 edmPFCandName = cms.untracked.string('particleFlow'),
                                     
                                 Info = cms.untracked.PSet(
    isActive             = cms.untracked.bool(True),
    edmPFCandName        = cms.untracked.string('particleFlow'),
    edmPileupInfoName    = cms.untracked.string('addPileupInfo'),
    edmBeamspotName      = cms.untracked.string('offlineBeamSpot'),
    edmPFMETName         = cms.untracked.string('pfMet'),
    #edmPFMETCorrName     = cms.untracked.string('pfType1CorrectedMet'),
    edmPFMETCorrName     = cms.untracked.string('pfMetT1'),
    edmMVAMETName        = cms.untracked.string('pfMVAMEt30'),
    edmPuppETName        = cms.untracked.string('pfType1PuppiCorrectedMet'),
    edmTrackMET          = cms.untracked.string('pfChMet'),
    edmRhoForIsoName     = cms.untracked.string('fixedGridRhoFastjetAll'),
    edmRhoForJetEnergy   = cms.untracked.string('fixedGridRhoFastjetAll'),
    doFillMETFilters     = cms.untracked.bool(False),
    doFillMET            = cms.untracked.bool(True)
    ),
                                 
                                 GenInfo = cms.untracked.PSet(
    isActive            = ( cms.untracked.bool(False) if is_data_flag else cms.untracked.bool(True) ),
    #isActive            = cms.untracked.bool(False),
    edmGenEventInfoName = cms.untracked.string('generator'),
    edmGenParticlesName = cms.untracked.string('genParticles'),
    fillAllGen          = cms.untracked.bool(False)
    ),
                                 
                                 PV = cms.untracked.PSet(
    isActive      = cms.untracked.bool(True),   
    edmName       = cms.untracked.string('offlinePrimaryVertices'),
    minNTracksFit = cms.untracked.uint32(0),
    minNdof       = cms.untracked.double(4),
    maxAbsZ       = cms.untracked.double(24),
    maxRho        = cms.untracked.double(2)
    ),
                                 
                                     Electron = cms.untracked.PSet(
    isActive                  = cms.untracked.bool(True),
    minPt                     = cms.untracked.double(15),
    edmName                   = cms.untracked.string('gedGsfElectrons'),
    edmPFCandName             = cms.untracked.string('particleFlow'),
    edmTrackName              = cms.untracked.string('generalTracks'),
    edmBeamspotName           = cms.untracked.string('offlineBeamSpot'),
    edmConversionName         = cms.untracked.string('allConversions'),
    edmSuperClusterName       = cms.untracked.string('particleFlowEGamma')
    ),
                                 
                                 Muon = cms.untracked.PSet(
    isActive      = cms.untracked.bool(True),
    minPt         = cms.untracked.double(15),
    edmName       = cms.untracked.string('muons'),
    edmPFCandName = cms.untracked.string('particleFlow'),
    
    # save general tracker tracks in our muon collection (used in tag-and-probe for muons)
    doSaveTracks = cms.untracked.bool(True),
    minTrackPt   = cms.untracked.double(15),
    edmTrackName = cms.untracked.string('generalTracks')    
    ),
                                     
                                 Photon = cms.untracked.PSet(
    isActive               = cms.untracked.bool(True),
    minPt                  = cms.untracked.double(15),
    edmName                = cms.untracked.string('gedPhotons'),
    edmPFCandName          = cms.untracked.string('particleFlow'),
    edmElectronName        = cms.untracked.string('gedGsfElectrons'),
    edmConversionName      = cms.untracked.string('allConversions'),
    edmSuperClusterName    = cms.untracked.string('particleFlowEGamma'),
    #    edmEBRecHitName       = cms.untracked.string('reducedEcalRecHitsEB'),
    #    edmEERecHitName       = cms.untracked.string('reducedEcalRecHitsEE'),
    #    edmRhoForEnergyRegression = cms.untracked.string('kt6PFJets'),
    #    edmPVName                 = cms.untracked.string('offlinePrimaryVertices')
    ),
                                 
                                 #  Tau = cms.untracked.PSet(
                                 #    isActive = cms.untracked.bool(True),
                                 #    minPt    = cms.untracked.double(15),
                                 #    edmName  = cms.untracked.string('hpsPFTauProducer'),
                                 #    ringIsoFile      = cms.untracked.string('BaconProd/Utils/data/gbrfTauIso_apr29a.root'),
                                 #    ringIso2File     = cms.untracked.string('BaconProd/Utils/data/gbrfTauIso_v2.root'),
                                 #    edmRhoForRingIso = cms.untracked.string('kt6PFJets')
                                 #  ),
                                 Jet = cms.untracked.PSet(
        isActive             = cms.untracked.bool(True),
        minPt                = cms.untracked.double(27),
        #    doComputeFullJetInfo = cms.untracked.bool(True),
        #    doGenJet             = ( cms.untracked.bool(False) if is_data_flag else cms.untracked.bool(True) ),
        #    
        #coneSizes = cms.untracked.vdouble(0.4),#,0.8,1.2),
        postFix   = cms.untracked.vstring("CHS"),
        #    
        edmPVName = cms.untracked.string('offlinePrimaryVertices'),
        ##    
        ## ORDERED lists of jet energy correction input files
        jecFiles = ( cms.untracked.vstring('dummy.txt',
                                           'dummy.txt',
                                           'dummy.txt',
                                           'dummy.txt')
                     if is_data_flag else 
                     cms.untracked.vstring('BaconProd/Utils/data/Summer15_25nsV6_MC_L1FastJet_AK4PFchs.txt',
                                           'BaconProd/Utils/data/Summer15_25nsV6_MC_L2Relative_AK4PFchs.txt',
                                           'BaconProd/Utils/data/Summer15_25nsV6_MC_L3Absolute_AK4PFchs.txt')
                     ),
        jecUncFiles = ( cms.untracked.vstring('dummy.txt')
                        if is_data_flag else
                        cms.untracked.vstring('dummy.txt')
                        ),
        edmRhoName = cms.untracked.string('fixedGridRhoFastjetAll'),
        #    
        #    # ORDERD list of pileup jet ID input files
        #    jetPUIDFiles = cms.untracked.vstring('',
        #                                         'BaconProd/Utils/data/TMVAClassificationCategory_JetID_53X_Dec2012.weights.xml'),
        #    
        # names of various jet-related collections
        jetName            = cms.untracked.string('ak4PFJetsCHS'),
        #    genJetName         = cms.untracked.string('GenJets'),
        #    jetFlavorName      = cms.untracked.string('byValAlgo'),
        #    jetFlavorPhysName  = cms.untracked.string('byValPhys'),
        #    pruneJetName       = cms.untracked.string('caPFJetsPruned'),
        #    subJetName         = cms.untracked.string('caPFJetsPruned'),
        csvBTagName        = cms.untracked.string('combinedInclusiveSecondaryVertexV2BJetTags')#,
        #    csvBTagSubJetName  = cms.untracked.string('jetCombinedSecondaryVertexBJetTagsSJ'),
        #    jettiness          = cms.untracked.string('Njettiness'),
        #    qgLikelihood       = cms.untracked.string('QGTagger'),
        #    qgLikelihoodSubjet = cms.untracked.string('QGTaggerSubJets')
        ),
                                 
                                 PFCand = cms.untracked.PSet(
        isActive       = cms.untracked.bool(False),
        edmName        = cms.untracked.string('particleFlow'),
        edmPVName      = cms.untracked.string('offlinePrimaryVertices'),
        doAddDepthTime = cms.untracked.bool(False)
        )
                                 )

process.baconSequence = cms.Sequence(#process.PFBRECO*
  process.metFilters*
  #process.pfMVAMEt30Sequence* #MVA ME
  process.producePFMETCorrections*
  process.pfCandNoLep*
  process.pfCandLep*
  process.puppinolep*
  process.egmPhotonIDSequence*
  process.puppimetinput*
  process.puppiPhoton*
  process.pfMetPuppi* #  Puppi Met
  process.ak4PFJetsPuppi* 
  process.ak4PuppiL1FastL2L3Chain*
  process.producePFMETCorrectionsPuppi *
  #process.producePFMETCorrections*
  #process.recojetsequence*
  #process.genjetsequence*
  #process.AK5jetsequenceCHS*
  #process.AK5genjetsequence*
  #process.recoTau*   ### must come after antiktGenJets otherwise conflict on RecoJets/JetProducers/plugins
  #process.MVAMetSeq*
  process.ntupler)

if do_hlt_filter:
  process.p = cms.Path(process.hltHighLevel*process.baconSequence)
else:
  process.p = cms.Path(process.baconSequence)
  
      #
      # simple checks to catch some mistakes...
      #
  if is_data_flag:
    assert process.ntupler.GenInfo.isActive == cms.untracked.bool(False)
  #  assert process.ntupler.Jet.doGenJet == cms.untracked.bool(False)
