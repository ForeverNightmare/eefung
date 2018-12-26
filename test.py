# coding=gbk
import tensorflow as tf
import numpy as np

# ����һ������, ��ʼ��Ϊ���� 0.
state = tf.Variable(0, name="counter")

# ����һ�� op, ��������ʹ state ���� 1

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# ����ͼ��, ���������Ⱦ���`��ʼ��` (init) op ��ʼ��,
# ���ȱ�������һ��`��ʼ��` op ��ͼ��.
init_op = tf.initialize_all_variables()

# ����ͼ, ���� op
with tf.Session() as sess:
    # ���� 'init' op
    sess.run(init_op)
    # ��ӡ 'state' �ĳ�ʼֵ
    print(sess.run(state))
    # ���� op, ���� 'state', ����ӡ 'state'
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

# ���:

# 0
# 1
# 2
# 3