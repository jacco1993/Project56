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
using System.IO;

namespace WcfService2
{
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        //Zodra je getproducts meegeeft achteraanaan de service URL, krijg je de List die in getproducts wordt gereturned
        //Zet deze list om naar JSON
        [WebGet(UriTemplate = "getproducts", ResponseFormat = WebMessageFormat.Json)]
         List<Products> getProducts();
    }
    }