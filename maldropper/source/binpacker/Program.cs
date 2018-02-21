using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO.Compression;
using System.IO;
using System.Text;
using System.Reflection;

namespace binpacker
{
    class Program
    {
        static void Main(string[] args)
        {
            FileStream fs = File.Open("maldrp.exe", FileMode.Create);
            var maldrop = File.ReadAllBytes(@"K:\ezctf\testing\maldropper\maldrop\maldrop\bin\Debug\maldrop.exe");
            var payload = File.ReadAllBytes(@"K:\ezctf\testing\maldropper\maldrop\payload\bin\Debug\payload.exe");
            var flagbuilder = File.ReadAllBytes(@"K:\ezctf\testing\maldropper\maldrop\flagbuilder\bin\Debug\flagbuilder.exe");
            
            var spliter = Encoding.ASCII.GetBytes("[SPLITERATOR]");

            fs.Write(maldrop, 0, maldrop.Length);
            fs.Write(spliter, 0, spliter.Length);
            fs.Write(payload, 0, payload.Length);
            fs.Write(spliter, 0, spliter.Length);
            GZipStream gz = new GZipStream(fs, CompressionLevel.Fastest);
            gz.Write(flagbuilder, 0, flagbuilder.Length);
            gz.Close();
            fs.Close();
        }
    }
}
