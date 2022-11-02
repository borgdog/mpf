"""Defines for FAST Boards."""

HARDWARE_KEY = {
    "fast":  '2000',
    "sys11": '1100',
    "wpc89": '8900',
    "wpc95": '9500'
}

RETRO_SWITCH_MAP = {

    # Name   HEX    DEC
    'S11': '00',  # 00
    'S12': '01',  # 01
    'S13': '02',  # 02
    'S14': '03',  # 03
    'S15': '04',  # 04
    'S16': '05',  # 05
    'S17': '06',  # 06
    'S18': '07',  # 07

    'S21': '08',  # 08
    'S22': '09',  # 09
    'S23': '0A',  # 10
    'S24': '0B',  # 11
    'S25': '0C',  # 12
    'S26': '0D',  # 13
    'S27': '0E',  # 14
    'S28': '0F',  # 15

    'S31': '10',  # 16
    'S32': '11',  # 17
    'S33': '12',  # 18
    'S34': '13',  # 19
    'S35': '14',  # 20
    'S36': '15',  # 21
    'S37': '16',  # 22
    'S38': '17',  # 23

    'S41': '18',  # 24
    'S42': '19',  # 25
    'S43': '1A',  # 26
    'S44': '1B',  # 27
    'S45': '1C',  # 28
    'S46': '1D',  # 29
    'S47': '1E',  # 30
    'S48': '1F',  # 31

    'S51': '20',  # 32
    'S52': '21',  # 33
    'S53': '22',  # 34
    'S54': '23',  # 35
    'S55': '24',  # 36
    'S56': '25',  # 37
    'S57': '26',  # 38
    'S58': '27',  # 39

    'S61': '28',  # 40
    'S62': '29',  # 41
    'S63': '2A',  # 42
    'S64': '2B',  # 43
    'S65': '2C',  # 44
    'S66': '2D',  # 45
    'S67': '2E',  # 46
    'S68': '2F',  # 47

    'S71': '30',  # 48
    'S72': '31',  # 49
    'S73': '32',  # 50
    'S74': '33',  # 51
    'S75': '34',  # 52
    'S76': '35',  # 53
    'S77': '36',  # 54
    'S78': '37',  # 55

    'S81': '38',  # 56
    'S82': '39',  # 57
    'S83': '3A',  # 58
    'S84': '3B',  # 59
    'S85': '3C',  # 60
    'S86': '3D',  # 61
    'S87': '3E',  # 62
    'S88': '3F',  # 63

    'S91': '40',  # 64
    'S92': '41',  # 65
    'S93': '42',  # 66
    'S94': '43',  # 67
    'S95': '44',  # 68
    'S96': '45',  # 69
    'S97': '46',  # 70
    'S98': '47',  # 71

    'S101': '48',  # 72
    'S102': '49',  # 73
    'S103': '4A',  # 74
    'S104': '4B',  # 75
    'S105': '4C',  # 76
    'S106': '4D',  # 77
    'S107': '4E',  # 78
    'S108': '4F',  # 79

    # Directs
    'SD1': '50',  # 80
    'SD2': '51',  # 81
    'SD3': '52',  # 82
    'SD4': '53',  # 83
    'SD5': '54',  # 84
    'SD6': '55',  # 85
    'SD7': '56',  # 86
    'SD8': '57',  # 87

    # Fliptronics
    'SF1': '58',  # 88
    'SF2': '59',  # 89
    'SF3': '5A',  # 90
    'SF4': '5B',  # 91
    'SF5': '5C',  # 92
    'SF6': '5D',  # 93
    'SF7': '5E',  # 94
    'SF8': '5F',  # 95

    # DIP switches
    # These addresses are also used by Fliptronics switches (above) but can be
    # used in non-Fliptronics machines (e.g. System11) as regular switches.
    'DIP1': '58',  # 88
    'DIP2': '59',  # 89
    'DIP3': '5A',  # 90
    'DIP4': '5B',  # 91
    'DIP5': '5C',  # 92
    'DIP6': '5D',  # 93
    'DIP7': '5E',  # 94
    'DIP8': '5F',  # 95
}

RETRO_LIGHT_MAP = {
    'L11': '00', 'L12': '01', 'L13': '02', 'L14': '03',
    'L15': '04', 'L16': '05', 'L17': '06', 'L18': '07',
    'L21': '08', 'L22': '09', 'L23': '0A', 'L24': '0B',
    'L25': '0C', 'L26': '0D', 'L27': '0E', 'L28': '0F',
    'L31': '10', 'L32': '11', 'L33': '12', 'L34': '13',
    'L35': '14', 'L36': '15', 'L37': '16', 'L38': '17',
    'L41': '18', 'L42': '19', 'L43': '1A', 'L44': '1B',
    'L45': '1C', 'L46': '1D', 'L47': '1E', 'L48': '1F',
    'L51': '20', 'L52': '21', 'L53': '22', 'L54': '23',
    'L55': '24', 'L56': '25', 'L57': '26', 'L58': '27',
    'L61': '28', 'L62': '29', 'L63': '2A', 'L64': '2B',
    'L65': '2C', 'L66': '2D', 'L67': '2E', 'L68': '2F',
    'L71': '30', 'L72': '31', 'L73': '32', 'L74': '33',
    'L75': '34', 'L76': '35', 'L77': '36', 'L78': '37',
    'L81': '38', 'L82': '39', 'L83': '3A', 'L84': '3B',
    'L85': '3C', 'L86': '3D', 'L87': '3E', 'L88': '3F',
}

RETRO_DRIVER_MAP = {
    'C01': '00', 'C02': '01', 'C03': '02', 'C04': '03',
    'C05': '04', 'C06': '05', 'C07': '06', 'C08': '07',
    'C09': '08', 'C10': '09', 'C11': '0A', 'C12': '0B',
    'C13': '0C', 'C14': '0D', 'C15': '0E', 'C16': '0F',
    'C17': '10', 'C18': '11', 'C19': '12', 'C20': '13',
    'C21': '14', 'C22': '15', 'C23': '16', 'C24': '17',
    'C25': '18', 'C26': '19', 'C27': '1A', 'C28': '1B',
    'C29': '1C', 'C30': '1D', 'C31': '1E', 'C32': '1F',
    'C33': '24', 'C34': '25', 'C35': '26', 'C36': '27',
    'C37': '28', 'C38': '29', 'C39': '2A', 'C40': '2B',
    'C41': '2C', 'C42': '2D', 'C43': '2E', 'C44': '2F',
    'FLRM': '20', 'FLRH': '21', 'FLLM': '22', 'FLLH': '23',
    'FURM': '24', 'FURH': '25', 'FULM': '26', 'FULH': '27',
}

RETRO_GI_MAP = {
    'G01': '00', 'G02': '01', 'G03': '02', 'G04': '03',
    'G05': '04', 'G06': '05', 'G07': '06', 'G08': '07',
}

EXPANSION_BOARD_ADDRESS_MAP = {

    # board type - index : one byte address
    'exp-0071-i0': 'B4',
    'exp-0071-i1': 'B5',
    'exp-0071-i2': 'B6',
    'exp-0071-i3': 'B7',

    'exp-0201-i0': '88',
    'exp-0201-i1': '89',
    'exp-0201-i2': '8A',
    'exp-0201-i3': '8B',

    'cpu-2000-i0': '48',
}

EXPANSION_BOARD_BREAKOUT_MAP = {

    # board: highest breakout index, zero-based
    '0071': 2,
    '0201': 3,
    '2000': 5,
}