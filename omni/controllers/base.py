class BaseController:
    _model = None
    _name = None

    async def create(self, **kwargs):
        instance = None
        try:
            print(kwargs)
            instance = await self._model.get_or_none(email=kwargs['email'])
        except Exception as error:
            message = f'Error {self._name}: field {error}'
            print(message)
            return instance, message
        if instance:
            return instance, 'User already exist'
        try:
            instance = await self._model.create(**kwargs)
            message = f'Successfully created {self._name}'
            print(message)
            return instance, message
        except Exception as error:
            message = f'Error {self._name} Model: {error}'
            print(message)
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
