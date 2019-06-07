from dateutil import tz

symbol = 'btc_usd'
contractType = 'next_quarter'

init_money = 0
init_btc = 1

models = ['RF','XGB']

types = ['1min','3min','5min','15min', '30min','1hour','2hour','4hour','6hour','12hour','1day','3day','1week']
typetimes = [60, 3 * 50, 5 * 60, 15 * 60, 30 * 60, 3600, 2 * 3600, 4 * 3600, 6 * 3600, 12 *3600, 24 * 3600, 3 * 24 * 3600, 7 * 24 * 3600]
typesizes = [2401, 2881, 1729, 1681, 1681, 1681, 1681, 841, 561, 401, 1301, 434, 186]
refreshtimes = [typetime * 1000 for typetime in typetimes] # update kline every 1000 * their time
MAX_SIZE=6000

alpha = 0.06
build_point = 0.5
t0 = 3 * 24 * 3600 # 3 days

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

indicators = [
        # volume delta against previous day
        'volume_-20_d',
        'close_-20_r',

        # open delta against next 2 day
        #'open_2_d',

        # open price change (in percent) between today and the day before yesterday
        # 'r' stands for rate.
        #'open_-2_r',

        # CR indicator, including 5, 10, 20 days moving average
       # 'cr',
        #'cr-ma1',
        #'cr-ma2',
        'cr-ma3',

        # volume max of three days ago, yesterday and two days later
        #'volume_-3,2,-1_max',

        # volume min between 3 days ago and tomorrow
        'volume_-15~0_min',
        'volume_-15~0_max',

        # KDJ, default to 9 days
        'kdjk_18',
        'kdjd_18',
        'kdjj_18',
        #'kdjk_3',
        #'kdjd_3',
        #'kdjj_3',

        # three days KDJK cross up 3 days KDJD
        #'kdjk_3_xu_kdjd_3',

        # 2 days simple moving average on open price
        'open_15_sma',

        # MACD
        #'macd',
        # MACD signal line
        #'macds',
        # MACD histogram
        #'macdh',

        # bolling, including upper band and lower band
        #'boll',
        #'boll_ub',
        #'boll_lb',

        # close price less than 10.0 in 5 days count
        #'close_10.0_le_5_c',

        # CR MA2 cross up CR MA1 in 20 days count
        #'cr-ma2_xu_cr-ma1_20_c',

        # 6 days RSI
        #'rsi_6',
        # 12 days RSI
        #'rsi_12',

        # 10 days WR
        'wr_10',
        # 6 days WR
        #'wr_6',

        # CCI, default to 14 days
        #'cci',
        # 20 days CCI
        'cci_20',

        # TR (true range)
        #'tr',
        # ATR (Average True Range)
        #'atr',

        # DMA, difference of 10 and 50 moving average
        #'dma',

        # DMI
        # +DI, default to 14 days
        'pdi',
        # -DI, default to 14 days
        'mdi',
        # DX, default to 14 days of +DI and -DI
        #'dx',
        # ADX, 6 days SMA of DX, same as 'dx_6_ema',
        #'adx',
        #'dx_6_ema',
        # ADXR, 6 days SMA of ADX, same as 'adx_6_ema',
        #'adx_6_ema',

        # TRIX, default to 12 days
        #'trix',
        # MATRIX is the simple moving average of TRIX
        #'trix_15_sma',

        # VR, default to 26 days
        'vr',
        # MAVR is the simple moving average of VR
        'vr_20_sma'
        ]

indicators_TALIB = ['CDL2CROWS', #            Two Crows

        'CDL3BLACKCROWS',#       Three Black Crows

        'CDL3INSIDE',#           Three Inside Up/Down

        'CDL3LINESTRIKE',#       Three-Line Strike

        'CDL3OUTSIDE',#          Three Outside Up/Down

        'CDL3STARSINSOUTH',#     Three Stars In The South

        'CDL3WHITESOLDIERS',#    Three Advancing White Soldiers

        'CDLABANDONEDBABY',#     Abandoned Baby

        'CDLADVANCEBLOCK',#      Advance Block

        'CDLBELTHOLD',#          Belt-hold

        'CDLBREAKAWAY',#         Breakaway

        'CDLCLOSINGMARUBOZU',#   Closing Marubozu

        'CDLCONCEALBABYSWALL',#  Concealing Baby Swallow

        'CDLCOUNTERATTACK',#    Counterattack

        'CDLDARKCLOUDCOVER',#    Dark Cloud Cover

        'CDLDOJI',#              Doji

        'CDLDOJISTAR',#          Doji Star

        'CDLDRAGONFLYDOJI',#     Dragonfly Doji

        'CDLENGULFING',#         Engulfing Pattern

        'CDLEVENINGDOJISTAR',#   Evening Doji Star

        'CDLEVENINGSTAR',#       Evening Star

        'CDLGAPSIDESIDEWHITE',#  Up/Down-gap side-by-side white lines

        'CDLGRAVESTONEDOJI',#    Gravestone Doji

        'CDLHAMMER',#            Hammer

        'CDLHANGINGMAN',#        Hanging Man

        'CDLHARAMI',#            Harami Pattern

        'CDLHARAMICROSS',#       Harami Cross Pattern

        'CDLHIGHWAVE',#          High-Wave Candle

        'CDLHIKKAKE',#           Hikkake Pattern

        'CDLHIKKAKEMOD',#        Modified Hikkake Pattern

        'CDLHOMINGPIGEON',#      Homing Pigeon

        'CDLIDENTICAL3CROWS',#   Identical Three Crows

        'CDLINNECK',#            In-Neck Pattern

        'CDLINVERTEDHAMMER',#    Inverted Hammer

        'CDLKICKING',#           Kicking

        'CDLKICKINGBYLENGTH',#   Kicking - bull/bear determined by the longer marubozu

        'CDLLADDERBOTTOM',#      Ladder Bottom

        'CDLLONGLEGGEDDOJI',#    Long Legged Doji

        'CDLLONGLINE',#          Long Line Candle

        'CDLMARUBOZU',#          Marubozu

        'CDLMATCHINGLOW',#       Matching Low

        'CDLMATHOLD',#           Mat Hold

        'CDLMORNINGDOJISTAR',#   Morning Doji Star

        'CDLMORNINGSTAR',#       Morning Star

        'CDLONNECK',#            On-Neck Pattern

        'CDLPIERCING',#          Piercing Pattern

        'CDLRICKSHAWMAN',#       Rickshaw Man

        'CDLRISEFALL3METHODS',#  Rising/Falling Three Methods

        'CDLSEPARATINGLINES',#   Separating Lines

        'CDLSHOOTINGSTAR',#      Shooting Star

        'CDLSHORTLINE',#         Short Line Candle

        'CDLSPINNINGTOP',#       Spinning Top

        'CDLSTALLEDPATTERN',#    Stalled Pattern

        'CDLSTICKSANDWICH',#     Stick Sandwich

        'CDLTAKURI',#            Takuri (Dragonfly Doji with very long lower shadow)

        'CDLTASUKIGAP',#         Tasuki Gap

        'CDLTHRUSTING',#         Thrusting Pattern

        'CDLTRISTAR',#           Tristar Pattern

        'CDLUNIQUE3RIVER',#      Unique 3 River

        'CDLUPSIDEGAP2CROWS',#   Upside Gap Two Crows

        'CDLXSIDEGAP3METHODS'#  Upside/Downside Gap Three Methods
        ]
