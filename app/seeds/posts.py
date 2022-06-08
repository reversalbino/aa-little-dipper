from app.models import db, Post



def seed_posts():
    post1 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_1.jpeg', title='weakness')
    post2 = Post(userId=43, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_2.jpeg', title='burst')
    post3 = Post(userId=47, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_3.jpeg', title='morale')
    post4 = Post(userId=4, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_4.jpeg', title='farewell')
    post5 = Post(userId=22, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_5.jpeg', title='manner')
    post6 = Post(userId=37, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_6.jpeg', title='hide')
    post7 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_7.jpeg', title='branch')
    post8 = Post(userId=6, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_8.jpeg', title='excavation')
    post9 = Post(userId=8, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_9.jpeg', title='way')
    post10 = Post(userId=36, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_10.jpeg', title='peel')
    post11 = Post(userId=14, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_11.jpeg', title='god')
    post12 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_12.jpeg', title='daughter')
    post13 = Post(userId=49, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_13.jpeg', title='volunteer')
    post14 = Post(userId=10, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_14.jpeg', title='mood')
    post15 = Post(userId=4, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_15.jpeg', title='collar')
    post16 = Post(userId=8, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_16.jpeg', title='publish')
    post17 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_17.jpeg', title='federation')
    post18 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_18.jpeg', title='kitchen')
    post19 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_19.jpeg', title='mist')
    post20 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_20.jpeg', title='laser')
    post21 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_21.jpeg', title='glow')
    post22 = Post(userId=26, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_22.jpeg', title='meaning')
    post23 = Post(userId=24, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_23.jpeg', title='jail')
    post24 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_24.jpeg', title='slime')
    post25 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_25.jpeg', title='line')
    post26 = Post(userId=30, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_26.jpeg', title='terms')
    post27 = Post(userId=25, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_27.jpeg', title='topple')
    post28 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_28.jpeg', title='panic')
    post29 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_29.jpeg', title='tourist')
    post30 = Post(userId=48, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_30.jpeg', title='bronze')
    post31 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_31.jpeg', title='slave')
    post32 = Post(userId=37, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_32.jpeg', title='precision')
    post33 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_33.jpeg', title='break')
    post34 = Post(userId=22, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_34.jpeg', title='desk')
    post35 = Post(userId=46, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_35.jpeg', title='distortion')
    post36 = Post(userId=45, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_36.jpeg', title='infrastructure')
    post37 = Post(userId=2, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_37.jpeg', title='presidential')
    post38 = Post(userId=1, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_38.jpeg', title='grimace')
    post39 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_39.jpeg', title='grow')
    post40 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_40.jpeg', title='roar')
    post41 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_41.jpeg', title='panel')
    post42 = Post(userId=31, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_42.jpeg', title='profit')
    post43 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_43.jpeg', title='inquiry')
    post44 = Post(userId=23, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_44.jpeg', title='chemistry')
    post45 = Post(userId=13, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_45.jpeg', title='taxi')
    post46 = Post(userId=32, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_46.jpeg', title='expertise')
    post47 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_47.jpeg', title='learn')
    post48 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_48.jpeg', title='language')
    post49 = Post(userId=5, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_49.jpeg', title='soap')
    post50 = Post(userId=51, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_50.jpeg', title='pupil')
    post51 = Post(userId=33, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_51.jpeg', title='palace')
    post52 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_52.jpeg', title='smart')
    post53 = Post(userId=1, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_53.jpeg', title='tragedy')
    post54 = Post(userId=41, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_54.jpeg', title='coat')
    post55 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_55.jpeg', title='drift')
    post56 = Post(userId=10, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_56.jpeg', title='curl')
    post57 = Post(userId=21, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_57.jpeg', title='place')
    post58 = Post(userId=36, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_58.jpeg', title='umbrella')
    post59 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_59.jpeg', title='irony')
    post60 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_60.jpeg', title='encourage')
    post61 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_61.jpeg', title='mix')
    post62 = Post(userId=29, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_62.jpeg', title='recommendation')
    post63 = Post(userId=42, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_63.jpeg', title='increase')
    post64 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_64.jpeg', title='gaffe')
    post65 = Post(userId=41, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_65.jpeg', title='object')
    post66 = Post(userId=34, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_66.jpeg', title='energy')
    post67 = Post(userId=50, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_67.jpeg', title='install')
    post68 = Post(userId=17, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_68.jpeg', title='portion')
    post69 = Post(userId=29, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_69.jpeg', title='tidy')
    post70 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_70.jpeg', title='litigation')
    post71 = Post(userId=45, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_71.jpeg', title='telephone')
    post72 = Post(userId=46, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_72.jpeg', title='bike')
    post73 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_73.jpeg', title='conversation')
    post74 = Post(userId=18, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_74.jpeg', title='single')
    post75 = Post(userId=10, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_75.jpeg', title='mug')
    post76 = Post(userId=27, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_76.jpeg', title='profile')
    post77 = Post(userId=52, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_77.jpeg', title='size')
    post78 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_78.jpeg', title='facade')
    post79 = Post(userId=19, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_79.jpeg', title='vegetable')
    post80 = Post(userId=15, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_80.jpeg', title='captivate')
    post81 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_81.jpeg', title='cancel')
    post82 = Post(userId=2, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_82.jpeg', title='exception')
    post83 = Post(userId=2, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_83.jpeg', title='goat')
    post84 = Post(userId=39, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_84.jpeg', title='nail')
    post85 = Post(userId=43, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_85.jpeg', title='consumer')
    post86 = Post(userId=35, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_86.jpeg', title='champion')
    post87 = Post(userId=21, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_87.jpeg', title='ton')
    post88 = Post(userId=49, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_88.jpeg', title='volume')
    post89 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_89.jpeg', title='crystal')
    post90 = Post(userId=10, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_90.jpeg', title='classify')
    post91 = Post(userId=41, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_91.jpeg', title='difference')
    post92 = Post(userId=46, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_92.jpeg', title='whisper')
    post93 = Post(userId=48, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_93.jpeg', title='exceed')
    post94 = Post(userId=48, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_94.jpeg', title='fix')
    post95 = Post(userId=49, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_95.jpeg', title='ditch')
    post96 = Post(userId=19, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_96.jpeg', title='appetite')
    post97 = Post(userId=24, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_97.jpeg', title='insure')
    post98 = Post(userId=9, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_98.jpeg', title='coerce')
    post99 = Post(userId=6, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_99.jpeg', title='negative')
    post100 = Post(userId=18, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_100.jpeg', title='orbit')
    post101 = Post(userId=39, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_101.jpeg', title='economic')
    post102 = Post(userId=49, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_102.jpeg', title='vat')
    post103 = Post(userId=36, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_103.jpeg', title='deposit')
    post104 = Post(userId=23, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_104.jpeg', title='comfort')
    post105 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_105.jpeg', title='emergency')
    post106 = Post(userId=51, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_106.jpeg', title='gain')
    post107 = Post(userId=28, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_107.jpeg', title='combination')
    post108 = Post(userId=35, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_108.jpeg', title='admiration')
    post109 = Post(userId=17, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_109.jpeg', title='writer')
    post110 = Post(userId=1, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_110.jpeg', title='estate')
    post111 = Post(userId=23, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_111.jpeg', title='accumulation')
    post112 = Post(userId=52, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_112.jpeg', title='mutation')
    post113 = Post(userId=22, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_113.jpeg', title='incredible')
    post114 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_114.jpeg', title='queen')
    post115 = Post(userId=47, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_115.jpeg', title='contempt')
    post116 = Post(userId=47, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_116.jpeg', title='large')
    post117 = Post(userId=21, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_117.jpeg', title='translate')
    post118 = Post(userId=43, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_118.jpeg', title='rumor')
    post119 = Post(userId=27, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_119.jpeg', title='realize')
    post120 = Post(userId=19, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_120.jpeg', title='crosswalk')
    post121 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_121.jpeg', title='lesson')
    post122 = Post(userId=13, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_122.jpeg', title='leg')
    post123 = Post(userId=45, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_123.jpeg', title='supplementary')
    post124 = Post(userId=30, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_124.jpeg', title='relax')
    post125 = Post(userId=47, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_125.jpeg', title='virtue')
    post126 = Post(userId=9, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_126.jpeg', title='freight')
    post127 = Post(userId=30, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_127.jpeg', title='gap')
    post128 = Post(userId=23, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_128.jpeg', title='total')
    post129 = Post(userId=40, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_129.jpeg', title='conductor')
    post130 = Post(userId=50, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_130.jpeg', title='plead')
    post131 = Post(userId=34, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_131.jpeg', title='exact')
    post132 = Post(userId=20, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_132.jpeg', title='dilemma')
    post133 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_133.jpeg', title='throw')
    post134 = Post(userId=48, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_134.jpeg', title='contract')
    post135 = Post(userId=5, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_135.jpeg', title='few')
    post136 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_136.jpeg', title='unfortunate')
    post137 = Post(userId=6, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_137.jpeg', title='us')
    post138 = Post(userId=11, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_138.jpeg', title='harsh')
    post139 = Post(userId=22, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_139.jpeg', title='cereal')
    post140 = Post(userId=31, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_140.jpeg', title='orgy')
    post141 = Post(userId=18, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_141.jpeg', title='onion')
    post142 = Post(userId=22, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_142.jpeg', title='overcharge')
    post143 = Post(userId=12, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_143.jpeg', title='workshop')
    post144 = Post(userId=50, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_144.jpeg', title='athlete')
    post145 = Post(userId=14, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_145.jpeg', title='formation')
    post146 = Post(userId=14, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_146.jpeg', title='separation')
    post147 = Post(userId=13, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_147.jpeg', title='width')
    post148 = Post(userId=11, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_148.jpeg', title='labour')
    post149 = Post(userId=5, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_149.jpeg', title='consumption')
    post150 = Post(userId=51, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_150.jpeg', title='marine')
    post151 = Post(userId=2, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_151.jpeg', title='railcar')
    post152 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_152.jpeg', title='format')
    post153 = Post(userId=28, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_153.jpeg', title='tool')
    post154 = Post(userId=27, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_154.jpeg', title='survivor')
    post155 = Post(userId=32, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_155.jpeg', title='inspiration')
    post156 = Post(userId=9, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_156.jpeg', title='road')
    post157 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_157.jpeg', title='slant')
    post158 = Post(userId=52, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_158.jpeg', title='club')
    post159 = Post(userId=40, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_159.jpeg', title='error')
    post160 = Post(userId=19, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_160.jpeg', title='bride')
    post161 = Post(userId=10, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_161.jpeg', title='bolt')
    post162 = Post(userId=36, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_162.jpeg', title='sand')
    post163 = Post(userId=26, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_163.jpeg', title='demand')
    post164 = Post(userId=4, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_164.jpeg', title='prevalence')
    post165 = Post(userId=47, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_165.jpeg', title='ivory')
    post166 = Post(userId=7, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_166.jpeg', title='concert')
    post167 = Post(userId=4, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_167.jpeg', title='gene')
    post168 = Post(userId=48, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_168.jpeg', title='hospitality')
    post169 = Post(userId=38, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_169.jpeg', title='inflate')
    post170 = Post(userId=35, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_170.jpeg', title='anger')
    post171 = Post(userId=26, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_171.jpeg', title='lace')
    post172 = Post(userId=2, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_172.jpeg', title='earthwax')
    post173 = Post(userId=27, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_173.jpeg', title='motorcycle')
    post174 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_174.jpeg', title='infinite')
    post175 = Post(userId=17, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_175.jpeg', title='quest')
    post176 = Post(userId=28, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_176.jpeg', title='owl')
    post177 = Post(userId=27, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_177.jpeg', title='location')
    post178 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_178.jpeg', title='confine')
    post179 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_179.jpeg', title='person')
    post180 = Post(userId=26, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_180.jpeg', title='vegetarian')
    post181 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_181.jpeg', title='hotdog')
    post182 = Post(userId=19, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_182.jpeg', title='helpless')
    post183 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_183.jpeg', title='retired')
    post184 = Post(userId=9, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_184.jpeg', title='cruel')
    post185 = Post(userId=44, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_185.jpeg', title='decorative')
    post186 = Post(userId=11, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_186.jpeg', title='prosper')
    post187 = Post(userId=39, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_187.jpeg', title='lecture')
    post188 = Post(userId=14, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_188.jpeg', title='hell')
    post189 = Post(userId=16, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_189.jpeg', title='bench')
    post190 = Post(userId=39, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_190.jpeg', title='circulate')
    post191 = Post(userId=12, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_191.jpeg', title='debut')
    post192 = Post(userId=42, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_192.jpeg', title='childish')
    post193 = Post(userId=53, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_193.jpeg', title='stop')
    post194 = Post(userId=50, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_194.jpeg', title='witch')
    post195 = Post(userId=40, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_195.jpeg', title='treasurer')
    post196 = Post(userId=32, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_196.jpeg', title='organ')
    post197 = Post(userId=21, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_197.jpeg', title='consciousness')
    post198 = Post(userId=14, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_198.jpeg', title='cheat')
    post199 = Post(userId=39, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_199.jpeg', title='dash')
    post200 = Post(userId=3, postImageUrl='https://little-dipper.s3.us-west-2.amazonaws.com/image_200.jpeg', title='get')

    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)
    db.session.add(post17)
    db.session.add(post18)
    db.session.add(post19)
    db.session.add(post20)
    db.session.add(post21)
    db.session.add(post22)
    db.session.add(post23)
    db.session.add(post24)
    db.session.add(post25)
    db.session.add(post26)
    db.session.add(post27)
    db.session.add(post28)
    db.session.add(post29)
    db.session.add(post30)
    db.session.add(post31)
    db.session.add(post32)
    db.session.add(post33)
    db.session.add(post34)
    db.session.add(post35)
    db.session.add(post36)
    db.session.add(post37)
    db.session.add(post38)
    db.session.add(post39)
    db.session.add(post40)
    db.session.add(post41)
    db.session.add(post42)
    db.session.add(post43)
    db.session.add(post44)
    db.session.add(post45)
    db.session.add(post46)
    db.session.add(post47)
    db.session.add(post48)
    db.session.add(post49)
    db.session.add(post50)
    db.session.add(post51)
    db.session.add(post52)
    db.session.add(post53)
    db.session.add(post54)
    db.session.add(post55)
    db.session.add(post56)
    db.session.add(post57)
    db.session.add(post58)
    db.session.add(post59)
    db.session.add(post60)
    db.session.add(post61)
    db.session.add(post62)
    db.session.add(post63)
    db.session.add(post64)
    db.session.add(post65)
    db.session.add(post66)
    db.session.add(post67)
    db.session.add(post68)
    db.session.add(post69)
    db.session.add(post70)
    db.session.add(post71)
    db.session.add(post72)
    db.session.add(post73)
    db.session.add(post74)
    db.session.add(post75)
    db.session.add(post76)
    db.session.add(post77)
    db.session.add(post78)
    db.session.add(post79)
    db.session.add(post80)
    db.session.add(post81)
    db.session.add(post82)
    db.session.add(post83)
    db.session.add(post84)
    db.session.add(post85)
    db.session.add(post86)
    db.session.add(post87)
    db.session.add(post88)
    db.session.add(post89)
    db.session.add(post90)
    db.session.add(post91)
    db.session.add(post92)
    db.session.add(post93)
    db.session.add(post94)
    db.session.add(post95)
    db.session.add(post96)
    db.session.add(post97)
    db.session.add(post98)
    db.session.add(post99)
    db.session.add(post100)
    db.session.add(post101)
    db.session.add(post102)
    db.session.add(post103)
    db.session.add(post104)
    db.session.add(post105)
    db.session.add(post106)
    db.session.add(post107)
    db.session.add(post108)
    db.session.add(post109)
    db.session.add(post110)
    db.session.add(post111)
    db.session.add(post112)
    db.session.add(post113)
    db.session.add(post114)
    db.session.add(post115)
    db.session.add(post116)
    db.session.add(post117)
    db.session.add(post118)
    db.session.add(post119)
    db.session.add(post120)
    db.session.add(post121)
    db.session.add(post122)
    db.session.add(post123)
    db.session.add(post124)
    db.session.add(post125)
    db.session.add(post126)
    db.session.add(post127)
    db.session.add(post128)
    db.session.add(post129)
    db.session.add(post130)
    db.session.add(post131)
    db.session.add(post132)
    db.session.add(post133)
    db.session.add(post134)
    db.session.add(post135)
    db.session.add(post136)
    db.session.add(post137)
    db.session.add(post138)
    db.session.add(post139)
    db.session.add(post140)
    db.session.add(post141)
    db.session.add(post142)
    db.session.add(post143)
    db.session.add(post144)
    db.session.add(post145)
    db.session.add(post146)
    db.session.add(post147)
    db.session.add(post148)
    db.session.add(post149)
    db.session.add(post150)
    db.session.add(post151)
    db.session.add(post152)
    db.session.add(post153)
    db.session.add(post154)
    db.session.add(post155)
    db.session.add(post156)
    db.session.add(post157)
    db.session.add(post158)
    db.session.add(post159)
    db.session.add(post160)
    db.session.add(post161)
    db.session.add(post162)
    db.session.add(post163)
    db.session.add(post164)
    db.session.add(post165)
    db.session.add(post166)
    db.session.add(post167)
    db.session.add(post168)
    db.session.add(post169)
    db.session.add(post170)
    db.session.add(post171)
    db.session.add(post172)
    db.session.add(post173)
    db.session.add(post174)
    db.session.add(post175)
    db.session.add(post176)
    db.session.add(post177)
    db.session.add(post178)
    db.session.add(post179)
    db.session.add(post180)
    db.session.add(post181)
    db.session.add(post182)
    db.session.add(post183)
    db.session.add(post184)
    db.session.add(post185)
    db.session.add(post186)
    db.session.add(post187)
    db.session.add(post188)
    db.session.add(post189)
    db.session.add(post190)
    db.session.add(post191)
    db.session.add(post192)
    db.session.add(post193)
    db.session.add(post194)
    db.session.add(post195)
    db.session.add(post196)
    db.session.add(post197)
    db.session.add(post198)
    db.session.add(post199)
    db.session.add(post200)

    db.session.commit()

def undo_posts():
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()
