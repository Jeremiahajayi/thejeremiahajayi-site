#!/usr/bin/env python3
"""Write the inner page templates (pages/*.html) in the homepage's language."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import inner_services as S, inner_work as W, inner_rest as R, inner_wid as D
P = pathlib.Path(__file__).parent / 'pages'
out = {
    'services': S.services(), 'svc-positioning': S.service('svc-positioning'), 'svc-launch': S.service('svc-launch'),
    'svc-content': S.service('svc-content'), 'work': W.page(), 'about': R.about(), 'writing': R.writing(),
    'empowerq': R.empowerq(), 'contact': R.contact(), 'what-id-do': D.page(),
}
for k, v in out.items():
    (P / f'{k}.html').write_text(v)
    print('page', k, len(v))
