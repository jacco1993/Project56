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
<<<<<<< HEAD
using System.IO;
=======
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001

namespace WcfService2
{

    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
<<<<<<< HEAD
        [WebGet(UriTemplate="getproducts")]
        String getProducts();
        [WebGet(UriTemplate = "getmusic", ResponseFormat = WebMessageFormat.Json)]
        [OperationContract]
        List<Muziek> getMusic();
=======
        String getProducts();
        [OperationContract]
        String getMusic();
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001
        //MongoServer Server();
    }
    }