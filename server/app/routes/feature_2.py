from fastapi import APIRouter

router = APIRouter(prefix='/api/v1/2', tags=['feature'])

@router.get('/status')
def feature_2_status():
    return {'ok': True, 'feature': 'Desenvolver e implementar um componente React para visualização de dados de equipamento.', 'task': '2'}
