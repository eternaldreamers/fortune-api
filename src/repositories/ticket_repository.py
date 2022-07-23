from injector import inject

# from src.models import TicketModel
# from src.schemas import TicketSchema

class TicketRepository:
    @inject
    def __init__(self):
        pass
        # self.__ticket_model = TicketModel
        # self.__ticket_schema = TicketSchema()
        # self.__tickets_schema = TicketSchema(many=True)

    def get_one(self, id):
        return {}
        # ticket = self.__ticket_model.query.filter_by(ticket_id=id).first()
        # return self.__ticket_schema.jsonify(ticket)

    def get_many(self):
        return []
        # tickets = self.__ticket_model.query.all()
        # result = self.__tickets_schema.dump(tickets)
        # return result

    def find_many(self, query):
        return []
        # tickets = self.__ticket_model.query.filter_by(*query).all()
        # result = self.__tickets_schema.dump(tickets)
        # return result

    def create(self, dto):
        return {}
        # new_ticket = self.__ticket_model(*dto)
        # return self.__ticket_schema.jsonify(new_ticket)