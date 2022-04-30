dataset_info = dict(
    dataset_name='openMonkey',
    paper_info=dict(
        author='obtained from the internet, three National Primate Research Centers, and the Minnesota Zoo',
        title='OpenMonkeyChallenge Dataset',
        homepage='http://openmonkeychallenge.com/challenge.html',
    ),
    keypoint_info={
        0:
        dict(name='right_eye', id=0, color=[51, 153, 255], type='upper', swap='right_eye'),
        1:
        dict(
            name='left_eye',
            id=1,
            color=[0,0,0],
            type='upper',
            swap='right_eye'),
        2:
        dict(
            name='nose',
            id=2,
            color=[0,0,0],
            type='upper',
            swap=''),
        3:
        dict(
            name='head',
            id=3,
            color=[0,0,0],
            type='upper',
            swap=''),
        4:
        dict(
            name='neck',
            id=4,
            color=[0,0,0],
            type='upper',
            swap=''),
        5:
        dict(
            name='right_shoulder',
            id=5,
            color=[0,0,0],
            type='upper',
            swap='left_shoulder'),
        6:
        dict(
            name='right_elbow',
            id=6,
            color=[0,0,0],
            type='upper',
            swap='left_elbow'),
        7:
        dict(
            name='right_wrist',
            id=7,
            color=[0,0,0],
            type='upper',
            swap='left_wrist'),
        8:
        dict(
            name='left_shoulder',
            id=8,
            color=[0,0,0],
            type='upper',
            swap='right_shoulder'),
        9:
        dict(
            name='left_elbow',
            id=9,
            color=[0,0,0],
            type='upper',
            swap='right_elbow'),
        10:
        dict(
            name='left_wrist',
            id=10,
            color=[0,0,0],
            type='upper',
            swap='right_wrist'),
        11:
        dict(
            name='hip',
            id=11,
            color=[0,0,0],
            type='lower',
            swap=''),
        12:
        dict(
            name='right_knee',
            id=12,
            color=[0,0,0],
            type='lower',
            swap='left_knee'),
        13:
        dict(
            name='right_ankle',
            id=13,
            color=[0,0,0],
            type='lower',
            swap='left_ankle'),
        14:
        dict(
            name='left_knee',
            id=14,
            color=[0,0,0],
            type='lower',
            swap='right_knee'),
        15:
        dict(
            name='left_ankle',
            id=15,
            color=[0,0,0],
            type='lower',
            swap='right_ankle'),
        16:
        dict(
            name='tail',
            id=16,
            color=[0,0,0],
            type='lower',
            swap='')
    },
    skeleton_info={
        0:
        dict(link=('left_eye', 'nose'), id=0, color=[195,159,232]),
        1:
        dict(link=('right_eye', 'nose'), id=1, color=[195,159,232]),
        2:
        dict(link=('head', 'neck'), id=2, color=[177,38,27]),
        3:
        dict(link=('left_shoulder', 'neck'), id=3, color=[60,55,184]),
        4:
        dict(link=('right_shoulder', 'neck'), id=4, color=[38,78,132]),
        5:
        dict(link=('left_shoulder', 'left_elbow'), id=5, color=[130,170,210]),
        6:
        dict(link=('right_shoulder', 'right_elbow'), id=6, color=[90,130,190]),
        7:
        dict(
            link=('right_elbow', 'right_wrist'),
            id=7,
            color=[70,130,210]),
        8:
        dict(link=('left_elbow', 'left_wrist'), id=8, color=[90,196,197]),
        9:
        dict(
            link=('neck', 'hip'), id=9, color=[200,115,43]),
        10:
        dict(link=('hip', 'tail'), id=10, color=[230,230,85]),


        11:
        dict(link=('hip', 'right_knee'), id=11, color=[255, 128, 0]),
        12:
        dict(link=('hip', 'left_knee'), id=12, color=[51, 153, 255]),
        13:
        dict(link=('right_knee', 'right_ankle'), id=13, color=[51, 153, 255]),
        14:
        dict(link=('left_knee', 'left_ankle'), id=14, color=[51, 153, 255])
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1.2, 1.2, 1.5, 1.5, 1., 1., 1.2, 1.2, 1.5,
        1.5
    ],
    sigmas=[
        0.026, 0.025, 0.025, 0.035, 0.035, 0.079, 0.079, 0.072, 0.072, 0.062,
        0.062, 0.107, 0.107, 0.087, 0.087, 0.089, 0.089
    ])