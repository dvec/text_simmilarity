from logging import basicConfig, INFO

from text_similarity import SimilarityAnalyzer

basicConfig(level=INFO)
categories = ['полететь на марс', 'заказать пиццу', 'погладить кота']

if __name__ == '__main__':
    analyzer = SimilarityAnalyzer.load('./examples/.w2v/save')

    while 1:
        s = input()
        a = []
        for c in categories:
            a.append((analyzer.similarity(s, c), c))
        print(*map('{0[1]} - {0[0]}'.format, sorted(a, reverse=True)), sep='\n')
