from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/1', tags=['feature'])

@router.get('/status')
def feature_1_status():
    return {'ok': True, 'feature': 'Identificar e documentar requisitos funcionais para o painel administrativo React.', 'task': '1'}
