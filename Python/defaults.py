PRESET_PARTS = {
  "DbAudiowarePreset": {
    "product": "DMXIS",
    "major": "1",
    "minor": "2",
    "patch": "0",
    "algoname": "DMXIS",
  },

  "Param": {
    "v": "0.000000",
    "cc": "-1",
    "nrpn": "-1",
    "ch": "0",
  },

  "c": {
    "t": "0",
    "a": "0.500000",
    "p": "0.000000",
    "s": "7",
    "tm": "10.000000",
    "sh": "0.500000",
    "i": "0",
    "en": "1",
    "fa": "1.000000",
    "fr": "49.987503",
    "fg": "0"
    }
  }

DMX_NAMES = [str(i) for i in xrange(1, 513)]

PARAM_FIRST = [
  'X Value', 'Bank', 'Preset', 'PresetUp', 'PresetDown', 'ShowPresetPage',
  'BankUp', 'BankDown', 'NewPreset', 'DeletePreset', 'EditPreset', 'NewBank',
  'DeleteBank', 'EditBank', 'SortMode', 'Autoplay Bank', 'OverwrtPst']

PARAM_SECOND = [
  'DmxNextPage', 'DmxPrevPage', 'Master Speed', 'MasterTempo', 'Macros',
  'Grand Master', 'Crossfade', 'Type', 'Amount', 'Offset', 'Speed', 'Shape',
  'Band', 'Level', 'Attack', 'Release', 'Dir', 'Invert']

PARAM_NAMES = PARAM_FIRST + DMX_NAMES + PARAM_SECOND

def Get(theName, **kwds):
  return dict(PRESET_PARTS[theName], **kwds)
