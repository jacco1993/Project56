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
    public class Muziek
    {
        [BsonId]
        public ObjectId _id  { get; set; }
        public String artiest { get; set; }
        public String genre { get; set; }
        public Song songs { get; set; }
    }



    public class Song
    {
        public String title { get; set; }
        public String title1 { get; set; }
        public String title2 { get; set; }
    }

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

        /*public MongoServer server;

        public MongoServer Server()
        {
            var connectionString = "mongodb://localhost:27017";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            return server;
        }*/

        public List<Muziek> getMusic()
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            MongoDatabase database = server.GetDatabase("DevOpdr");
            MongoCollection<Muziek> muziek = database.GetCollection<Muziek>("Muziek");
            MongoCursor<Muziek> alles = muziek.FindAll();
            List<Muziek> muziekLijst = alles.ToList();
            return muziekLijst;
            //var jsonSerialiser = new JavaScriptSerializer();
            //var json = jsonSerialiser.Serialize(muziekLijst);
            //return new MemoryStream(Encoding.UTF8.GetBytes(json));
            

            //return json;
        }

        public List<Products> getProducts()
        {
            //Connect met MongoDB op de server
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            //Pak database "Project56", en de collectie "Products"
            MongoDatabase database = server.GetDatabase("Products");
            MongoCollection<Products> products = database.GetCollection<Products>("files2");
            //Pak alle BSON documenten
            MongoCursor<Products> allProducts = products.FindAll();
            //Zet alle documenten in een lijst
            List<Products> productsList = allProducts.ToList();
            return productsList;
        }

    }
    
}
