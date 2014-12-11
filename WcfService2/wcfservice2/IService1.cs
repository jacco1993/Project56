using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using MongoDB.Bson;
using MongoDB.Driver;
using MongoDB.Driver.Builders;
using MongoDB.Driver.GridFS;
using MongoDB.Driver.Linq;
using MongoDB;
using MongoDB.Bson.Serialization.Attributes;

namespace WcfService2
{

    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        String getProducts();
        [OperationContract]
        String getMusic();
        //MongoServer Server();
    }
    }