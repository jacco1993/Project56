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



namespace WcfService2
{
    public class Muziek
    {
        public ObjectId _id { get; set; }
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

        public String getProducts()
        {
            var connectionString = "mongodb://localhost";
            var client = new MongoClient(connectionString);
            var server = client.GetServer();
            MongoDatabase database = server.GetDatabase("DevOpdr");
            MongoCollection<Muziek> muziek = database.GetCollection<Muziek>("Muziek");
            MongoCursor<Muziek> alles = muziek.FindAll();
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
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    
    
}
