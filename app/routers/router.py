from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def read_root():
    return [{
        'id': 1,
        'name': 'first'
    }]


@router.get('/comic_id')
def read_comic(comic_id: int):
    return {'comic_id': comic_id, 'name': 'first'}
