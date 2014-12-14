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
<<<<<<< HEAD
using System.IO;
=======
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001



namespace WcfService2
{
    public class Muziek
    {
<<<<<<< HEAD
        [BsonId]
=======
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001
        public ObjectId _id { get; set; }
        public String artiest { get; set; }
        public String genre { get; set; }
        public Song songs { get; set; }
    }

<<<<<<< HEAD


=======
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001
    public class Song
    {
        public String title { get; set; }
        public String title1 { get; set; }
        public String title2 { get; set; }
    }
<<<<<<< HEAD
    
    public class Products
    {
        public String title { get; set; }
        public String title1 { get; set; }
        public String title2 { get; set; }
    }
=======

>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001


    public class Service1 : IService1
    {

<<<<<<< HEAD
        /*public MongoServer server;

        public MongoServer Server()
        {
            var connectionString = "mongodb://localhost:27017";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            return server;
        }*/

        public List<Muziek> getMusic()
=======
        public String getProducts()
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            MongoDatabase database = server.GetDatabase("DevOpdr");
            MongoCollection<Muziek> muziek = database.GetCollection<Muziek>("Muziek");
            MongoCursor<Muziek> alles = muziek.FindAll();
<<<<<<< HEAD
            List<Muziek> muziekLijst = alles.ToList();
            return muziekLijst;
            //var jsonSerialiser = new JavaScriptSerializer();
            //var json = jsonSerialiser.Serialize(muziekLijst);
            //return new MemoryStream(Encoding.UTF8.GetBytes(json));
            

            //return json;
        }

        public String getProducts()
        {
            //Connect met MongoDB op de server
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            //Pak database "Project56", en de collectie "Products"
            MongoDatabase database = server.GetDatabase("Project56");
            MongoCollection<Products> products = database.GetCollection<Products>("Products");
            //Pak alle BSON documenten
            MongoCursor<Products> allProducts = products.FindAll();
            //Zet alle documenten in een lijst
            List<Products> productsList = allProducts.ToList();
            //Zet BSON om in JSON
            var jsonSerialiser = new JavaScriptSerializer();
            var json = jsonSerialiser.Serialize(productsList);
            //Geef JSON terug
            return json.ToString();
        }

    }
    
=======
            List<Muziek> lijst = alles.ToList();
            var jsonSerialiser = new JavaScriptSerializer();
            var json = jsonSerialiser.Serialize(lijst);
            Debug.WriteLine(json.ToString());
           return json.ToString();
        }

        public String getMusic()
        {
            return "Hoi!";
        }
    }
>>>>>>> 69cfd330a9dec5e03f1e855adf8d95fb279eb001
}
