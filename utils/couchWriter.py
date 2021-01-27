import couchdb

class couchWriter:
    """
    what is my purpose?

    you write to couch.

    oh my god
    """

    def __init__(self,server='http://admin:Bluboi314!@127.0.0.1:5984/'):
        self.server = server


    def start_session(self):
        """
        starts the couch session for writing & reading
        :return: sofa.Couch object
        """

        try:
            return couchdb.Server(self.server)

        except Exception as exception:
            print('Error occured in setting up session:{}'.format(exception))
            raise Exception

    def save_doc(self,doc,sofa = None,dbname = ''):
        """
        Save single json adherent documents
        :param doc: json adherent object to attempt writing
        :param sofa: optional sofa.Couch database
        :param dbname: string of target db in couch
        :return: None
        """

        # start session if one isn't passed #
        if not sofa:
            ## need either a dbname or a couch db object ##
            if not dbname:
                print('please supply a db name to write to')

                return None
            couch = self.start_session()
            sofa = couch[str(dbname)]

        sofa.save(doc)

        return None

    def save_docs(self,docs=[],dbname = ''):
        """
        executes self.save_doc for each doc in docs
        :param docs: list of json adherent objects
        :param dbname: string name of target database for writing
        :return:
        """

        couch = self.start_session()

        if not dbname:

            print('please supply a db name to write to')

            return None

        sofa_= couch[str(dbname)]

        for doc in docs:
            # we want an all or nothing write so no try-except here #
            self.save_doc(doc=doc,
                          sofa=sofa_)

        return None

