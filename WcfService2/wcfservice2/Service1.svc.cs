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
using MongoDB.Bson.IO;
using System.Web.Script.Serialization;
using Newtonsoft.Json;
using System.Diagnostics;
using System.IO;



namespace WcfService2
{
    public class Products
    {
        public ObjectId _id { get; set; }
        public String price { get; set; }
        public List<Specs> specs { get; set; }
        public String Title { get; set; }
    }

    public class Specs 
    {
        public String name { get; set;}
        public String value { get; set; }
    }

    public class Service1 : IService1
    {
        public List<Products> getProducts()
        {
            //Connect met MongoDB op de server
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            //Pak database "Products", en de collectie "files2", hierin staan de producten
            MongoDatabase database = server.GetDatabase("DevOpdr");
            MongoCollection<Products> products = database.GetCollection<Products>("Muziek");
            //Pak alle BSON documenten
            MongoCursor<Products> allProducts = products.FindAll();
            //Zet alle documenten in een lijst
            List<Products> productsList = allProducts.ToList();
            return productsList;
        }



    }
    
}
