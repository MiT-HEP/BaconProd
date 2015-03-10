#ifndef BACONPROD_NTUPLER_FILLERMUON_HH
#define BACONPROD_NTUPLER_FILLERMUON_HH

#include "BaconProd/Utils/interface/TriggerTools.hh"
#include <vector>
#include <string>

// forward class declarations
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
class TClonesArray;
namespace trigger {
  class TriggerEvent;
}


namespace baconhep
{
  class FillerMuon
  {
    public:
      FillerMuon(const edm::ParameterSet &iConfig);
      ~FillerMuon();
      
      void fill(TClonesArray			 *array,	   // output array to be filled
                const edm::Event		 &iEvent,	   // event info
	        const edm::EventSetup		 &iSetup,	   // event setup info
	        const reco::Vertex		 &pv,	           // event primary vertex
	        const std::vector<TriggerRecord> &triggerRecords,  // list of trigger names and objects
	        const trigger::TriggerEvent	 &triggerEvent);   // event trigger objects

      
      // Muon cuts
      double fMinPt;
      
      // EDM object collection names
      std::string fMuonName;
      std::string fPFCandName;
      std::string fTrackName;

      // general tracks cuts
      bool   fSaveTracks;
      double fTrackMinPt;
  };
}
#endif
