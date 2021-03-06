__author__ = 'jrlimingyang@jd.com'

import os


def conlleval(label_predict, label_path, metric_path):
    """

    :param label_predict:
    :param label_path:
    :param metric_path:
    :return:
    """
    eval_perl = '../model/conlleval_rev.pl'
    with open(label_path, 'w', encoding='utf-8') as fw:
        line = []
        for sent_result in label_predict:
            for char, tag, tag_ in sent_result:
                tag = '0' if tag == '0' else tag
                # char = char.encode('utf-8')
                line.append('{} {} {}\n'.format(char, tag, tag_))
            line.append('\n')
        fw.writelines(line)
    os.system('perl {} < {} > {}'.format(eval_perl, label_path, metric_path))
    with open(metric_path) as fr:
        metrics = [line.split() for line in fr]
    return metrics


if __name__ == '__main__':
    conlleval([], '../data_save/1560322519/results/label_1', '../data_save/1560322519/results/result_metric_1')
