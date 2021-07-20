class BaseController:
    _model = None
    _name = None

    async def create(self, **kwargs):
        instance = None
        try:
            instance = await self._model.create(**kwargs)
            message = f'Successfully created {self._name}'
            print(message)
            return instance, message
        except Exception as error:
            error = str(error)
            if 'user_email_key' in error:
                instance = await self._model.get(email=kwargs['email'])
                return instance, f'{self._name} already exist'
            message = f'Error {self._name} Model: {error}'
            return instance, message

    @classmethod
    async def get(cls, id):
        return await cls._model.get_or_none(id=id)

    async def update(self, _id,  **kwargs):
        if kwargs.get('email'):
            kwargs.pop('email')
        await self._model.get(id=_id).update(**kwargs)
        self._model = await self._model.get(id=_id)
        print(f'Update { self._name} success')
        return self._model

    async def delete(self, _id):
        await self._model.get(id=_id).delete()

    @classmethod
    async def all(cls):
        return await cls._model.all()
